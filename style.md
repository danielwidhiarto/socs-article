# Style Guide — Artikel SOCS BINUS

Diturunkan dari audit 20 artikel contoh di folder ini (2026-10-24): median ±600 kata (rentang 519–763, gaya hitung Word: semua teks termasuk tabel, dihitung sekali), 2–3 gambar per artikel (rata-rata 2.2, total 44), median 4 referensi (rentang 1–7), 14/20 artikel memakai tabel.
Pakai file ini sebagai konteks saat generate artikel baru. Statistik lama (39 artikel, median 649 kata) tidak lagi jadi acuan — angka dari 20 artikel inilah yang berlaku.

---

## 1. Bahasa & Tone

- **Bahasa Indonesia** ragam populer-ilmiah: santai tapi kredibel. Bukan bahasa skripsi, bukan slang.
- **Istilah teknis tetap Inggris**, jangan diterjemahkan: *cloud, framework, fine-tuning, deploy, open source, pipeline*.
- Pakai "kita" dan pertanyaan retoris. Boleh analogi sehari-hari.
- Target pembaca: mahasiswa Informatika & developer pemula Indonesia.
- Tanpa blok kode panjang — ini explainer, bukan tutorial. Maksimal potongan kecil jika benar-benar perlu.

## 2. Judul

- Format wajib: **`Nama Teknologi: Tagline`** (20/20 artikel di folder ini).
- Tagline = manfaat/kontras menarik, bukan deskripsi generik:
  - ✅ `Smart Contract: Kode yang Bisa Berjanji`
  - ✅ `Chaos Engineering: Sengaja Merusak Sistem Agar Lebih Tangguh`
  - ✅ `Speech Synthesis dan Voice Cloning: Ketika Suara Jadi Produk Digital`
  - ❌ `Pengenalan Smart Contract`
- Sub-genre "vs": `A vs B: Pertanyaan Provokatif` — contoh: `Deno vs Node.js: Siapa Raja Baru Dunia JavaScript?`
- Catatan: 6/20 judul existing kehilangan tanda `:` di judul dokumen (efek ekspor/publish). Artikel baru: `:` **wajib tetap ada** di judul; dihapus hanya di nama file (§10).

## 3. Panjang

- **Umumnya 500–800 kata. Target ideal ±650** (median korpus: 593, rata-rata 607, terpanjang 763 — Blockchain Trilemma).
- Hitung kata gaya Word: semua teks termasuk isi tabel, tiap teks dihitung sekali.
- Hard cap ±800. Materi lebih berat → pecah jadi artikel terpisah.

## 4. Struktur (alur wajib)

1. **Judul** (+ Figure 1 di dekatnya)
2. **Hook** — masalah sehari-hari yang relatable buat mahasiswa/developer, bukan definisi langsung. Pola pembuka yang terbukti (15/20 artikel):
   - **"Bayangkan ..."** (11/20): *"Bayangkan kamu membangun sebuah kota digital..."*
   - **"Pernahkah kamu/Anda ...?"** (3/20): *"Pernahkah kita bertanya: bagaimana keyboard smartphone bisa semakin akurat..."*
   - **"Banyak orang yang belajar coding pasti pernah mengalami hal serupa: ..."** (1/20)
3. **Apa itu X** — definisi + asal-usul/sejarah singkat (siapa, tahun, dari mana)
4. **Fitur / Cara kerja** — bullet list 4–6 poin, tiap poin `istilah – penjelasan`
5. **Contoh penggunaan di dunia nyata** — 3–4 skenario konkret (kerja tim, magang, portofolio, industri)
6. **Tabel** — minimal 1 tabel (perbandingan `Aspek | X | Y` jika topik "vs", atau tabel ringkasan; lihat §6)
7. **Kelebihan & keterbatasan** — jujur, 2–4 poin masing-masing
8. **Kesimpulan** — 2–4 kalimat + opsional 1 kalimat kaitan SDG
9. **Penulis** — byline
10. **Referensi**

Heading section di file existing mayoritas **paragraf tebal sendiri** — bukan Word Heading style (hanya Firebase Studio yang pakai Heading 3). Di CMS/output tetap render sebagai Heading 2/3. Contoh penamaan existing: *Apa itu Firebase Studio*, *Fitur Utama*, *Contoh Penggunaan di Dunia Nyata*, *Kelebihan dibanding IDE Konvensional*, *Keterbatasan yang perlu diketahui*, *Kesimpulan*, *Referensi*. Nama heading bebas asal alur sama; varian umum di korpus: *Tantangan dan Batasan*, *Mengapa X Penting*, *Bagaimana X Bekerja*.

## 5. Gambar

- **2–4 gambar per artikel** (korpus: 2–3, rata-rata 2.2; lebih dari 1 **wajib**, paling umum tepat 2).
- **Figure 1 selalu di dekat judul/hook** (20/20 korpus meletakkannya sebelum paragraf pembuka); Figure 2+ menyusul di bagian teknis (arsitektur, cara kerja).
- Caption wajib format: `Figure N. <deskripsi singkat> (URL sumber)` — pakai titik setelah angka (bukan `:`), URL dalam kurung di akhir. Contoh korpus: `Figure 2. Alur kerja smart contract dari identifikasi hingga eksekusi (https://www.geeksforgeeks.org/...)`
- **Penomoran berurutan mulai dari Figure 1, tidak boleh lompat** (jangan mengulang kasus Human-in-the-Loop yang loncat 1→3), tidak boleh tanpa URL.
- Kalau kamu bisa membuat diagram arsitektur/alur sendiri, itu nilai tambah — labeli saja tetap `Figure N.` + cantumkan sumber/deskripsi.
- Prioritas sumber: website resmi produk, docs resmi, blog vendor besar. Boleh AI-generated untuk ilustrasi konsep (label `AI Generated` seperti di Smart Contract), tapi minimal 1 gambar harus dari sumber kredibel.

## 6. Tabel

- Di korpus, **14/20 artikel pakai tabel** — bukan cuma topik "vs". Pakai tabel untuk dua kebutuhan:
  1. **Perbandingan dua teknologi** (Deno vs Node.js, Serverless vs Traditional, PoW vs PoS): kolom pertama `Aspek`, lalu satu kolom per teknologi. Bandingkan 5–7 aspek, pilih dari: instalasi, biaya, kecepatan/performance, skalabilitas, keamanan, fleksibilitas, kolaborasi, ekosistem/komunitas, kurva belajar, dukungan platform. Isi sel singkat dan padat, bukan paragraf. (Catatan: PoW vs PoS existing justru tanpa tabel — jangan ditiru.)
  2. **Meringkas poin topik non-"vs"** (Guardrails, MCP, RAFT, Sakana Fugu, Human-in-the-Loop, Smart Contract, dll.): misal tabel kelebihan/keterbatasan, jenis/kategori, atau perbandingan "dengan vs tanpa X".
- Satu tabel cukup; dua hanya jika benar-benar menambah (Deno punya 2). Contoh tabel nyata dari korpus → §11.3.

## 7. Byline & SDG

- Byline wajib di akhir. Korpus memakai 3 varian:
  1. `Penulis:Emmanuel Daniel Widhiarto, S.Kom – FDP Scholar` (11/20, satu baris, varian terbanyak)
  2. Tanpa kata "Penulis": `Emmanuel Daniel Widhiarto, S.Kom - FDP Scholar` (8/20; terlihat pada artikel yang dibuat dgn AI)
  3. `Penulis` (baris sendiri) → `Emmanuel Daniel Widhiarto – FDP Scholar` (tanpa gelar; hanya Firebase Studio, jangan ditiru)
- **Format kanonik untuk artikel baru — pilih satu dan konsisten selamanya:**

  ```
  Penulis: Emmanuel Daniel Widhiarto, S.Kom, M.Kom – FDP Scholar
  ```

  (pakai spasi setelah `Penulis:` + gelar `S.Kom, M.Kom`; beda dari semua varian existing yang masih `S.Kom`)
- **JANGAN mengubah/diseragamkan byline artikel lama** (`[PUBLISHED]`) yang masih `S.Kom` — terbit sebelum lulus S2. Aturan `S.Kom, M.Kom` hanya untuk artikel baru.
- Pemisah strip: korpus campur `–` (en dash) dan `-`; pakai `–`.

- Kaitan SDG: **opsional** (hanya 2/20 artikel existing yang menyebut SDG). Kalau dipakai, 1 kalimat di kesimpulan atau heading sendiri — *"Selain itu, X sejalan dengan SDG 9 (Industry, Innovation, and Infrastructure) karena ..."*
  - SDG umum dipakai: 9 (Inovasi/Infrastruktur), 4 (Pendidikan), 7 (Energi Bersih — untuk topik green computing), 11 (Kota Berkelanjutan — dipakai artikel Green Computing).

## 8. Referensi

- Section `Referensi` di paling akhir, **2–7 sumber (ideal 3–4)**.
- Gaya APA-ish: `Author/Organisasi. (Tahun). Judul. URL` — organisasi **tanpa kurung siku** (jangan ulangi pola `[ArXiv]. (2026)` di artikel Sakana Fugu/RAFT/MCP).
- Satu sumber = satu baris, jangan digabung dua sumber dalam satu baris.
- Jangan menempel daftar referensi ke heading-nya — kasus Deno: `ReferensiDahl, R. (2018)...` jadi satu paragraf. Heading `Referensi` harus paragraf sendiri, entri mulai baris berikutnya.
- Contoh nyata referensi yang benar vs salah → §11.
- Referensi harus punya URL dan tahun; jangan ulangi kasus Guardrails yang punya entri tanpa tahun (`GuardrailsAI Docs. https://...`).
- Hanya sumber kredibel:
  - ✅ Docs resmi (kubernetes.io, firebase.studio), blog vendor (Google, IBM, Microsoft, AWS), Nature, arXiv, Gartner, publikasi riset.
  - ❌ Wikipedia sebagai referensi utama, blog anonim, aggregator konten.
- Untuk topik blockchain/crypto, boleh tambah 1 sumber edukasi lokal kredibel (Pintu Academy, Coinvestasi).

## 9. Pemilihan Topik

- Harus **teknologi emerging/trending** (kisaran 2023–sekarang) dari salah satu klaster:
  - AI/LLM ecosystem (RAG, agent, MCP, guardrails, fine-tuning, federated learning, ...)
  - Blockchain & Web3
  - Security modern (zero trust, encryption, DID)
  - Cloud & infrastruktur (serverless, container, IaC, data center, green computing)
  - Developer tooling & web platform (PWA, WebAssembly, IDE, CLI, framework baru)
- Satu artikel = **satu teknologi/konsep**. Jangan campur dua topik.
- Sudah ditulis (jangan duplikat): lihat daftar artikel `[PUBLISHED]` di folder ini (20 artikel per 2026-10-24).
- Harus relevan praktis: pembaca bisa mempelajari/memakainya sekarang.

## 10. Nama File

- Draft: `Judul Artikel.docx`
- Setelah tayang: `[PUBLISHED] Judul Artikel.docx`
- Nama file = judul artikel, tanpa tanda `:` (ganti dengan spasi), boleh pakai `_` untuk `:` di judul berformat `X: Y`.

---

## 11. Contoh Konkret (copas dari artikel existing)

Bagian ini contoh nyata dari korpus — jadikan acuan bentuk, jangan ditulis ulang isinya.

### 11.1 Hook pembuka yang benar

- **"Bayangkan ..."** (paling umum, 11/20) — Green Computing:
  > *"Bayangkan sebuah pagi di kota modern: gedung-gedung berdiri, mobil listrik melintas, dan semua sistem berjalan tanpa kita sadari memakan energi dalam jumlah besar..."*
- **"Pernahkah kamu ...?"** — Federated Learning:
  > *"Pernahkah kita bertanya: bagaimana keyboard smartphone bisa semakin akurat menebak kata yang kita ketik, padahal data kita tidak pernah dikirim ke mana-mana?"*
- **Relatable ke tugas kuliah** — Containerization:
  > *"Bayangkan kamu sedang mengerjakan proyek web untuk tugas akhir. Di laptopmu semuanya berjalan lancar, tapi begitu demo di laptop temanmu, aplikasinya error..."*

### 11.2 Caption gambar yang benar vs salah

✅ **BENAR** (Smart Contract, DID):
```
Figure 1. Ilustrasi konsep smart contract (AI Generated)
Figure 2. Alur kerja smart contract dari identifikasi hingga eksekusi (https://www.geeksforgeeks.org/solidity/smart-contracts-in-blockchain/)
```
❌ **SALAH — jangan ditiru** (kasus nyata di korpus):
```
Figure 1: Model Arsitektur Sakana Fugu            ← pakai ":" bukan "."; tanpa URL
Figure 3: Perbandingan Workflow...                 ← loncat dari 1 ke 3 (Human-in-the-Loop)
Figure 1. Ilustrasi Alur Fine-Tuning Model         ← URL dipisah ke paragraf lain
```

### 11.3 Tabel perbandingan yang benar (dari artikel Deno vs Node.js)

| Aspek | Node.js | Deno |
|---|---|---|
| Tahun Rilis | 2009 | 2018 |
| Bahasa Utama | C++ | Rust |
| Modul | CommonJS (require) | ES Modules (import/export) |
| Manajer Paket | npm | Import langsung via URL |
| Keamanan | Akses sistem terbuka | Permission-based (sandboxed) |
| TypeScript | Perlu konfigurasi tambahan | Didukung secara native |
| Tooling | Terpisah (npm, eslint, nodemon) | Terintegrasi (deno fmt, deno test) |

Catatan bentuk: kolom pertama `Aspek`, isi sel frasa pendek bukan kalimat panjang, 6–8 baris. (Tabel kedua di artikel yang sama memakai pola `Aspek | Node.js | Deno` dengan baris Kelebihan/Kekurangan — itu pola untuk topik tunggal.)

### 11.4 Byline yang benar vs salah

✅ **BENAR** (format kanonik artikel baru):
```
Penulis: Emmanuel Daniel Widhiarto, S.Kom, M.Kom – FDP Scholar
```
❌ **SALAH — jangan ditiru** (varian nyasar di korpus):
```
Penulis:Emmanuel Daniel Widhiarto, S.Kom – FDP Scholar      ← tanpa spasi setelah ":"
Emmanuel Daniel Widhiarto, S.Kom - FDP Scholar              ← tanpa kata "Penulis", strip biasa
Emmanuel Daniel Widhiarto – FDP Scholar                     ← gelar hilang (Firebase)
```

### 11.5 Referensi yang benar vs salah

✅ **BENAR** (Federated Learning):
```
Google Research. (2023). Federated Learning: Collaborative Machine Learning Without Centralized Data. https://research.google/blog/federated-learning-collaborative-machine-learning-without-centralized-training-data/
NVIDIA. (2024). What Is Federated Learning? https://blogs.nvidia.com/blog/what-is-federated-learning/
```
❌ **SALAH — jangan ditiru** (kasus nyata di korpus):
```
[ArXiv]. (2026). TRINITY: An Evolved LLM Coordinator. ...     ← kurung siku pada nama organisasi
GuardrailsAI Docs. https://guardrailsai.com/guardrails/docs   ← tanpa tahun
ReferensiDahl, R. (2018, May 27). ...                          ← daftar nempel ke heading "Referensi"
Coinvestasi. (2024). Proof of Work vs Proof of Stake. https://coinvestasi.com/...TokenMetrics   ← dua sumber nempel satu baris
```

### 11.6 Profil artikel yang memenuhi semua aturan

**Federated Learning Melatih AI Tanpa Mengirim Data ke Cloud** — jadikan template emas:
- 602 kata (gaya Word) ✅ target ±650
- 3 gambar, `Figure 1/2/3. deskripsi (URL)`, urut, semua dari sumber kredibel (Google Research, NVIDIA, GeeksforGeeks) ✅
- Struktur: hook "Pernahkah kita bertanya..." → definisi → "Bagaimana Federated Learning Bekerja?" (bullet) → "Contoh di Dunia Nyata" → penutup ✅
- Byline `Penulis:Emmanuel ... S.Kom – FDP Scholar` (varian lama; untuk artikel baru tambah spasi + `S.Kom, M.Kom`) ✅
- 5 referensi valid satu baris per sumber ✅
- Tanpa tabel (topik tunggal tanpa perbandingan — masih boleh, tapi idealnya tambah 1 tabel ringkasan)

---

## Checklist Sebelum Publish

- [ ] Judul format `Nama Teknologi: Tagline` (`:` tetap ada di judul)
- [ ] 500–800 kata, target ±650 (hitung gaya Word: semua teks sekali)
- [ ] Struktur lengkap: hook ("Bayangkan..." / "Pernahkah...") → apa itu → fitur/cara kerja → use case → kelebihan/keterbatasan → kesimpulan
- [ ] 2–4 gambar, `Figure N. deskripsi (URL)`, penomoran urut mulai Figure 1, Figure 1 di dekat judul
- [ ] Ada minimal 1 tabel (perbandingan `Aspek | X | Y` jika topik "vs"; tabel ringkasan jika topik tunggal)
- [ ] Byline `Penulis: Emmanuel Daniel Widhiarto, S.Kom, M.Kom – FDP Scholar`
- [ ] Referensi 2–7 (ideal 3–4), kredibel, satu baris per sumber, ada tahun + URL
- [ ] Bahasa Indonesia, istilah teknis tetap Inggris
- [ ] Topik belum pernah ditulis
- [ ] Nama file sesuai konvensi

## Template Prompt Generate Artikel Baru

```
Tulis artikel blog Bahasa Indonesia (600–700 kata) untuk website SOCS BINUS
tentang [NAMA TEKNOLOGI].

Konteks: [1-2 kalimat kenapa teknologi ini relevan sekarang].

Ikuti style guide ini:
- Judul: "Nama Teknologi: Tagline menarik" (tanda : wajib ada di judul)
- Struktur: hook relatable (mulai dengan "Bayangkan ..." atau "Pernahkah ...")
  → Apa itu X (definisi+sejarah singkat) → Fitur/cara kerja (bullet 4-6) →
  Contoh penggunaan nyata (3-4) → Kelebihan & keterbatasan → Kesimpulan →
  Penulis: Emmanuel Daniel Widhiarto, S.Kom, M.Kom – FDP Scholar → Referensi
- Sisipkan 2-4 gambar dengan caption "Figure N. deskripsi (URL sumber)".
  Figure 1 di dekat judul/hook, sisanya di bagian teknis. Penomoran urut.
  [jelaskan gambar apa yang dibutuhkan; boleh minta AI buatkan diagram
  arsitektur/alur sendiri]
- Sertakan minimal 1 tabel ringkasan. [Jika topik perbandingan] tabel
  "Aspek | A | B" dengan 6 aspek.
- Heading section sebagai paragraf tebal sendiri (atau Heading 2/3 di CMS).
- Istilah teknis tetap Inggris, tone populer-ilmiah, tanpa blok kode.
- Referensi: 3-4 sumber kredibel (docs resmi / blog vendor / paper),
  format "Author. (Tahun). Judul. URL", tanpa kurung siku, satu baris per sumber.

[Jika topik perbandingan] Tambahkan tabel "Aspek | A | B" dengan 6 aspek.
```
