# Aturan Artikel SOCS BINUS

Ini satu-satunya sumber aturan untuk skill ini. Contoh artikel terbit ada di `pola-artikel-terbit.md` dan hanya perlu dibaca saat butuh contoh. Format dokumen Word mengikuti artikel acuan *Agentic Coding* (lihat bagian 15), dengan kertas A4.

Tingkat keparahan: High = artikel gagal validasi. Medium = wajib diperbaiki. Low = saran.

## 1. Panjang

- Hitung seluruh teks artikel seperti Word: judul, isi, tabel, caption, byline, dan referensi, masing-masing dihitung sekali.
- Minimum 500 kata dan maksimum 800 kata (High jika dilanggar).
- Target 600 sampai 700 kata (Low jika di luar target).
- Kalau materi terlalu berat untuk 800 kata, pecah jadi artikel terpisah.

## 2. Judul dan nama file

- Format yang dianjurkan: `Nama Teknologi: Tagline`. Tanda `:` opsional, jadi kalau tidak ada hanya Low.
- Maksimal 10 kata dan 70 karakter (Medium jika lebih).
- Tagline berisi manfaat atau kontras, bukan deskripsi generik.
  - Bagus: `Smart Contract: Kode yang Bisa Berjanji`
  - Bagus: `Deno vs Node.js: Siapa Raja Baru Dunia JavaScript?`
  - Hindari: `Pengenalan Smart Contract`
- Judul di baris pertama artikel harus sama persis dengan judul yang dipilih user (High jika tidak).
- Nama file: judul tanpa `:` dan tanpa `_`, ganti dengan spasi. Contoh: `Smart Contract Kode yang Bisa Berjanji.docx`.

## 3. Hook pembuka

- Mulai dari adegan, masalah sehari-hari, atau fenomena konkret.
- Pola yang sah: "Bayangkan ...", "Pernahkah kamu/kita ...?", "Banyak orang ...".
- Dilarang: definisi langsung di kalimat pertama (Medium).

## 4. Struktur

Urutan wajib:

1. Judul, lalu Figure 1 tepat di bawahnya.
2. Hook (1 sampai 2 paragraf).
3. Apa itu X: definisi dan asal-usul singkat (siapa dan tahun).
4. Cara kerja atau fitur, dalam bentuk paragraf atau daftar bullet `- istilah: penjelasan`.
5. Contoh penggunaan nyata: 3 sampai 4 skenario.
6. Tabel (lihat bagian 7).
7. Kelebihan dan keterbatasan, atau tantangan. Jujur dan spesifik, 2 sampai 4 poin.
8. Kesimpulan: minimal 5 kalimat. Satu pemikiran ke depan, satu kalimat yang kembali ke dunia nyata. Tanpa kalimat bombastis.
9. Byline `Penulis:`.
10. Referensi.

Aturan tambahan:
- Setiap paragraf prosa minimal 5 kalimat, tanpa pengecualian (Medium). Paragraf yang kurang dari 5 kalimat digabung dengan paragraf sebelumnya dalam bagian yang sama. Jika di bagian itu belum ada paragraf sebelumnya, gabungkan dengan paragraf berikutnya. Jika kalimatnya belum cukup, tambahkan kalimat yang masih satu ide, bukan kalimat kosong.
- Buat paragraf baru hanya saat ide berpindah, misalnya dari adegan ke masalah, atau dari masalah ke solusi. Jangan memecah paragraf yang masih satu ide hanya untuk memenuhi jumlah paragraf atau kalimat.
- Jika satu paragraf memuat dua ide berbeda dan lebih dari 5 kalimat, pecah di titik pergeseran ide.
- Hook: 1 paragraf minimal 5 kalimat. Hook 2 paragraf hanya jika masing-masing paragraf minimal 5 kalimat dan ada pergeseran dari adegan ke masalah.
- Dua paragraf berurutan tidak boleh diawali kata yang sama (Medium).
- Istilah teknis dijelaskan sekali. Penjelasan dalam kurung maksimal 7 kata, dan maksimal satu per paragraf (Low).
- Fokus pada dampak dan insight, bukan syntax atau konfigurasi.

## 5. Subjudul

- Minimal 3 subjudul (High jika kurang). Di Markdown pakai `##`.
- Di dokumen Word, subjudul adalah paragraf tebal, rata kiri-kanan, tanpa indent.
- Satu subjudul memuat keyword utama.

## 6. Figure

- Figure 1 wajib (Medium jika tidak ada), diletakkan di bawah judul.
- Total 2 sampai 4 figure, dianjurkan (Low di luar itu).
- Tulis gambar dan caption dengan urutan ini:

```
![](nama-file-gambar.png)
Figure N. Deskripsi singkat gambar
(URL sumber)
```

- Caption memakai titik setelah nomor: `Figure N.` (Medium jika memakai titik dua).
- Sumber harus di baris berikutnya dalam kurung: `(URL)` atau `(AI Generated)` (Medium jika tidak ada).
- Lebar gambar default 14,3 cm. Untuk mengubah, tambahkan `{w=13.2cm}` setelah path. Tinggi mengikuti proporsi gambar kecuali ditambah `h=...cm`.
- Penomoran berurutan mulai dari 1 tanpa lompatan (Medium).
- URL sumber wajib untuk gambar bukan AI-generated. URL hanya boleh dari sumber yang sudah diverifikasi, tidak boleh karangan (High).
- Gambar AI-generated boleh dengan `(AI Generated)` sebagai pengganti URL.
- Minimal satu figure harus dari sumber kredibel, bukan AI-generated.
- Setiap figure wajib disebut secara eksplisit di paragraf teks, misalnya "Secara umum, prosesnya dapat dijelaskan melalui tahapan pada figure 1 berikut:". Figure yang hanya dipajang tanpa disebut di teks ditandai Medium.
- Figure buatan skrip (diagram atau grafik yang digambar penulis) harus diberi caption yang jujur, misalnya "Ilustrasi penulis" atau "Grafik penulis berdasarkan data ...".
- Untuk figure buatan skrip, URL di baris sumber adalah sumber fakta yang digambarkan, bukan sumber gambar. Jangan memakai URL yang menyiratkan gambar diambil dari sana.

## 7. Tabel

- Satu tabel dianjurkan (Low jika tidak ada). Bukan wajib.
- Untuk topik perbandingan, pakai format `Aspek | A | B` dengan 5 sampai 7 aspek.
- Baris pertama tabel adalah header (tebal).
- Caption tabel tidak diatur. Jangan pakai `Table N.` (Low).

## 8. Gaya dan bahasa

- Bahasa Indonesia ragam populer-ilmiah: santai tapi kredibel. Bukan bahasa skripsi, bukan slang.
- Istilah teknis tetap Inggris, misalnya cloud, framework, deploy, open source, pipeline.
- Pakai "kamu" dan "kita". Jangan pakai "Anda" (Low).
- Boleh analogi sehari-hari dan pertanyaan retoris.
- Tanpa blok kode. Artikel ini explainer, bukan tutorial (Low).
- Target pembaca: mahasiswa Informatika dan developer pemula.

## 9. Byline

- Satu baris, persis seperti artikel acuan. Label `Penulis:` dan nama dicetak tebal:

```
Penulis: [Nama], [Gelar] – [Jabatan]
```

- Pemisah sebelum jabatan adalah en dash `–` dengan spasi di kiri dan kanan.
- Nama, gelar, dan jabatan diambil dari input user. Agent wajib menanyakannya, jangan mengisi dari memori atau dari contoh.
- Blok ini wajib ada di bagian penutup (Medium jika tidak ada atau formatnya salah).

## 10. Referensi

- Heading `## Referensi` berdiri sendiri. Entri mulai di baris berikutnya.
- Jumlah 3 sampai 7 (High jika kurang dari 3, Medium jika lebih dari 7). Ideal 3 sampai 5.
- Satu entri per baris (Medium jika dua entri menempel dalam satu baris).
- Format: `Penyedia. (Tahun). *Judul*. URL`. Judul dicetak miring. Nama penyedia tanpa kurung siku.
- Setiap entri wajib punya tahun (Medium) dan URL (High).
- URL di referensi menjadi hyperlink otomatis di dokumen Word.
- Sumber kredibel: docs resmi, blog vendor besar (Google, IBM, Microsoft, AWS, NVIDIA), paper (arXiv, Nature), laporan riset (Gartner). Hindari Wikipedia sebagai sumber utama, blog anonim, dan agregator.
- Utamakan sumber dari 3 tahun terakhir (dihitung dari tahun berjalan). Sumber lebih lama hanya boleh untuk konsep dasar, sejarah, atau asal-usul.
- Untuk docs resmi, gunakan halaman yang mengacu versi terbaru. Jika hanya ada sumber lama untuk klaim penting, catat di laporan ke user.
- URL harus sudah diverifikasi (bisa dibuka) sebelum dimasukkan.

## 11. Angka dan klaim

- Setiap angka riset atau ukuran wajib punya sumber di Referensi (Medium jika tidak).
- Jika menyebut temuan, sebut pemiliknya secara natural, misalnya "tim di vLLM" atau "peneliti dari Universitas X".
- Sitasi formal seperti `(Nama dkk., 2023)` hanya boleh jika sumbernya ada di Referensi.
- Tahun publikasi harus sesuai dengan sumbernya. Jangan menebak tahun.
- Setiap angka (persentase, ukuran, waktu, jumlah) wajib tercatat di buku klaim (`klaim.md`) dengan status Terverifikasi. Validator memeriksanya jika diberi `--klaim` (Medium jika tidak).
- Klaim yang tidak ditemukan di sumber setelah dicek dengan web_fetch mode full berstatus Belum. Klaim Belum dihapus dari draft, atau diubah jadi pernyataan umum tanpa angka.
- Kata absolut seperti mewajibkan, menjamin, terbukti, sempurna, pasti, dan 100% diperiksa validator sebagai Low. Pakai hanya jika sumber memang mengatakannya sekuat itu, kalau tidak perhalus.
- Pencarian frasa yang gagal di mode selective belum berarti klaim salah. Cek ulang di mode full sebelum mengubah status.

## 12. Pemilihan topik

- Teknologi emerging atau trending (kira-kira 2023 ke atas). Klaster: AI dan LLM, Blockchain dan Web3, security modern, cloud dan infrastruktur, developer tooling dan web platform.
- Satu artikel satu teknologi atau konsep.
- Cek duplikat sebelum menulis (lihat langkah 2 di SKILL.md).
- Harus relevan praktis: pembaca bisa mempelajari atau memakainya sekarang.

## 13. SDG

- Opsional. Hanya dibahas jika user memintanya, dalam 1 sampai 2 kalimat di kesimpulan.
- Jika tidak diminta, jangan dipaksakan.

## 14. Checklist sebelum diajukan

- [ ] Judul sama persis dengan judul yang dipilih, dan maksimal 10 kata.
- [ ] Total kata 500 sampai 800, target 600 sampai 700.
- [ ] Minimal 3 subjudul, satu memuat keyword utama.
- [ ] Figure 1 ada, penomoran berurutan, caption `Figure N.` dengan sumber `(URL)` atau `(AI Generated)` di baris berikutnya.
- [ ] Setiap figure disebut di paragraf teks (misalnya "pada figure 1 berikut").
- [ ] Tabel satu atau lebih, atau sudah dipertimbangkan.
- [ ] Byline satu baris: `Penulis: Nama, Gelar – Jabatan`.
- [ ] 3 sampai 7 referensi, satu per baris, masing-masing punya tahun dan URL.
- [ ] Setiap paragraf prosa minimal 5 kalimat.
- [ ] Buku klaim ada, setiap angka berstatus Terverifikasi, dan sumbernya ada di Referensi.
- [ ] Tidak ada typo atau spasi yang hilang (misalnya "eksekusi(https").
- [ ] Topik belum pernah ditulis di situs.
- [ ] `.docx` sudah dibuat dengan `build_docx.py` dan dibuka untuk dicek.

## 15. Format dokumen Word

Dokumen dibuat oleh `scripts/build_docx.py` dan meniru artikel acuan *Agentic Coding*. Satu-satunya perbedaan: kertas dibuat A4 (acuan memakai US Letter).

- Kertas A4. Margin 2,54 cm di semua sisi. Header dan footer 1,27 cm.
- Font Times New Roman 12 pt, warna hitam. Spasi baris 1,5. Bahasa Indonesia (en-ID).
- Semua paragraf memakai spasi otomatis (`beforeAutospacing` dan `afterAutospacing`), dengan nilai 5 pt sebelum dan sesudah. Spasi default sesudah paragraf 8 pt.
- Judul: tengah, tebal, spasi baris 1,5 saja.
- Isi: rata kiri-kanan, indent baris pertama 1,27 cm. Tidak diindent jika paragraf diakhiri `:` atau tepat setelah daftar. Aturan ini diambil dari perilaku artikel acuan.
- Subjudul: tebal, rata kiri-kanan, tanpa indent.
- Daftar: bullet dengan simbol Symbol, atau bernomor `1.`. Indent kiri 1,27 cm, menggantung 0,63 cm. Setiap daftar bernomor mulai dari 1.
- Gambar: tengah. Lebar default 14,3 cm.
- Caption: tengah, 11 pt. Sumber `(URL)` di bawahnya: tengah, 12 pt, URL menjadi hyperlink.
- Tabel: gaya Grid Table Light (garis abu-abu BFBFBF), lebar otomatis, baris pertama tebal.
- Referensi: heading tebal, entri rata kiri-kanan, judul miring, URL menjadi hyperlink dengan gaya Hyperlink (biru, garis bawah).
- Byline: satu baris tebal, rata kiri-kanan.

Catatan tentang artikel acuan (file *Agentic Coding* di folder `submitted`): isinya dobel, karena subjudul dan referensi muncul dua kali. Jangan memakainya sebagai acuan isi, hanya sebagai acuan format. Caption Figure 1-nya juga berbeda dari Figure 2 (ukuran dan spasi), dan itu tidak diikuti oleh builder.
