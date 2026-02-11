from typing import Type
from crewai import Agent, Task, Crew, Process, LLM
from crewai.tools import BaseTool  # Import dari sini biasanya aman
from pydantic import BaseModel, Field

# ------------------------------------------
# 1. DEFINISI STRUKTUR INPUT (Schema)
# ------------------------------------------
class HitungLuasInput(BaseModel):
    """Input schema untuk alat hitung luas."""
    panjang: int = Field(..., description="Panjang tanah dalam meter.")
    lebar: int = Field(..., description="Lebar tanah dalam meter.")

# ------------------------------------------
# 2. DEFINISI LOGIKA TOOL (Class BaseTool)
# ------------------------------------------
class HitungLuasTanahTool(BaseTool):
    name: str = "Kalkulator Luas Tanah"
    description: str = "Gunakan alat ini untuk menghitung luas tanah berdasarkan panjang dan lebar."
    args_schema: Type[BaseModel] = HitungLuasInput

    def _run(self, panjang: int, lebar: int) -> str:
        # Masukkan logika Python kamu di sini
        luas = panjang * lebar
        return f"Luas tanah adalah {luas} meter persegi."

# ------------------------------------------
# 3. CARA PASANG KE AGENT
# ------------------------------------------

# A. Inisialisasi Tool-nya dulu (PENTING!)
alat_hitung = HitungLuasTanahTool()

# B. Setup LLM (Pakai OpenRouter/Gemini saran sebelumnya)
llm = LLM(
    model="ollama/llama3.1:8b",
    base_url="http://localhost:11434",
)

# C. Masukkan ke Agent
mandor = Agent(
    role='Mandor Bangunan',
    goal='Menghitung kebutuhan lahan',
    backstory='Ahli sipil berpengalaman.',
    tools=[alat_hitung], # <--- Masukkan variable alat_hitung di sini
    llm=llm,
    verbose=True
)

# D. Test Jalan
task = Task(
    description="Hitung luas tanah jika panjangnya 20m dan lebarnya 15m.",
    expected_output="Jawaban singkat luas tanah.",
    agent=mandor
)

crew = Crew(agents=[mandor], tasks=[task], verbose=True)
result = crew.kickoff()
print(result)