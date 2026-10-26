#!/usr/bin/env python3
"""Validasi draft artikel SOCS BINUS (format Markdown) terhadap references/aturan.md.

Pemakaian:
    python validate_article.py draft.md [--keywords "kata1,kata2"]

Exit code: 0 jika tidak ada temuan High, 1 jika ada temuan High.
Hanya memakai library standar Python.
"""
import argparse
import re
import sys
from collections import Counter

FIG_OK = re.compile(r"^Figure (\d+)\. (.+) \((https?://\S+|AI Generated)\)\s*$")
FIG_ANY = re.compile(r"^Figure\s+(\d+)\s*[.:]")
FIG_COLON = re.compile(r"^Figure (\d+): ")
BYLINE_LINE = re.compile(r"^Penulis\s*:")
BYLINE_OK = re.compile(r"^Penulis: .+, .+ [\u2013-] .+$")
YEAR = re.compile(r"\((19|20)\d{2}[^)]*\)")
URL = re.compile(r"https?://\S+")
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
TABLE_SEP = re.compile(r"^\s*\|?[\s:\-|]+\|?\s*$")
LIST_ITEM = re.compile(r"^\s*([-*+]|\d+\.)\s+")


def clean_words(text):
    text = re.sub(r"[*_`>#|]", " ", text)
    return re.findall(r"\S+", text)


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("draft")
    ap.add_argument("--keywords", default="", help="Keyword yang wajib muncul, dipisah koma")
    args = ap.parse_args()

    with open(args.draft, encoding="utf-8") as f:
        raw_lines = f.read().splitlines()

    findings = []  # (severity, message)

    def add(sev, msg):
        findings.append((sev, msg))

    # Judul = baris non-kosong pertama
    title_idx = next((i for i, l in enumerate(raw_lines) if l.strip()), None)
    if title_idx is None:
        print("File kosong.")
        return 1
    title = raw_lines[title_idx].lstrip("#").strip()
    title_words = len(title.split())
    if title_words > 10:
        add("Medium", f"Judul {title_words} kata (maks 10).")
    if len(title) > 70:
        add("Medium", f"Judul {len(title)} karakter (maks 70).")
    if ":" not in title:
        add("Low", "Judul sebaiknya format 'Nama Teknologi: Tagline' (tanda ':' belum ada).")

    # Pisahkan bagian: referensi, byline, caption, heading, dan prosa
    in_refs = False
    refs_entries = []
    refs_heading_line = None
    headings = []  # (level, text, line_no)
    prose = []  # (line_no, text)
    captions = []  # (line_no, line)
    byline_lines = []
    table_count = 0
    code_fence = False
    in_table = False
    code_found = False

    for i, line in enumerate(raw_lines):
        if i == title_idx:
            continue
        stripped = line.strip()
        if stripped.startswith("```"):
            code_fence = not code_fence
            code_found = True
            continue
        if code_fence:
            continue
        if not stripped:
            in_table = False
            continue

        m = HEADING.match(stripped)
        if m:
            level = len(m.group(1))
            text = m.group(2).strip()
            headings.append((level, text, i + 1))
            in_refs = text.lower().startswith("referensi")
            if in_refs and text.lower() != "referensi":
                refs_heading_line = i + 1
            continue

        if BYLINE_LINE.match(stripped):
            byline_lines.append((i + 1, stripped))
            in_refs = False
            continue

        if in_refs:
            refs_entries.append((i + 1, stripped))
            continue

        if FIG_ANY.match(stripped):
            captions.append((i + 1, stripped))
            continue

        if stripped.startswith("|"):
            if not in_table:
                table_count += 1
                in_table = True
            if TABLE_SEP.match(stripped):
                continue
            prose.append((i + 1, stripped))
            continue

        in_table = False
        prose.append((i + 1, stripped))

    # --- Panjang ---
    # Hitungan seperti Word: semua teks (judul, caption, byline, referensi, tabel) dihitung sekali.
    word_count = sum(
        len(clean_words(l))
        for l in raw_lines
        if l.strip() and not TABLE_SEP.match(l.strip()) and not l.strip().startswith("```")
    )
    if word_count < 500:
        add("High", f"Panjang artikel {word_count} kata (minimum 500).")
    elif word_count > 800:
        add("High", f"Panjang artikel {word_count} kata (maksimum 800).")
    elif not (600 <= word_count <= 700):
        add("Low", f"Panjang artikel {word_count} kata (target ideal 600-700).")

    # --- Subjudul ---
    h2h3 = [h for h in headings if h[0] in (2, 3)]
    if len(h2h3) < 3:
        add("High", f"Subjudul H2/H3 hanya {len(h2h3)} (minimum 3).")

    # --- Paragraf berurutan tidak boleh diawali kata yang sama ---
    prev_first = None
    for line_no, text in prose:
        if LIST_ITEM.match(text) or text.startswith("|"):
            prev_first = None
            continue
        words = clean_words(text)
        first = words[0].lower().strip(".,;:!?\"'()") if words else None
        if first and prev_first and first == prev_first:
            add("Medium", f"Baris {line_no}: paragraf berurutan diawali kata '{first}' yang sama.")
        prev_first = first

    # --- Hook pembuka ---
    if prose:
        first_para = clean_words(prose[0][1])
        if first_para and first_para[0].lower() not in ("bayangkan", "pernahkah", "dulu", "coba", "beberapa", "di", "dalam", "dunia", "pernah"):
            add("Low", "Pembuka sebaiknya dimulai adegan/fenomena konkret, misalnya 'Bayangkan ...' atau 'Pernahkah ...'.")

    # --- Figure ---
    if not captions:
        add("Medium", "Figure 1 wajib ada (tidak ditemukan caption Figure).")
    numbers = []
    for line_no, line in captions:
        if FIG_COLON.match(line):
            add("Medium", f"Baris {line_no}: caption memakai ':' — format wajib 'Figure N. Deskripsi (URL)'.")
        m_ok = FIG_OK.match(line)
        if not m_ok:
            if not URL.search(line) and "AI Generated" not in line:
                add("Medium", f"Baris {line_no}: caption figure tanpa URL sumber.")
            elif not FIG_COLON.match(line):
                add("Medium", f"Baris {line_no}: caption tidak sesuai format 'Figure N. Deskripsi (URL)'.")
            m_num = FIG_ANY.match(line)
        else:
            m_num = m_ok
        numbers.append(int(m_num.group(1)))
    if numbers:
        if numbers[0] != 1:
            add("Medium", f"Penomoran figure dimulai dari {numbers[0]}, harus dari 1.")
        expected = list(range(1, len(numbers) + 1))
        if numbers != expected:
            add("Medium", f"Penomoran figure tidak berurutan: {numbers}.")
    if captions and len(captions) < 2:
        add("Low", "Disarankan 2-4 figure (saat ini hanya 1).")
    if len(captions) > 4:
        add("Low", f"Figure {len(captions)} (disarankan maksimal 4).")

    # --- Tabel dan blok kode ---
    if table_count == 0:
        add("Low", "Belum ada tabel. Disarankan minimal 1 tabel ringkasan atau perbandingan.")
    if code_found:
        add("Low", "Ada blok kode. Artikel ini explainer, bukan tutorial; batasi potongan kode kecil.")

    # --- Byline ---
    if not byline_lines:
        add("Medium", "Blok 'Penulis:' tidak ditemukan di bagian penutup.")
    else:
        for line_no, line in byline_lines:
            if not BYLINE_OK.match(line):
                add("Medium", f"Baris {line_no}: format byline harus 'Penulis: Nama, Gelar – Jabatan'.")

    # --- Referensi ---
    if not any(h[1].lower().startswith("referensi") for h in headings):
        add("High", "Bagian 'Referensi' tidak ditemukan.")
    if refs_heading_line is not None:
        add("Medium", f"Baris {refs_heading_line}: heading 'Referensi' menempel dengan isi. Pisahkan jadi baris sendiri.")
    if len(refs_entries) < 3:
        add("High", f"Referensi hanya {len(refs_entries)} entri (minimum 3).")
    elif len(refs_entries) > 7:
        add("Medium", f"Referensi {len(refs_entries)} entri (maksimum 7).")
    for line_no, entry in refs_entries:
        if len(re.findall(r"https?://", entry)) > 1:
            add("Medium", f"Baris {line_no}: lebih dari satu referensi dalam satu baris, pisahkan.")
        if not URL.search(entry):
            add("High", f"Baris {line_no}: referensi tanpa URL.")
        if not YEAR.search(entry):
            add("Medium", f"Baris {line_no}: referensi tanpa tahun.")
        if "[" in entry and "]" in entry:
            add("Low", f"Baris {line_no}: nama organisasi sebaiknya tanpa kurung siku.")

    # --- Gaya: kata ganti dan caption tabel ---
    for i, l in enumerate(raw_lines):
        if re.search(r"\bAnda\b", l):
            add("Low", f"Baris {i + 1}: pakai 'kamu' atau 'kita', bukan 'Anda'.")
            break
    for i, l in enumerate(raw_lines):
        if re.match(r"^\s*Table\s+\d+[.:]", l):
            add("Low", f"Baris {i + 1}: caption tabel 'Table N.' tidak diatur, sebaiknya dihapus.")

    # --- Keyword ---
    keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]
    all_text = "\n".join(raw_lines).lower()
    for kw in keywords:
        if kw.lower() not in all_text:
            add("Medium", f"Keyword '{kw}' tidak muncul di artikel.")
    if keywords:
        main_kw = keywords[0].lower()
        if not any(main_kw in h[1].lower() for h in h2h3 if h[0] == 2):
            add("Medium", f"Keyword utama '{keywords[0]}' belum ada di salah satu subjudul H2.")

    # --- Laporan ---
    order = {"High": 0, "Medium": 1, "Low": 2}
    findings.sort(key=lambda x: order[x[0]])
    print(f"Judul      : {title}")
    print(f"Kata       : {word_count} (semua teks, seperti Word)")
    print(f"Subjudul   : {len(h2h3)} (H2/H3)")
    print(f"Figure     : {len(captions)}")
    print(f"Tabel      : {table_count}")
    print(f"Referensi  : {len(refs_entries)}")
    print()
    if not findings:
        print("Tidak ada temuan.")
    counts = Counter(s for s, _ in findings)
    for sev, msg in findings:
        print(f"[{sev}] {msg}")
    print()
    print(f"Ringkasan: High={counts['High']} Medium={counts['Medium']} Low={counts['Low']}")
    return 1 if counts["High"] else 0


if __name__ == "__main__":
    sys.exit(main())
