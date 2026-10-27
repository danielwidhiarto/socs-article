# Target Bekasi (BINUS @Bekasi, Computer Science – Software Engineering)

Override untuk `references/aturan.md` saat menulis artikel kategori
[Computer Science – Software Engineering](https://binus.ac.id/bekasi/category/article/computer-science-software-engineering/).
Aktifkan dengan `--target bekasi` di `scripts/validate_article.py` dan mulai dari
`assets/template-bekasi.md`. Tanpa flag itu, aturan SOCS berlaku apa adanya.

Disusun dari 9 artikel Bekasi (Juni 2024–Juni 2026, dibaca 27 Okt 2026):
Empati AI, Edge Computing, Deploy Jumat, Green Software, Spatial Computing,
Lima Metrik Defect, Serverless, Pasukan Agen AI, Pemrograman Kuantum.

## Ringkasan perbedaan

| Aspek | SOCS (`socs.binus.ac.id`) | Bekasi (`binus.ac.id/bekasi`) |
|---|---|---|
| Sapaan | `kamu/kita`, `Anda` = Low | `Anda` default (mayoritas sampel); `kamu` juga lolos (artikel Kuantum). Validator tidak mengecek |
| Pembuka | Hook adegan/fenomena | Sama, boleh didahului sapaan `Hai, Software Engineers!` |
| Figure | `Figure N.` + baris `(URL)` terpisah, 2–4 gambar | `Gambar 1. Deskripsi (sumber: URL)` satu baris; 1 gambar lazim (8 dari 9 sampel); sumber boleh `(sumber: URL)` |
| Sebutan figure di badan | Wajib (Low jika tidak) | Tidak wajib, tidak dicek |
| Tabel | Dianjurkan | Dianjurkan (sama; 9/9 sampel tanpa tabel) |
| Byline | Wajib `Penulis: Nama, Gelar – Jabatan` | Tidak ada (9/9 sampel tanpa byline; author = `editorarticle`). Penulis tidak perlu ditanya |
| Referensi | Format ketat, 3–7, tahun wajib | Bebas: bare URL, numbered, atau link judul; 3–8; tahun opsional |
| Subjudul | Min 3 (`##`/`###`), High jika kurang | Min 2 (boleh `#`/`##`/`###` atau paragraf ber-pemimpin bold `**...**`), Medium jika kurang |
| Paragraf | Min 5 kalimat | Min 3 kalimat (Medium jika kurang) |
| Judul | Maks 10 kata / 70 karakter (Medium) | Maks 15 kata / 110 karakter (Low); bentuk bebas, pertanyaan sah |
| Struktur | Urutan 10 langkah wajib | Esai opini bebas; pola umum: judul → gambar → hook → 2–6 subjudul → referensi |
| Kata absolut, em dash, anti-slop | Sama | Sama |

## Bukti per artikel

| Artikel | Sapaan | Figure | Referensi | Subjudul | Catatan |
|---|---|---|---|---|---|
| Empati AI | Anda | 1, tanpa caption | 8 bare URL | ~7 (`#`) | Greeting `Hai, Software Engineers!` |
| Edge devices | Anda | 1, tanpa caption | 8 bare URL | 4 (`#`) | Greeting sama |
| Deploy Jumat | impersonal | 1 + `Gambar 2.` tanpa gambar (caption yatim) | 8 numbered formal | 5 (`#`) | Hook `Bayangkan ...` |
| Green software | kita | 1 + caption inline `(sumber: pexels)` | 3 bare URL | 3 (`#` bernomor) | Tanpa greeting |
| Spatial computing | Anda | 1, tanpa caption | 5 bare URL | 3 (`#`) | Fokus karir, sudut pandang cocok untuk topik profesi |
| Lima Metrik Defect | impersonal | 6 (`Gambar 1–6`, rumus tanpa sumber) | 8 link judul | 6 (`##` bernomor) | Satu-satunya multi-figure; jadi preseden batas atas figure |
| Serverless | impersonal | 1 caption inline `(sumber: ...)` | 5 link judul | 2 (`#`) | Preseden batas bawah subjudul |
| Pasukan Agen AI | Anda | 1, tanpa caption | 7 bare URL | 0 heading, 2 bold-lead | Preseden subjudul bold-lead; ada angka % |
| Kuantum | kamu | 1, tanpa caption | 6 bare URL | 5 (`#`) | Preseden sapaan `kamu`; ada angka Rp/$ |

## Aturan figure Bekasi (yang divalidasi)

- `Gambar 1` wajib (Medium jika tidak ada). `Figure N.` tetap diterima.
- Caption boleh satu baris dengan sumber inline: `Gambar 1. Deskripsi (sumber: https://...)`.
- Tanpa sumber inline, baris berikutnya harus `(URL)` atau `(sumber: URL)` (Low jika tidak ada, bukan Medium).
- Penomoran dari 1 dan berurutan (Medium jika tidak).
- Lebih dari 6 figure: Low. Satu figure tidak ditegur.

## Aturan referensi Bekasi (yang divalidasi)

- Heading diterima: `Referensi`, `References`, `Daftar Referensi`, `Daftar Pustaka` (tanpa teguran varian).
- Entri boleh bare URL (`<https://...>`), numbered (`1. ...`), bullet, atau link judul — satu entri per baris, tiap entri wajib memuat URL (High jika tidak).
- Tahun opsional, tidak dicek. Maksimal 8 entri (Low jika lebih); minimal 3 (High jika kurang).
- URL tetap wajib diverifikasi bisa dibuka dan dicatat di buku klaim seperti SOCS.

## Yang tetap sama dari SOCS

Panjang 500–800 kata, hook adegan/fenomena, buku klaim untuk angka,
larangan em dash, gaya anti-slop, tanpa placeholder, keyword wajib muncul
(keyword utama di salah satu subjudul, level heading bebas).
