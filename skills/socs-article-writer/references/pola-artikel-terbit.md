# Pola Artikel yang Sudah Terbit

Hasil ekstraksi 37 artikel `published/` dari file .docx. Dipakai sebagai contoh bentuk, bukan isi.

## Angka

- Panjang prosa: minimum 552, maksimum 828, median sekitar 643 kata.
- Tabel: 25 dari 37 artikel punya minimal satu tabel. Artikel "vs" sering punya dua tabel (perbandingan, lalu kelebihan dan kekurangan), tapi tidak selalu.
- Gambar: 2 file gambar paling umum (30 artikel). 3 file: 5 artikel. 4 file: 1 artikel. Satu artikel hanya punya 1.
- Caption: `Figure N.` 59 kali, `Figure N:` 10 kali. Format dengan titik dipakai mayoritas.
- Byline: variasi tidak seragam. Format paling banyak `Penulis:Nama, S.Kom - FDP Scholar` (tanpa spasi, strip biasa). Format baru `Penulis: Nama, S.Kom, M.Kom - FDP Scholar` muncul di artikel-artikel terbaru. Skill memakai format kanonik dari `aturan.md`.

## Hook pembuka

Pembuka yang paling sering dipakai:

- "Bayangkan ..." (paling dominan)
- "Pernahkah kamu/kita/Anda ...?"
- Fenomena konkret, misalnya "Dulu, layar hitam dengan teks hijau..." atau "Di balik setiap pencarian Google..."

## Struktur umum

Hampir semua artikel mengikuti pola ini:

1. Judul (bold di dokumen, `#` atau `##` di markdown), lalu Figure 1.
2. Hook (1-2 paragraf).
3. Definisi dan asal-usul, sering dengan subjudul "Apa itu ..." atau "Mengenal ...".
4. "Bagaimana ... Bekerja?" atau "Fitur Utama": bullet list.
5. "Contoh di Dunia Nyata" atau "Contoh Penggunaan": 3-4 bullet dengan `Nama - penjelasan`.
6. "Mengapa ... Penting?" atau "Kelebihan dan Keterbatasan".
7. Tantangan atau batasan (sering ada, tidak wajib).
8. Kesimpulan.
9. Byline `Penulis:`.
10. Referensi: 3-5 entri, satu baris per sumber.

## Referensi

- Jumlah umum 4-5 entri.
- Sumber yang sering dipakai: docs resmi (docs.deno.com, kubernetes.io, modelcontextprotocol.io), blog vendor (Google Research, NVIDIA, IBM, Google Cloud), GeeksforGeeks, dan arXiv.
- Kesalahan yang pernah muncul: heading `Referensi` menempel dengan isi, entri tanpa tahun, dan dua sumber dalam satu baris. Validator memeriksa ketiganya.

## Yang perlu dihindari (ditemukan di artikel lama)

- Tanpa spasi setelah `Penulis:`.
- Caption tanpa URL, misalnya `(Sumber: Dokumentasi Penulis)`.
- Figure yang lompat nomor (1 lalu 3).
- Kata pembuka paragraf berurutan yang sama.
- Referensi yang dicampur dengan heading.
