# Aturan Pembuatan Artikel Articly

Dokumen ini merangkum aturan teknis (panjang, struktur, judul, figure, keyword, referensi, SDG) yang diterapkan pada pembuatan artikel. Aturan gaya penulisan tidak termasuk.

Sumber: `app/lib/prompts.js` dan `app/lib/validate-article.js`.

## 1. Panjang Artikel

Panjang dihitung dalam kata prosa. Judul, caption Figure, blok Penulis, dan Referensi tidak ikut dihitung.

| Aturan | Nilai | Tingkat keparahan jika dilanggar |
|---|---|---|
| Total kata prosa minimum | 500 | High |
| Total kata prosa maksimum | 800 (batas keras) | High |
| Target pembuka (intro) | ~80–120 kata | Target |
| Target isi (body) | ~380–500 kata | Target |
| Target penutup (closing) | ~80–120 kata | Target |

## 2. Judul

- Format: `[Topik]: [Kalimat Provokatif Human-Friendly]`.
- Maksimal 10 kata dan 70 karakter. Melebihi batas: Medium.
- Judul di artikel harus sama persis dengan judul yang dipilih user. Jika tidak sama: High.
- Judul wajib ada di baris pertama artikel. Jika tidak ada: High.

## 3. Struktur

- Minimal 3 subjudul H2/H3. Kurang dari itu: High.
- Pembuka dimulai dari adegan, cerita, atau fenomena konkret, bukan definisi atau pertanyaan.
- Paragraf 3–5 kalimat.
- Dua paragraf berurutan tidak boleh diawali kata yang sama.
- Disarankan ada bagian "Mengapa [topik] penting?" bila relevan.
- Disarankan ada bagian tantangan, trade-off, atau keterbatasan bila relevan.
- Tabel perbandingan atau daftar hanya dipakai bila membantu pemahaman. Tabel memakai format markdown dengan pipe `|`.
- Penutup berisi satu pemikiran ke depan dan satu kalimat yang mengembalikan pembaca ke dunia nyata.
- Penutup tidak boleh berupa kalimat poster atau bombastis.

## 4. Figure

- Figure 1 wajib ada dalam format code block caption. Jika tidak ada: Medium.
- Figure 2 dan Figure 3 sebaiknya ada dan disisipkan merata di isi artikel. Jika tidak ada: Low.
- Format caption:

```
Figure N: [Deskripsi singkat gambar]
(URL gambar)
```

## 5. Keyword

- Setiap keyword yang dipilih user harus muncul di artikel. Jika tidak: Medium.
- Satu subjudul H2 wajib memuat keyword utama.

## 6. Isi dan Konten

- Minimal satu contoh nyata (produk, perusahaan, atau tool yang dikenal).
- Minimal satu angka riset atau ukuran nyata beserta sumbernya.
- Jika menyebut riset atau temuan, sebut pemiliknya secara natural (misalnya "tim di vLLM" atau "peneliti dari Universitas X").
- Sitasi formal seperti "(Nama dkk., 2023)" hanya boleh dipakai bila sumbernya ada di daftar referensi.
- Istilah teknis dijelaskan sekali. Penjelasan dalam kurung maksimal 7 kata dan maksimal satu per paragraf.
- Fokus pada dampak dan insight teknologi, bukan syntax atau konfigurasi.

## 7. Blok Penulis

- Blok `Penulis:` wajib ada di bagian penutup. Jika tidak ada: Medium.
- Format:

```
Penulis:
[Nama] - [Jabatan]
[Departemen]
```

## 8. Referensi

- Minimal 3 entri referensi. Jika kurang: High.
- Setiap sitasi formal di teks harus punya entri di bagian Referensi. Jika tidak: High.
- Format entri: `[Nama Penyedia]. (Tahun). [Judul/deskripsi]. [URL]`.
- URL hanya boleh berasal dari sumber web yang sudah diverifikasi. URL yang tidak valid dihapus otomatis oleh pipeline.
- Dilarang mengarang URL.

## 9. SDG (Sustainable Development Goals)

- SDG bersifat opsional.
- Jika user memilih SDG: topik dikaitkan dengan SDG tersebut dalam 1–2 kalimat.
- Jika user tidak memilih SDG: artikel tidak boleh memaksakan pembahasan SDG.
- Kepatuhan SDG hanya diarahkan lewat prompt dan tidak diperiksa oleh validator otomatis.

## 10. Tingkat Keparahan Validasi

- High: artikel dianggap gagal validasi.
- Medium: perlu diperbaiki, tidak menggagalkan validasi.
- Low: saran perbaikan.
