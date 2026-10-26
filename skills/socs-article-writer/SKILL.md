---
name: socs-article-writer
description: Membantu menulis, merancang, dan memvalidasi artikel explainer teknologi Bahasa Indonesia untuk website SOCS BINUS (socs.binus.ac.id/category/article). Gunakan saat user ingin membuat, menulis, atau mengecek artikel SOCS, BINUS, atau draft artikel teknologi yang akan diajukan ke redaksi.
---

# SOCS Article Writer

Skill ini membantu user menyusun artikel untuk website SOCS BINUS dari nol sampai draft siap ditinjau. Artikel terbit tetap dinilai dan disetujui manusia. Skill tidak mempublikasikan apa pun.

Aturan lengkap ada di `references/aturan.md`. Pola artikel yang sudah terbit ada di `references/pola-artikel-terbit.md`. Template kerangka ada di `assets/template.md`.

## Langkah kerja

### 1. Intake

Pastikan informasi berikut sudah ada. Tanyakan yang belum ada, dan lewati yang sudah diberikan user:

- Topik: satu teknologi atau konsep. Jika user belum punya, tawarkan 2-3 pilihan dari klaster yang sesuai.
- Sudut pandang atau tagline (opsional). Jika tidak ada, buat 3 kandidat judul dengan format `Nama Teknologi: Tagline`.
- Keyword wajib (opsional). Semua keyword harus muncul di artikel.
- SDG (opsional). Jika tidak diminta, jangan dibahas.
- Penulis: nama, gelar, dan jabatan. Wajib untuk byline. Jangan mengisi nama dari memori atau dari contoh di referensi.
- Gambar: sumber gambar jika user punya. Jika tidak, usulkan 2-3 gambar yang bisa dicari dari sumber resmi, atau ilustrasi AI-generated yang diberi label.

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

### 5. Tulis draft

- Bahasa Indonesia ragam populer-ilmiah. Istilah teknis tetap Inggris.
- Target 600-700 kata (seluruh teks, seperti Word). Batas keras 500-800.
- Mulai dari template di `assets/template.md`, lalu isi sesuai outline.
- Gunakan `Figure N. Deskripsi (URL)` satu baris, dengan penomoran berurutan dari 1.
- Simpan di `drafts/` dengan nama file judul tanpa tanda `:`, misalnya `drafts/Deno vs Node.js Siapa Raja Baru Dunia JavaScript.md`. Buat folder `drafts/` jika belum ada.

### 6. Validasi

Jalankan validator dari root workspace:

    python scripts/validate_article.py "<path draft>.md" --keywords "keyword1,keyword2"

Jalankan dari folder tempat skill ini dipasang (folder yang berisi SKILL.md). Path draft boleh absolut atau relatif terhadap folder kerja user.

- Perbaiki semua temuan High dan Medium, lalu jalankan ulang sampai tidak ada High.
- Temuan Low dilaporkan ke user, dan diperbaiki jika mudah.
- Validator hanya memeriksa aturan mekanis. Kualitas tulisan, akurasi klaim, dan relevansi sumber tetap perlu dicek manusia.

### 7. Serahkan ke user

Laporkan hal berikut secara ringkas:

- Path draft.
- Hasil validator (jumlah kata, subjudul, figure, referensi, dan sisa temuan Low).
- Daftar sumber yang sudah diverifikasi beserta URL-nya.
- Asumsi atau keputusan yang dibuat selama menulis.
- Pengingat bahwa artikel perlu ditinjau manusia sebelum diajukan.

Jika user ingin file Word, konversi dengan `pandoc "drafts/<nama>.md" -o "drafts/<nama>.docx"`. Catat bahwa gambar tidak ikut tersisip otomatis.

## Batasan

- Jangan mempublikasikan, mengunggah, atau mengirim artikel ke website atau redaksi.
- Jangan membuat URL, angka, kutipan, atau nama orang yang tidak bisa diverifikasi.
- Jangan memakai data pribadi (nama, gelar, kontak) yang tidak diberikan user untuk artikel ini.
- Jangan menambahkan pembahasan SDG jika user tidak memintanya.
- Jangan membuat blok kode panjang. Artikel ini explainer, bukan tutorial.
- Jika user meminta artikel tentang topik sensitif (kesehatan, hukum, atau keuangan), bantu dari sisi teknologi saja, dan jangan memberi nasihat profesional.
