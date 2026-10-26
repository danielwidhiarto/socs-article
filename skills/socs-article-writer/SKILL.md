---
name: socs-article-writer
description: Membantu menulis, merancang, memvalidasi, dan membuat file Word (.docx) untuk artikel explainer teknologi Bahasa Indonesia di website SOCS BINUS (socs.binus.ac.id/category/article). Gunakan saat user ingin membuat, menulis, mengecek, atau mengubah artikel SOCS, BINUS, atau draft artikel teknologi yang akan diajukan ke redaksi.
---

# SOCS Article Writer

Skill ini membantu user menyusun artikel untuk website SOCS BINUS dari nol sampai file Word siap ditinjau. Artikel terbit tetap dinilai dan disetujui manusia. Skill tidak mempublikasikan apa pun.

Aturan lengkap ada di `references/aturan.md`. Contoh artikel terbit ada di `references/pola-artikel-terbit.md`. Template Markdown ada di `assets/template.md`. Semua path di bawah relatif terhadap folder skill ini.

## Langkah kerja

### 1. Intake

Pastikan informasi berikut sudah ada. Tanyakan yang belum ada, dan lewati yang sudah diberikan user:

- Topik: satu teknologi atau konsep. Jika user belum punya, tawarkan 2-3 pilihan dari klaster yang sesuai.
- Sudut pandang atau tagline (opsional). Jika tidak ada, buat 3 kandidat judul dengan format `Nama Teknologi: Tagline`.
- Keyword wajib (opsional). Semua keyword harus muncul di artikel.
- SDG (opsional). Jika tidak diminta, jangan dibahas.
- Penulis: nama, gelar, dan jabatan. Wajib untuk byline. Tanyakan ketiganya, jangan mengisi dari memori atau dari contoh.
- Gambar: sumber gambar jika user punya. Jika tidak, usulkan 2-3 gambar yang bisa dicari dari sumber resmi, atau ilustrasi AI-generated yang diberi label.
- Folder kerja untuk draft dan gambar, misalnya `drafts/<judul>/`.

### 2. Cek duplikat

- Ambil daftar judul dari https://socs.binus.ac.id/category/article/ dengan web_fetch. Telusuri halaman berikutnya lewat link pagination sampai topik yang sama ditemukan atau daftar habis. Situs ini punya banyak halaman, jadi tidak semua perlu dibuka.
- Cek juga folder `published/` dan `submitted/` di workspace jika ada.
- Jika ada topik yang mirip, beri tahu user dan tanyakan sebelum lanjut.

### 3. Riset dan verifikasi sumber

- Cari 3-5 sumber kredibel dengan remote_web_search. Prioritaskan docs resmi, blog vendor besar, paper, dan laporan riset.
- Verifikasi setiap URL dengan web_fetch. URL yang gagal dibuka tidak boleh masuk artikel.
- Catat setiap angka atau klaim beserta sumbernya. Angka yang tidak bisa diverifikasi jangan dipakai.
- Jangan pernah mengarang URL, angka, kutipan, atau nama peneliti.

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

    python scripts/validate_article.py "<path draft>.md" --keywords "keyword1,keyword2"

- Perbaiki semua temuan High dan Medium, lalu jalankan ulang sampai tidak ada High.
- Temuan Low dilaporkan ke user, dan diperbaiki jika mudah.
- Validator hanya memeriksa aturan mekanis. Kualitas tulisan, akurasi klaim, dan relevansi sumber tetap perlu dicek manusia.

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
