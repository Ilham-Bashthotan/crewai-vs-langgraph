# List of misconceptions 

## Miskonsepsi (Misconception)

- Intentional bug (IB): Asumsi bahwa sistem dapat membuat pilihan berdasarkan keadaan masa depan mesin. 
- While demon (WD): Eksekusi loop kondisional (perulangan bersyarat) dihentikan secara preventif berdasarkan perubahan kondisi keluar selama loop berjalan. 
- Mix of intentional bug and while demon (IBxWD): Berhenti secara preventif di tengah jalan loop karena kondisi keluar akan berubah dengan eksekusi pernyataan berikutnya. 
- Conditional loop as conditional statement without alternative (WhileIf): Loop kondisional dieksekusi seperti pernyataan kondisional, jadi meskipun kondisi keluar belum berubah, kode di dalam blok hanya dijalankan satu kali. 
- Conditional statement without alternative as conditional loop (IfWhile): Pernyataan kondisional tanpa alternatif dieksekusi layaknya sebuah loop kondisional. 
- Executed once (EO): Setiap pernyataan harus dieksekusi setidaknya satu kali. 
- Drop through error (DT): Pernyataan-pernyataan setelah pernyataan kondisional tanpa alternatif tidak dieksekusi, terlepas dari apakah kondisinya benar atau tidak. 

## Eror (Error)

- Full program as loop (SNIP): Pernyataan kondisional dan pernyataan-pernyataan berikutnya dieksekusi sebagai loop, bahkan jika kondisinya salah. 
- Ignore nesting 1 (IN1): Loop luar dan dalam dieksekusi secara saling bergantung (interdependen). 
- Ignore nesting 2 (IN2): Counter (penghitung) dari loop dalam dengan jumlah pengulangan tetap menimpa counter luar, dan pernyataan-pernyataan dieksekusi sebagai satu badan loop. 
- Ignore outer loop (IOL): Loop luar dengan jumlah pengulangan tetap diabaikan. Tidak ada pengulangan loop luar yang terjadi. 
- Execute n statement (EXN): Counter dari sebuah loop dengan jumlah pengulangan tetap mewakili berapa banyak pernyataan yang dieksekusi. 
- Multiply counter (MC): Counter dari loop bersarang dengan jumlah pengulangan tetap dikalikan. 
- Wrong order (WO): Mengeksekusi program dari bawah ke atas. 
## Ketidaktelitian (Carelessness)

- Mistyped action (AS): Hilangnya atau penambahan suatu tindakan (misalnya: eksekusi tambahan pernyataan gerak) di suatu tempat dalam jejak (trace) jika itu bukan karakteristik dari suatu miskonsepsi. 
- Miscounting loop (Loop+ atau Loop-): Hilangnya atau penambahan loop terakhir jika itu bukan karakteristik dari suatu miskonsepsi, yang disebabkan kemungkinan salah hitung.