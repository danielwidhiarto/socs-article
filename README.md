# socs-article

Repo untuk menulis artikel teknologi untuk website SOCS BINUS: https://socs.binus.ac.id/category/article/

## Isi repo

- `skills/socs-article-writer/`: skill untuk AI agent. Agent membantu menentukan topik, riset dan verifikasi sumber, menulis draft, dan memvalidasi draft terhadap aturan artikel.
- `published/` dan `submitted/`: arsip artikel pribadi. Folder ini di-ignore dan tidak ikut di repo.
- `drafts/`: tempat draft yang dibuat agent. Folder ini juga di-ignore.

## Memasang skill

Clone repo ini, lalu salin folder `skills/socs-article-writer` ke folder skills agent yang dipakai:

- Kiro: `.kiro/skills/` di workspace, atau `~/.kiro/skills/` untuk semua workspace.
- Agent lain: cek lokasi skills di dokumentasi agent tersebut.

Skill mengikuti format Agent Skills (`SKILL.md` dengan `name` dan `description`), jadi bisa dibaca banyak agent.

## Cara pakai

Setelah skill terpasang, minta agent menulis artikel SOCS. Agent akan menanyakan topik, nama penulis, gelar, dan jabatan sebelum mulai menulis.

Untuk memvalidasi draft secara manual (butuh Python 3, tanpa library tambahan):

```
python skills/socs-article-writer/scripts/validate_article.py "drafts/<judul>.md" --keywords "kata1,kata2"
```

## Aturan artikel

Aturan lengkap ada di `skills/socs-article-writer/references/aturan.md`. Contoh artikel yang sudah terbit ada di `skills/socs-article-writer/references/pola-artikel-terbit.md`.
