# Gaya Menulis Anti-Slop

Adaptasi gabungan dua skill: [stop-slop](https://github.com/hardikpandya/stop-slop) (prosa) dan [anti-slop](https://github.com/miqdadbadjuber/anti-slop) (copywriting), keduanya lisensi MIT. Lihat `sumber-gaya.md` untuk atribusi.

Fungsi: filter saat menulis dan saat merevisi draft. Bukan daftar larangan buta — setiap pola di bawah ditolak karena menandakan teks hasil template AI, bukan tulisan yang disusun. Aturan format (panjang, struktur, figure, referensi) tetap di `aturan.md`; file ini khusus soal gaya kalimat.

## 1. Pola kalimat yang dihindari

### Kontras biner
Pola "bukan X, melainkan Y" yang dibuat-buat. Sebut Y langsung.

| Hindari | Tulis |
|---|---|
| Bukan sekadar X, melainkan Y | Y. (tulis langsung) |
| Masalahnya bukan X, tapi Y | Masalahnya adalah Y |
| Bukan X. Bukan Y. Melainkan Z. | Z. (langsung, tanpa drama) |

Pengecualian: kontras biner boleh dipakai kalau memang ada dua hal nyata yang dibandingkan (misalnya kelebihan vs keterbatasan), bukan sekadar gimmick retoris.

### Daftar negatif
Mendefinisikan sesuatu lewat "bukan ini, bukan itu" sebelum menyebut apa dia. Sebut langsung definisinya.

### Fragmen dramatis
Fragmen untuk efek: "Satu kata: kepercayaan." atau kalimat pendek beruntun "X. Dan Y. Dan Z." Gunakan kalimat lengkap. Konten yang meyakinkan, bukan presentasi.

### Setup retoris
- "Bagaimana jika ...?" sebagai pembuka gagasan (bedakan dengan hook "Pernahkah kamu ...?" yang sah di `aturan.md` bagian 3).
- "Pertimbangkan ini:"
- "Dan itu tidak masalah."

Buat poinnya langsung. Pembaca menyimpulkan sendiri.

### Agency palsu
Benda mati jangan diberi peran manusia. Sebut pelakunya.

| Hindari | Tulis |
|---|---|
| Data memberi tahu kita | Peneliti membaca data dan menyimpulkan |
| Pasar memberi reward | Pembeli membayar untuk hal itu |
| Keputusan muncul dari diskusi | Tim memutuskan setelah berdiskusi |
| Tren bergeser | Pengembang beralih ke ... |

### Narator dari kejauhan
Kalimat mengambang tanpa pelaku: "Tak ada yang merancang sistem ini." atau "Orang-orang cenderung ...". Tarik pembaca masuk: pakai "kamu"/"kita" (memang sudah diwajibkan `aturan.md` bagian 8).

### Passive voice
Kalimat pasif menyembunyikan pelaku. Cari pelakunya, jadikan subjek. Bahasa Indonesia: hindari "dilakukan", "dibuat", "diputuskan" tanpa yang melakukannya.

### Pembuka Wh- dan "Jadi"
Jangan mulai kalimat dengan kata tanya (Apa, Kapan, Mengapa, Bagaimana) kecuali pertanyaan retoris yang disengaja. Jangan mulai paragraf dengan "Jadi". Mulai dari subjek atau verba.

## 2. Frasa yang dihapus

### Throat-clearing (pembuka basa-basi)
"Sebenarnya,", "Yang jelas,", "Tak dapat dipungkiri bahwa", "Perlu diketahui bahwa", "Mari kita bahas", "Berikut penjelasannya". Hapus, langsung ke inti.

### Crutch penekanan kosong
"Inilah mengapa hal ini penting.", "Jangan salah", "Coba renungkan.", "Titik."

### Adverb dan pewatas kosong
Hapus: sangat, benar-benar, secara harfiah, jujur saja, sebenarnya, sungguh, mendasar, secara signifikan, menariknya, penting untuk dicatat.

Juga: "pada intinya", "di era digital ini", "seiring berkembangnya zaman", "ketika berbicara tentang".

### Meta-komentar
Teks tidak menceritakan strukturnya sendiri: "Di bagian ini, kita akan ...", "Seperti yang akan kita lihat", "Tapi itu bahasan lain". Hapus; biarkan artikel bergerak.

### Declaratif kosong
Kalimat yang mengumumkan kepentingan tanpa menyebut spesifiknya: "Dampaknya sangat besar.", "Alasannya struktural.", "Taruhannya tinggi.". Ganti dengan hal spesifik yang dimaksud.

## 3. Aturan ritme dan kalimat

- Campur panjang kalimat. Tiga kalimat beruntun dengan panjang mirip: patahkan salah satunya.
- Dua item lebih baik daripada tiga; hindari daftar tiga-item sebagai kebiasaan.
- Akhir paragraf jangan selalu kalimat "punchline". Variasikan.
- Tanpa em dash (—). Pakai koma, titik, atau tanda kurung. (Konsisten dengan `aturan.md` bagian 8 dan validator.)
- Tanpa staccato: jangan menumpuk kalimat pendek untuk drama.
- Lazy extremes (semua, setiap, selalu, tidak pernah, semua orang): klaim melang. Pakai spesifik. Konsisten dengan aturan kata absolut di `aturan.md` bagian 11.
- Pertanyaan retoris boleh, tapi jangan langsung dijawab di kalimat berikutnya dengan formula; biarkan menggantung sebentar atau jawab dengan kalimat berbeda strukturnya.

## 4. Kejujuran konten (dari anti-slop)

Bagian ini untuk jaga-jaga saat menyarankan visual, contoh, atau angka:

- Jangan menampilkan statistik atau testimonial yang tidak bisa diverifikasi. Konsisten dengan buku klaim (`aturan.md` bagian 11).
- Jangan menulis klaim kepatuhan ("enterprise-grade", "SOC 2") tanpa bukti di sumber.
- Setiap istilah teknis dijelaskan sekali, spesifik, bukan generik. Konsisten dengan `aturan.md` bagian 4.
- Fokus pada dampak dan insight, bukan jargon yang menumpuk. Konsisten dengan `aturan.md` bagian 4.

## 5. Skoring revisi (opsional, untuk self-check)

Sebelum draft diserahkan, nilai 1-10 tiap dimensi:

| Dimensi | Pertanyaan |
|---|---|
| Lugas | Kalimat langsung menyatakan, atau mengumumkan? |
| Ritme | Panjang kalimat bervariasi, atau metronomis? |
| Kepercayaan | Menghormati kecerdasan pembaca, atau terlalu banyak menggenggam? |
| Otentik | Terdengar seperti manusia, atau template? |
| Padat | Ada yang bisa dipangkas? |

Total di bawah 35/50: revisi sebelum validasi. Ini alat bantu penulis, bukan langkah wajib dan tidak diperiksa validator.

## 6. Quick check sebelum validasi

- Ada pembuka basa-basi? Hapus, langsung ke inti.
- Ada "bukan X, melainkan Y" yang hanya gimmick? Tulis Y langsung.
- Ada benda mati melakukan aksi manusia? Sebut pelakunya.
- Ada kalimat pasif tanpa pelaku jelas? Ubah jadi aktif.
- Ada adverb/pewatas kosong? Hapus.
- Ada declaratif kosong ("dampaknya besar")? Sebut spesifiknya.
- Ada em dash? Ganti koma/titik/kurung.
- Ada daftar tiga-item sebagai kebiasaan? Kurangi jadi dua, atau beri alasan.
- Paragraf beruntun diawali kata yang sama? Sudah Medium di `aturan.md` bagian 4; hindari juga pola awal yang mirip.
- Kesimpulan berakhir dengan one-liner bombastis? Variasikan; `aturan.md` bagian 4 sudah melarang bombastis.
