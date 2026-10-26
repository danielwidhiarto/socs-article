# socs-article

Repo untuk menulis artikel teknologi untuk website SOCS BINUS: https://socs.binus.ac.id/category/article/

## Isi repo

- `skills/socs-article-writer/`: skill untuk AI agent. Agent membantu menentukan topik, riset dan verifikasi sumber, menulis draft, dan memvalidasi draft terhadap aturan artikel.
- `published/` dan `submitted/`: arsip artikel pribadi. Folder ini di-ignore dan tidak ikut di repo.
- `drafts/`: tempat draft yang dibuat agent. Folder ini juga di-ignore.

## Memasang skill

Skill ini mengikuti standar [Agent Skills](https://agentskills.io): satu folder dengan `SKILL.md` (berisi `name` dan `description`), plus `references/`, `scripts/`, dan `assets/`. Standar ini dibaca oleh banyak agent, jadi cukup satu folder untuk semua agent.

Langkah umum:

```
git clone https://github.com/danielwidhiarto/socs-article.git
cd socs-article
```

Lalu salin folder `skills/socs-article-writer` ke lokasi skills agent yang dipakai. Nama folder harus tetap `socs-article-writer`, karena harus sama dengan `name` di `SKILL.md`.

| Agent | Lokasi di workspace (project) | Lokasi global (semua project) | Catatan |
|---|---|---|---|
| Kiro | `.kiro/skills/` | `~/.kiro/skills/` | Cek dengan `/context show`. |
| Claude Code | `.claude/skills/` | `~/.claude/skills/` | Dibaca dari docs resmi. Perubahan di folder ini langsung terdeteksi dalam sesi. |
| Codex (OpenAI CLI) | `.agents/skills/` | `~/.agents/skills/` | Codex juga membaca `~/.codex/skills/` di beberapa panduan lama. Cek dengan `/skills`. |
| Gemini CLI | `.gemini/skills/` atau `.agents/skills/` | `~/.gemini/skills/` atau `~/.agents/skills/` | Lokasi `.agents/skills/` dipakai bersama agent lain. |
| GitHub Copilot CLI | `.github/skills/`, `.claude/skills/`, atau `.agents/skills/` | `~/.copilot/skills/`, `~/.claude/skills/`, atau `~/.agents/skills/` | Lokasi `.claude/skills/` juga dibaca Copilot CLI. |
| Oh My Pi (`omp`) | Belum diverifikasi | `~/.omp/agent/skills/` | Lokasi global dari panduan komunitas. Cek dokumentasi `omp` untuk lokasi project. |
| Pi (`pi`) | `.agents/skills/` atau folder skill Pi | `~/.agents/skills/` | Pi juga membaca standar Agent Skills. |
| Agent lain | Cek dokumentasi agent | Cek dokumentasi agent | Skill tetap bisa dipakai selama agent membaca standar Agent Skills. |

Contoh pemasangan untuk satu project:

- macOS, Linux, atau Git Bash di Windows:

  ```
  mkdir -p .agents/skills
  cp -r skills/socs-article-writer .agents/skills/
  ```

- Windows PowerShell:

  ```
  New-Item -ItemType Directory -Force -Path .agents\skills | Out-Null
  Copy-Item -Recurse skills\socs-article-writer .agents\skills\
  ```

Untuk Claude Code, ganti `.agents/skills` dengan `.claude/skills`. Untuk Kiro, ganti dengan `.kiro/skills`. Untuk pemasangan global, pakai folder home (misalnya `~/.agents/skills`).

Setelah disalin, mulai sesi agent yang baru (atau jalankan reload jika agent mendukungnya), lalu pastikan skill terbaca. Jika tidak terbaca, periksa bahwa `SKILL.md` ada di dalam `socs-article-writer` dan frontmatter-nya valid.

Pemasangan lewat `npx skills add` juga tersedia untuk beberapa agent, tetapi belum diuji untuk repo ini. Pemasangan manual di atas adalah cara yang sudah dicek.

## Cara pakai

Setelah skill terpasang, minta agent menulis artikel SOCS. Sebelum menulis, agent akan menanyakan nama lengkap, gelar, dan jabatan penulis, lalu menyimpannya di `penulis.local.md` di root workspace. File ini di-ignore git, jadi tidak ikut di-commit. Validator juga akan menolak artikel yang masih berisi placeholder seperti `[Nama]`.

Untuk memvalidasi draft secara manual (butuh Python 3, tanpa library tambahan):

```
python skills/socs-article-writer/scripts/validate_article.py "drafts/<judul>.md" --keywords "kata1,kata2"
```

Untuk membuat file Word dari draft Markdown (butuh `pip install python-docx==1.2.0`):

```
python skills/socs-article-writer/scripts/build_docx.py "drafts/<judul>/<judul>.md" "drafts/<judul>/<judul>.docx"
```

Format Word meniru artikel acuan *Agentic Coding* dengan kertas A4. Builder tidak memakai file artikel terbit, jadi repo ini tidak menyimpan contoh .docx apa pun.

## Aturan artikel

Aturan lengkap ada di `skills/socs-article-writer/references/aturan.md`. Contoh artikel yang sudah terbit ada di `skills/socs-article-writer/references/pola-artikel-terbit.md`.
