---
name: socs-article-writer
description: Membantu menulis, merancang, memvalidasi, dan membuat file Word (.docx) untuk artikel explainer teknologi Bahasa Indonesia di website SOCS BINUS (socs.binus.ac.id/category/article) dan BINUS @Bekasi CSSE (binus.ac.id/bekasi/category/article/computer-science-software-engineering). Gunakan saat user ingin membuat, menulis, mengecek, atau mengubah artikel SOCS, BINUS, Bekasi CSSE, atau draft artikel teknologi yang akan diajukan ke redaksi.
---

# SOCS & Bekasi CSSE Article Writer

Skill ini membantu user menyusun artikel untuk website SOCS BINUS dan kanal BINUS @Bekasi CSSE (Computer Science – Software Engineering), dari nol sampai file Word siap ditinjau. Artikel terbit tetap dinilai dan disetujui manusia. Skill tidak mempublikasikan apa pun.

Aturan lengkap ada di `references/aturan.md` (target SOCS). Override target Bekasi CSSE ada di `references/target-bekasi.md`. Gaya menulis anti-slop ada di `references/gaya-menulis.md`. Contoh artikel terbit ada di `references/pola-artikel-terbit.md` (SOCS) dan `references/target-bekasi.md` (Bekasi CSSE). Template Markdown: `assets/template.md` (SOCS), `assets/template-bekasi.md` (Bekasi CSSE). Semua path di bawah relatif terhadap folder skill ini.

## 0. Pilih target (wajib sebelum intake)

- Tanyakan target redaksi: SOCS atau Bekasi CSSE. Default SOCS jika user tidak menyebut.
- Target Bekasi CSSE: artikel untuk `binus.ac.id/bekasi/category/article/computer-science-software-engineering`, ikut override di `references/target-bekasi.md`.
- Perbedaan kunci Bekasi CSSE: sapaan `Anda` boleh, tanpa baris byline (tidak perlu menanyakan nama penulis), figure `Gambar 1. ... (sumber: URL)`, judul bebas maks 15 kata / 110 karakter, subjudul min 2, paragraf min 3 kalimat, referensi bebas 3–8 entri tanpa tahun wajib.
- Validator dan builder mengikuti target: tambah `--target bekasi` di `scripts/validate_article.py` (nama flag CLI tetap `bekasi`), mulai draft dari `assets/template-bekasi.md`.

## Langkah kerja

### 1. Intake (wajib sebelum menulis apa pun)

Jangan mulai menulis sebelum informasi wajib berikut ada:

- Target SOCS: penulis wajib (nama lengkap, gelar, jabatan; tidak boleh dari memori, contoh, atau placeholder). Cek dulu `penulis.local.md` di root workspace. Jika ada, tampilkan isinya ke user dan minta konfirmasi. Jika tidak ada, tanyakan lalu simpan jawabannya ke `penulis.local.md` (file ini di-ignore git, jangan di-commit).
- Target Bekasi CSSE: penulis tidak perlu ditanya (tanpa baris byline; 9/9 sampel tanpa byline, author = `editorarticle`).

Informasi berikut boleh ditanyakan bersamaan atau dilewati jika user sudah memberikannya:

- Sudut pandang atau tagline (opsional). Jika tidak ada, buat 3 kandidat judul dengan format `Nama Teknologi: Tagline`.
- Keyword wajib (opsional). Semua keyword harus muncul di artikel.
- SDG (opsional). Jika tidak diminta, jangan dibahas.
- Gambar: sumber gambar jika user punya. Jika tidak, usulkan 2-3 gambar yang bisa dicari dari sumber resmi, atau ilustrasi AI-generated yang diberi label.
- Folder kerja untuk draft dan gambar, misalnya `drafts/<judul>/`.

Jika target SOCS dan penulis belum diketahui, berhenti dan tanyakan. Jangan menulis `[Nama]` atau `[Gelar]` ke dalam artikel.

### 2. Cek duplikat

- Target SOCS: ambil daftar judul dari https://socs.binus.ac.id/category/article/ dengan web_fetch. Telusuri halaman berikutnya lewat link pagination sampai topik yang sama ditemukan atau daftar habis. Situs ini punya banyak halaman, jadi tidak semua perlu dibuka.
- Target Bekasi CSSE: ambil daftar judul dari https://binus.ac.id/bekasi/category/article/computer-science-software-engineering/ (42+ halaman per Okt 2026; cek halaman awal + pencarian topik, tidak perlu semua).
- Cek juga folder arsip lokal di workspace jika ada (`published/socs/`, `submitted/socs/` untuk SOCS; `published/bekasi-csse/` untuk Bekasi CSSE). Folder ini di-ignore git.
- Jika ada topik yang mirip, beri tahu user dan tanyakan sebelum lanjut.

### 3. Riset dan verifikasi sumber

- Cari 3-5 sumber kredibel dengan remote_web_search. Prioritaskan docs resmi, blog vendor besar, paper, dan laporan riset.
- Verifikasi setiap URL dengan web_fetch. URL yang gagal dibuka tidak boleh masuk artikel.
- Catat setiap angka atau klaim di buku klaim (lihat 3b), beserta sumber dan buktinya. Angka yang tidak bisa diverifikasi jangan dipakai.
- Jangan pernah mengarang URL, angka, kutipan, atau nama peneliti.

### 3b. Buku klaim

Sebelum menulis, buat buku klaim di folder kerja draft (`drafts/socs/<judul>/klaim.md` atau `drafts/bekasi-csse/<judul>/klaim.md`) berisi tabel:

| No | Klaim | Jenis | URL sumber | Bukti | Status |
|---|---|---|---|---|---|

- Jenis: angka, persentase, ukuran waktu, tahun, nama peneliti, atau klaim perbandingan/kausal.
- Verifikasi setiap URL dengan web_fetch mode `full`. Mode `selective` hanya untuk pencarian awal. Kegagalan pencarian frasa di mode selective belum berarti klaim salah, jadi cek ulang di mode `full` sebelum mengubah status.
- Status `Terverifikasi` hanya jika bukti ditemukan di sumber, dan kolom Bukti berisi kutipan atau baris yang relevan. Status `Belum` jika tidak ditemukan.
- Klaim `Belum` dihapus dari draft, atau diubah jadi pernyataan umum tanpa angka.
- Klaim absolut (mewajibkan, menjamin, terbukti, 100%, selalu) hanya dipakai jika sumber memang mengatakannya sekuat itu. Kalau tidak, perhalus, misalnya "menyarankan" atau "umumnya".
- Figure buatan skrip: caption wajib menyebut bahwa itu ilustrasi atau grafik buatan penulis. URL di baris sumber adalah sumber fakta yang digambarkan, bukan sumber gambar.

### 4. Outline

- Target SOCS: kerangka berdasarkan urutan di `references/aturan.md` bagian 4 dan pola di `references/pola-artikel-terbit.md`.
- Target Bekasi CSSE: esai opini bebas berdasarkan pola di `references/target-bekasi.md` (judul → gambar → hook → 2–6 subjudul → referensi). Tampilkan outline singkat ke user. Lanjut ke draft kecuali user minta meninjau outline dulu.

### 5. Tulis draft (Markdown)

- Target 600-700 kata. Batas keras: SOCS 500-800; Bekasi CSSE 400-1100 (dari 34 arsip).
- Target SOCS: mulai dari `assets/template.md`, isi sesuai outline; format figure (`Figure N.` + baris `(URL)`), byline satu baris, dan referensi persis seperti `references/aturan.md`.
- Target Bekasi CSSE: mulai dari `assets/template-bekasi.md`, isi sesuai outline; sapaan `Anda` boleh; figure `Gambar 1. ... (sumber: URL)`; tanpa byline; referensi bebas 3–8 entri (lihat `references/target-bekasi.md`).
- Simpan draft sebagai `drafts/socs/<judul>/<judul>.md` (SOCS) atau `drafts/bekasi-csse/<judul>/<judul>.md` (Bekasi CSSE), dengan judul tanpa tanda `:` untuk nama file. Simpan gambar di folder yang sama, lalu tulis path relatif di Markdown, misalnya `![](figure-1.png)`.

### 6. Validasi

Jalankan validator dari folder skill ini (tambah `--target bekasi` untuk Bekasi CSSE):

    python scripts/validate_article.py "<path draft>.md" --target socs --keywords "keyword1,keyword2" --klaim "drafts/socs/<judul>/klaim.md"
    python scripts/validate_article.py "<path draft>.md" --target bekasi --keywords "keyword1,keyword2" --klaim "drafts/bekasi-csse/<judul>/klaim.md"

- Perbaiki semua temuan High dan Medium, lalu jalankan ulang sampai tidak ada High.
- Temuan Low dilaporkan ke user, dan diperbaiki jika mudah.
- Validator SOCS memeriksa aturan mekanis, angka terhadap buku klaim, kata absolut, pola gaya anti-slop (em dash, kontras biner gimmick, throat-clearing, meta-komentar, declaratif kosong, klaim melang, intensifier kosong), panjang paragraf (minimal 5 kalimat, aturan.md bagian 4), dan rujukan figure di kalimat (aturan.md bagian 6). Mode Bekasi CSSE memeriksa override `references/target-bekasi.md`: paragraf minimal 3 kalimat, subjudul minimal 2 (level bebas + bold-lead), tanpa cek `Anda`/byline/rujukan figure, tahun referensi opsional. Ia tidak bisa memastikan sumber itu benar. Kebenaran klaim tetap dipastikan lewat buku klaim dan dicek manusia.

### 7. Buat file Word

Jalankan builder dari folder skill ini (tambah `--target bekasi` untuk Bekasi CSSE, kertas Letter):

    python scripts/build_docx.py "<path draft>.md" "<path draft>.docx"
    python scripts/build_docx.py "<path draft>.md" "<path draft>.docx" --target bekasi

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
