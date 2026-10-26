---
name: socs-article-writer
description: Membantu menulis, merancang, memvalidasi, dan membuat file Word (.docx) untuk artikel explainer teknologi Bahasa Indonesia di website SOCS BINUS (socs.binus.ac.id/category/article). Gunakan saat user ingin membuat, menulis, mengecek, atau mengubah artikel SOCS, BINUS, atau draft artikel teknologi yang akan diajukan ke redaksi.
---

# SOCS Article Writer

Skill ini membantu user menyusun artikel untuk website SOCS BINUS dari nol sampai file Word siap ditinjau. Artikel terbit tetap dinilai dan disetujui manusia. Skill tidak mempublikasikan apa pun.

Aturan lengkap ada di `references/aturan.md`. Contoh artikel terbit ada di `references/pola-artikel-terbit.md`. Template Markdown ada di `assets/template.md`. Semua path di bawah relatif terhadap folder skill ini.

## Langkah kerja

### 1. Intake (wajib sebelum menulis apa pun)

Jangan mulai menulis sebelum informasi wajib berikut ada. Informasi penulis bersifat wajib dan tidak boleh diisi dari memori, contoh, atau placeholder:

- Penulis: nama lengkap, gelar, dan jabatan. Cek dulu `penulis.local.md` di root workspace. Jika ada, tampilkan isinya ke user dan minta konfirmasi. Jika tidak ada, tanyakan lalu simpan jawabannya ke `penulis.local.md` (file ini di-ignore git, jangan di-commit).
- Topik: satu teknologi atau konsep. Jika user belum punya, tawarkan 2-3 pilihan dari klaster yang sesuai.

Informasi berikut boleh ditanyakan bersamaan atau dilewati jika user sudah memberikannya:

- Sudut pandang atau tagline (opsional). Jika tidak ada, buat 3 kandidat judul dengan format `Nama Teknologi: Tagline`.
- Keyword wajib (opsional). Semua keyword harus muncul di artikel.
- SDG (opsional). Jika tidak diminta, jangan dibahas.
- Gambar: sumber gambar jika user punya. Jika tidak, usulkan 2-3 gambar yang bisa dicari dari sumber resmi, atau ilustrasi AI-generated yang diberi label.
- Folder kerja untuk draft dan gambar, misalnya `drafts/<judul>/`.

Jika penulis belum diketahui, berhenti dan tanyakan. Jangan menulis `[Nama]` atau `[Gelar]` ke dalam artikel.

### 2. Cek duplikat

- Ambil daftar judul dari https://socs.binus.ac.id/category/article/ dengan web_fetch. Telusuri halaman berikutnya lewat link pagination sampai topik yang sama ditemukan atau daftar habis. Situs ini punya banyak halaman, jadi tidak semua perlu dibuka.
- Cek juga folder `published/` dan `submitted/` di workspace jika ada.
- Jika ada topik yang mirip, beri tahu user dan tanyakan sebelum lanjut.

### 3. Riset dan verifikasi sumber

- Cari 3-5 sumber kredibel dengan remote_web_search. Prioritaskan docs resmi, blog vendor besar, paper, dan laporan riset.
- Verifikasi setiap URL dengan web_fetch. URL yang gagal dibuka tidak boleh masuk artikel.
- Catat setiap angka atau klaim di buku klaim (lihat 3b), beserta sumber dan buktinya. Angka yang tidak bisa diverifikasi jangan dipakai.
- Jangan pernah mengarang URL, angka, kutipan, atau nama peneliti.

### 3b. Buku klaim

Sebelum menulis, buat `drafts/<judul>/klaim.md` berisi tabel:

| No | Klaim | Jenis | URL sumber | Bukti | Status |
|---|---|---|---|---|---|

- Jenis: angka, persentase, ukuran waktu, tahun, nama peneliti, atau klaim perbandingan/kausal.
- Verifikasi setiap URL dengan web_fetch mode `full`. Mode `selective` hanya untuk pencarian awal. Kegagalan pencarian frasa di mode selective belum berarti klaim salah, jadi cek ulang di mode `full` sebelum mengubah status.
- Status `Terverifikasi` hanya jika bukti ditemukan di sumber, dan kolom Bukti berisi kutipan atau baris yang relevan. Status `Belum` jika tidak ditemukan.
- Klaim `Belum` dihapus dari draft, atau diubah jadi pernyataan umum tanpa angka.
- Klaim absolut (mewajibkan, menjamin, terbukti, 100%, selalu) hanya dipakai jika sumber memang mengatakannya sekuat itu. Kalau tidak, perhalus, misalnya "menyarankan" atau "umumnya".
- Figure buatan skrip: caption wajib menyebut bahwa itu ilustrasi atau grafik buatan penulis. URL di baris sumber adalah sumber fakta yang digambarkan, bukan sumber gambar.

### 4. Outline

Susun kerangka berdasarkan urutan di `references/aturan.md` bagian 4 dan pola di `references/pola-artikel-terbit.md`. Tampilkan outline singkat ke user. Lanjut ke draft kecuali user minta meninjau outline dulu.

### 5. Tulis draft (Markdown)

- Bahasa Indonesia ragam populer-ilmiah. Istilah teknis tetap Inggris.
- Target 600-700 kata. Batas keras 500-800.
- Mulai dari `assets/template.md`, lalu isi sesuai outline.
- Simpan draft sebagai `drafts/<judul>/<judul>.md`, dengan judul tanpa tanda `:` untuk nama file. Simpan gambar di folder yang sama, lalu tulis path relatif di Markdown, misalnya `![](figure-1.png)`.
- Format figure (caption `Figure N.` dengan sumber di baris berikutnya), byline (satu baris), dan referensi harus persis seperti di `references/aturan.md`.

### 6. Validasi

Jalankan validator dari folder skill ini:

    python scripts/validate_article.py "<path draft>.md" --keywords "keyword1,keyword2" --klaim "drafts/<judul>/klaim.md"

- Perbaiki semua temuan High dan Medium, lalu jalankan ulang sampai tidak ada High.
- Temuan Low dilaporkan ke user, dan diperbaiki jika mudah.
- Validator memeriksa aturan mekanis, angka terhadap buku klaim, dan kata absolut. Ia tidak bisa memastikan sumber itu benar. Kebenaran klaim tetap dipastikan lewat buku klaim dan dicek manusia.

### 7. Buat file Word

Jalankan builder dari folder skill ini:

    python scripts/build_docx.py "<path draft>.md" "<path draft>.docx"

- Builder meniru format artikel acuan *Agentic Coding* dengan kertas A4 (lihat `references/aturan.md` bagian 15).
- Jika builder berhenti karena gambar tidak ditemukan, perbaiki path gambar di Markdown lalu jalankan ulang.
- Setelah dibuat, sebutkan ke user bahwa file perlu dibuka di Word untuk pengecekan visual, karena skill tidak bisa membuka Word.

### 8. Serahkan ke user

Laporkan hal berikut secara ringkas:

- Path file `.docx` dan `.md`.
- Hasil validator: jumlah kata, subjudul, figure, referensi, dan sisa temuan Low.
- Daftar sumber yang sudah diverifikasi beserta URL-nya.
- Asumsi atau keputusan yang dibuat selama menulis.
- Pengingat bahwa artikel perlu ditinjau manusia sebelum diajukan.

## Batasan

- Jangan mempublikasikan, mengunggah, atau mengirim artikel ke website atau redaksi.
- Jangan membuat URL, angka, kutipan, atau nama orang yang tidak bisa diverifikasi.
- Jangan memakai data pribadi (nama, gelar, kontak) yang tidak diberikan user untuk artikel ini.
- Jangan menambahkan pembahasan SDG jika user tidak memintanya.
- Jangan membuat blok kode panjang. Artikel ini explainer, bukan tutorial.
- Jika user meminta artikel tentang topik sensitif (kesehatan, hukum, atau keuangan), bantu dari sisi teknologi saja, dan jangan memberi nasihat profesional.
