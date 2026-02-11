import os
import asyncio
from pydantic import BaseModel
from typing import List, Dict, Any

from crewai import Agent, Task, Crew, LLM
from crewai.flow.flow import Flow, listen, start
from dotenv import load_dotenv

load_dotenv()

# LLM Configuration
llm = LLM(
    model="ollama/qwen3:0.6b-q4_K_M",
    base_url="http://localhost:11434"
)

# PYDANTIC MODELS untuk Output

class ProcessingResult(BaseModel):
    """Result dari text atau audio processing"""
    source: str  # "text" atau "audio"
    content: str
    confidence: float = 1.0
    metadata: Dict[str, Any] = {}

class FeedbackResult(BaseModel):
    """Result dari feedback analysis"""
    text_quality: str
    audio_quality: str
    recommendations: List[str]
    final_score: float

# Agent untuk Text Processing
text_processor = Agent(
    role="Text Processor",
    goal="Clean dan normalize text input dengan akurat",
    backstory="Expert text processor dengan 10 tahun pengalaman",
    llm=llm,
    verbose=True
)

# Agent untuk Audio Processing
audio_processor = Agent(
    role="Audio Transcriber",
    goal="Convert audio ke text dengan akurasi tinggi",
    backstory="Specialist speech-to-text dengan expertise multilingual",
    llm=llm,
    verbose=True
)

# Agent untuk Feedback Analysis
feedback_analyst = Agent(
    role="Quality Analyst",
    goal="Analyze dan compare hasil processing",
    backstory="Senior QA analyst dengan specialty di quality assessment",
    llm=llm,
    verbose=True
)

# CREWS DEFINITION
# Crew 1: Text Processing Crew
def create_text_crew():
    """Create crew untuk text processing"""
    text_task = Task(
        description="""
        Process text input: {text_input}
        
        Tasks:
        1. Clean special characters
        2. Normalize whitespace
        3. Ensure coherence
        
        Return JSON format:
        {{
            "source": "text",
            "content": "processed text",
            "confidence": 0.95,
            "metadata": {{"word_count": 100}}
        }}
        """,
        expected_output="Processed text dalam JSON format",
        agent=text_processor
    )
    
    return Crew(
        agents=[text_processor],
        tasks=[text_task],
        verbose=True
    )

# Crew 2: Audio Processing Crew
def create_audio_crew():
    """Create crew untuk audio processing"""
    audio_task = Task(
        description="""
        Transcribe audio: {audio_input}
        
        Tasks:
        1. Extract text dari audio
        2. Clean dan format
        3. Ensure accuracy
        
        Return JSON format:
        {{
            "source": "audio",
            "content": "transcribed text",
            "confidence": 0.92,
            "metadata": {{"duration": "30s"}}
        }}
        """,
        expected_output="Transcribed text dalam JSON format",
        agent=audio_processor
    )
    
    return Crew(
        agents=[audio_processor],
        tasks=[audio_task],
        verbose=True
    )

# Crew 3: Feedback Analysis Crew
def create_feedback_crew():
    """Create crew untuk feedback analysis"""
    feedback_task = Task(
        description="""
        Analyze hasil dari text dan audio processing:
        
        Text Result: {text_result}
        Audio Result: {audio_result}
        
        Tasks:
        1. Evaluate quality masing-masing
        2. Compare similarities dan differences
        3. Provide recommendations
        4. Give overall score (0-10)
        
        Return JSON format:
        {{
            "text_quality": "Good - clean and coherent",
            "audio_quality": "Excellent - accurate transcription",
            "recommendations": ["recommendation 1", "recommendation 2"],
            "final_score": 8.5
        }}
        """,
        expected_output="Comprehensive feedback dalam JSON",
        agent=feedback_analyst
    )
    
    return Crew(
        agents=[feedback_analyst],
        tasks=[feedback_task],
        verbose=True
    )

# STATE DEFINITION
class ParallelProcessingState(BaseModel):
    """State untuk parallel processing flow"""
    text_input: str = ""
    audio_input: str = ""
    text_result: Dict[str, Any] = {}
    audio_result: Dict[str, Any] = {}
    feedback: Dict[str, Any] = {}

# FLOW IMPLEMENTATION
class ParallelProcessingFlow(Flow[ParallelProcessingState]):
    """
    Flow yang menjalankan 2 crews secara parallel,
    kemudian menganalisis hasilnya dengan feedback crew
    """
    
    @start()
    async def run_parallel_crews(self):
        """
        Step 1: Jalankan text_crew dan audio_crew secara BERSAMAAN
        Menggunakan asyncio.gather() untuk true parallelism
        """
        print("="*80)
        print("STEP 1: Running Text & Audio Crews in Parallel")
        print("="*80)
        
        # Prepare inputs
        text_input = self.state.text_input or "Sample text with noise!!! and special chars..."
        audio_input = self.state.audio_input or "Audio: 'Hello, this is a test transcription'"
        
        print(f"\nText Input: {text_input}")
        print(f"Audio Input: {audio_input}")
        print(f"\nStarting parallel execution...\n")
        
        # Create crews
        text_crew = create_text_crew()
        audio_crew = create_audio_crew()
        
        # PARALLEL EXECUTION dengan asyncio.gather()
        # Kedua crew jalan BERSAMAAN (tidak sequential!)
        text_result, audio_result = await asyncio.gather(
            text_crew.kickoff_async(inputs={"text_input": text_input}),
            audio_crew.kickoff_async(inputs={"audio_input": audio_input})
        )
        
        print("\nBoth crews completed!\n")
        
        # Extract results
        text_output = text_result.raw if hasattr(text_result, 'raw') else str(text_result)
        audio_output = audio_result.raw if hasattr(audio_result, 'raw') else str(audio_result)
        
        print("Text Processing Result:")
        print(f"   {text_output[:200]}...\n")
        
        print("Audio Processing Result:")
        print(f"   {audio_output[:200]}...\n")
        
        # Update state dengan hasil parallel execution
        self.state.text_result = {"raw": text_output}
        self.state.audio_result = {"raw": audio_output}
        
        # Return dictionary untuk diteruskan ke listener
        return {
            "text_result": text_output,
            "audio_result": audio_output
        }
    
    @listen(run_parallel_crews)
    async def analyze_results(self, parallel_results):
        """
        Step 2: Analyze hasil dari kedua crews
        Method ini akan OTOMATIS dipanggil setelah run_parallel_crews selesai
        """
        print("="*80)
        print("STEP 2: Analyzing Results with Feedback Crew")
        print("="*80)
        
        # Ambil hasil dari parameter (dikirim dari run_parallel_crews)
        text_result = parallel_results.get("text_result", "No text result")
        audio_result = parallel_results.get("audio_result", "No audio result")
        
        print(f"\nReceived Text Result: {text_result[:100]}...")
        print(f"Received Audio Result: {audio_result[:100]}...\n")
        
        # Create feedback crew
        feedback_crew = create_feedback_crew()
        
        print("Running feedback analysis...\n")
        
        # Run feedback crew dengan hasil dari parallel execution
        feedback_result = await feedback_crew.kickoff_async(inputs={
            "text_result": text_result,
            "audio_result": audio_result
        })
        
        feedback_output = feedback_result.raw if hasattr(feedback_result, 'raw') else str(feedback_result)
        
        print("Feedback analysis completed!\n")
        print("Feedback Result:")
        print(f"   {feedback_output}\n")
        
        # Update state
        self.state.feedback = {"raw": feedback_output}
        
        return feedback_output
    
    @listen(analyze_results)
    def save_results(self, feedback):
        """
        Step 3: Save semua hasil ke file
        Method ini akan OTOMATIS dipanggil setelah analyze_results selesai
        """
        print("="*80)
        print("STEP 3: Saving Results")
        print("="*80)
        
        import json
        
        os.makedirs("output", exist_ok=True)
        
        # Compile semua hasil
        final_output = {
            "text_processing": self.state.text_result,
            "audio_processing": self.state.audio_result,
            "feedback_analysis": {"raw": feedback}
        }
        
        output_file = "output/parallel_processing_results.json"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(final_output, f, indent=2, ensure_ascii=False)
        
        print(f"\nResults saved to: {output_file}")
        print("\n" + "="*80)
        print("FLOW COMPLETED SUCCESSFULLY!")
        print("="*80)
        
        return final_output

# ============================================
# MAIN EXECUTION
# ============================================

if __name__ == "__main__":
    import nest_asyncio
    nest_asyncio.apply()
    
    print("\n" + "="*80)
    print("CrewAI Flow - Parallel Crews Execution Demo")
    print("="*80)
    
    # ===== DEMO 1: Basic Parallel Flow =====
    print("\n\n### DEMO 1: Basic Parallel Flow ###\n")
    
    flow = ParallelProcessingFlow()
    flow.state.text_input = "This is a sample text with special chars!!! and noise..."
    flow.state.audio_input = "Audio transcript: 'Hello world, this is a test recording'"
    
    # Kickoff the flow
    result = flow.kickoff()
    
    print("\n" + "="*80)
    print("FINAL RESULT:")
    print("="*80)
    print(result)
    
    print("\n\nAll demos completed!")