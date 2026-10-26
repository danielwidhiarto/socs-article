# Aturan Artikel SOCS BINUS

Ini satu-satunya sumber aturan untuk skill ini. Contoh artikel terbit ada di `pola-artikel-terbit.md` dan hanya perlu dibaca saat butuh contoh.

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
- Nama file: judul tanpa `:` dan tanpa `_`, ganti dengan spasi. Contoh: `Smart Contract Kode yang Bisa Berjanji.md`.

## 3. Hook pembuka

- Mulai dari adegan, masalah sehari-hari, atau fenomena konkret.
- Pola yang sah: "Bayangkan ...", "Pernahkah kamu/kita ...?", "Banyak orang ...".
- Dilarang: definisi langsung di kalimat pertama (Medium).

## 4. Struktur

Urutan wajib:

1. Judul, lalu Figure 1 tepat di bawahnya.
2. Hook (1 sampai 2 paragraf).
3. Apa itu X: definisi dan asal-usul singkat (siapa dan tahun).
4. Cara kerja atau fitur: bullet 4 sampai 6 poin, format `istilah - penjelasan`.
5. Contoh penggunaan nyata: 3 sampai 4 skenario.
6. Tabel (lihat bagian 7).
7. Kelebihan dan keterbatasan, atau tantangan. Jujur dan spesifik, 2 sampai 4 poin.
8. Kesimpulan: 2 sampai 4 kalimat. Satu pemikiran ke depan, satu kalimat yang kembali ke dunia nyata. Tanpa kalimat bombastis.
9. Byline `Penulis:`.
10. Referensi.

Aturan tambahan:
- Paragraf 3 sampai 5 kalimat sebagai saran (Low).
- Dua paragraf berurutan tidak boleh diawali kata yang sama (Medium).
- Istilah teknis dijelaskan sekali. Penjelasan dalam kurung maksimal 7 kata, dan maksimal satu per paragraf (Low).
- Fokus pada dampak dan insight, bukan syntax atau konfigurasi.

## 5. Subjudul

- Minimal 3 subjudul (High jika kurang). Di Markdown pakai `##` atau `###`.
- Di dokumen Word, subjudul boleh berupa paragraf tebal pendek. Keduanya dihitung sama.
- Satu subjudul H2 wajib memuat keyword utama.

## 6. Figure

- Figure 1 wajib (Medium jika tidak ada).
- Total 2 sampai 4 figure, dianjurkan (Low di luar itu).
- Format caption, satu baris:

```
Figure N. Deskripsi singkat gambar (URL sumber)
```

- Penomoran berurutan mulai dari 1 tanpa lompatan (Medium).
- URL sumber wajib. URL hanya boleh dari sumber yang sudah diverifikasi, tidak boleh karangan (High).
- Gambar AI-generated boleh, dengan `(AI Generated)` sebagai pengganti URL. Caption tetap satu baris.
- Minimal satu figure harus dari sumber kredibel, bukan AI-generated.

## 7. Tabel

- Satu tabel dianjurkan (Low jika tidak ada). Bukan wajib.
- Untuk topik perbandingan, pakai format `Aspek | A | B` dengan 5 sampai 7 aspek.
- Caption tabel tidak diatur. Jangan pakai `Table N.` (Low).

## 8. Gaya dan bahasa

- Bahasa Indonesia ragam populer-ilmiah: santai tapi kredibel. Bukan bahasa skripsi, bukan slang.
- Istilah teknis tetap Inggris, misalnya cloud, framework, deploy, open source, pipeline.
- Pakai "kamu" dan "kita". Jangan pakai "Anda" (Low).
- Boleh analogi sehari-hari dan pertanyaan retoris.
- Tanpa blok kode. Artikel ini explainer, bukan tutorial (Low).
- Target pembaca: mahasiswa Informatika dan developer pemula.

## 9. Byline

- Format satu baris: `Penulis: [Nama], [Gelar] – [Jabatan]`. Pakai en dash `–`.
- Nama, gelar, dan jabatan diambil dari input user. Agent wajib menanyakannya, jangan mengisi dari memori atau dari contoh.
- Blok ini wajib ada di bagian penutup (Medium jika tidak ada atau formatnya salah).

## 10. Referensi

- Heading `Referensi` berdiri sendiri. Entri mulai di baris berikutnya.
- Jumlah 3 sampai 7 (High jika kurang dari 3, Medium jika lebih dari 7). Ideal 3 sampai 5.
- Satu entri per baris. Entri yang menempel dalam satu baris (Medium).
- Format: `Penyedia. (Tahun). Judul. URL`. Nama penyedia tanpa kurung siku.
- Setiap entri wajib punya tahun (Medium) dan URL (High).
- Sumber kredibel: docs resmi, blog vendor besar (Google, IBM, Microsoft, AWS, NVIDIA), paper (arXiv, Nature), laporan riset (Gartner). Hindari Wikipedia sebagai sumber utama, blog anonim, dan agregator.
- URL harus sudah diverifikasi (bisa dibuka) sebelum dimasukkan.

## 11. Angka dan klaim

- Setiap angka riset atau ukuran wajib punya sumber di Referensi (Medium jika tidak).
- Jika menyebut temuan, sebut pemiliknya secara natural, misalnya "tim di vLLM" atau "peneliti dari Universitas X".
- Sitasi formal seperti `(Nama dkk., 2023)` hanya boleh jika sumbernya ada di Referensi.
- Tahun publikasi harus sesuai dengan sumbernya. Jangan menebak tahun.

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
- [ ] Minimal 3 subjudul, satu H2 memuat keyword utama.
- [ ] Figure 1 ada, penomoran berurutan, setiap caption punya URL atau `(AI Generated)`.
- [ ] Tabel satu atau lebih, atau sudah dipertimbangkan.
- [ ] Byline satu baris dengan format yang benar.
- [ ] 3 sampai 7 referensi, satu per baris, masing-masing punya tahun dan URL.
- [ ] Setiap angka punya sumber di Referensi.
- [ ] Tidak ada typo atau spasi yang hilang (misalnya "eksekusi(https").
- [ ] Topik belum pernah ditulis di situs.
