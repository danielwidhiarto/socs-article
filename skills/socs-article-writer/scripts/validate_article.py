#!/usr/bin/env python3
"""Validasi draft artikel SOCS BINUS atau BINUS @Bekasi CSSE (format Markdown).
Aturan SOCS: references/aturan.md. Override Bekasi: references/target-bekasi.md.

Pemakaian:
    python validate_article.py draft.md [--target socs|bekasi] [--keywords "kata1,kata2"] [--klaim klaim.md]

Jika --klaim diberikan, angka ber-satuan (%, persen, ms, detik, GB, kali, dst.) di draft
harus ada di baris buku klaim berstatus "Terverifikasi". Format tabel klaim:
| No | Klaim | Jenis | URL sumber | Bukti | Status |

Exit code: 0 jika tidak ada temuan High, 1 jika ada temuan High.
Hanya memakai library standar Python.
"""
import argparse
import re
import sys
from collections import Counter

CAPTION_DOT = re.compile(r"^Figure\s+(\d+)\.\s")  # format wajib SOCS (artikel acuan): 'Figure N. deskripsi'
CAPTION_COLON = re.compile(r"^Figure\s+(\d+):\s")  # tidak sesuai format SOCS, ditandai Medium
CAPTION_ANY_DOT = re.compile(r"^(?:Figure|Gambar)\s+(\d+)\.\s", re.IGNORECASE)
CAPTION_ANY_COLON = re.compile(r"^(?:Figure|Gambar)\s+(\d+):\s", re.IGNORECASE)
INLINE_SOURCE = re.compile(r"\(\s*sumber:\s*https?://\S+[^)]*\)", re.IGNORECASE)
SOURCE_BEKASI = re.compile(r"^\(\s*(?:sumber:\s*)?(https?://\S+|AI Generated)\)$", re.IGNORECASE)
BOLD_LEAD = re.compile(r"^\*\*(.+?)\*\*\s+\S")
REF_HEADINGS = ("referensi", "references", "daftar referensi", "daftar pustaka")
def is_refs_heading(text):
    t = text.strip().lower()
    return t in REF_HEADINGS or t.startswith("referensi") or t.startswith("references")
SOURCE = re.compile(r"^\((https?://\S+|AI Generated)\)$")
IMAGE = re.compile(r"^!\[[^\]]*\]\([^)]+\)")
BYLINE_LINE = re.compile(r"^Penulis:")
BYLINE_OK = re.compile(r"^Penulis: .+, .+ \u2013 .+$")
YEAR = re.compile(r"\((19|20)\d{2}[^)]*\)")
URL = re.compile(r"https?://\S+")
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
TABLE_SEP = re.compile(r"^\s*\|?[\s:\-|]+\|?\s*$")
LIST_ITEM = re.compile(r"^\s*([-*+]|\d+\.)\s+")
MEASURE = re.compile(
    r"(\d+(?:[.,]\d+)?)\s*(?:%|persen|ms|milidetik|detik|menit|jam|GB|MB|TB|kali|hari)(?![A-Za-z])",
    re.IGNORECASE,
)
OVERCLAIM = re.compile(
    r"\b(mewajibkan|menjamin|dijamin|terjamin|seratus persen|sempurna|terbukti|membuktikan|pasti)\b|100\s*%",
    re.IGNORECASE,
)
# --- Gaya anti-slop (references/gaya-menulis.md) ---
EM_DASH = re.compile(r"\u2014")
INTENSIFIERS = re.compile(
    r"\b(sangat|benar-benar|secara harfiah|sungguh|mendasar|secara signifikan|secara fundamental)\b",
    re.IGNORECASE,
)
FILLER_PHRASES = re.compile(
    r"\b(di era digital ini|seiring berkembangnya zaman|tak dapat dipungkiri|perlu diketahui bahwa|"
    r"pada intinya|tidak bisa dipungkiri|tak bisa dipungkiri)\b",
    re.IGNORECASE,
)
META_COMMENTARY = re.compile(
    r"\b(di bagian ini,? kita akan|seperti yang akan kita lihat|seperti yang sudah kita lihat|"
    r"mari kita bahas|berikut penjelasannya|itu adalah bahasan lain)\b",
    re.IGNORECASE,
)
BINARY_CONTRAST = re.compile(
    r"\b(bukan (?:sekadar|sekedar|hanya)[^.\n]{0,60}melainkan|bukan[^.\n]{0,60},? (?:melainkan|tetapi justru))\b",
    re.IGNORECASE,
)
EMPTY_DECLARATIVE = re.compile(
    r"\b(dampaknya (?:sangat )?besar|alasannya (?:bersifat )?struktural|taruhannya tinggi|"
    r"implikasinya (?:sangat )?signifikan)\b",
    re.IGNORECASE,
)
FALSE_AGENCY = re.compile(
    r"\b((?:keputusan|kebiasaan|tren|budaya)\s+(?:yang\s+)?muncul|"
    r"data\s+(?:memberi tahu|berbicara)|pasar\s+(?:memberi reward|menghargai))\b",
    re.IGNORECASE,
)
SWEEPING = re.compile(r"\b(semua orang|semua orang tahu|tidak ada yang tahu)\b", re.IGNORECASE)


def clean_words(text):
    text = re.sub(r"[*_`>#|]", " ", text)
    return re.findall(r"\S+", text)


ABBREV_DOT = re.compile(r"\b(dkk|dll|dsb|mis|sbb)\.", re.IGNORECASE)
DECIMAL_DOT = re.compile(r"\d+(?:\.\d+)+")
DOT_EXT = re.compile(r"\b[A-Za-z]+\.(?:md|py|json|ya?ml|tsx?|jsx?)\b")
SENT_SPLIT = re.compile(r'[.!?]+["\')\]]*(?:\s+|$)')


def count_sentences(text):
    """Hitung kalimat; titik di angka (2310.08560), ekstensi file (CLAUDE.md), dan singkatan (dkk.) tidak dihitung."""
    t = DECIMAL_DOT.sub(lambda m: m.group(0).replace(".", "\x00"), text)
    t = DOT_EXT.sub(lambda m: m.group(0).replace(".", "\x00"), t)
    t = ABBREV_DOT.sub(lambda m: m.group(0)[:-1] + "\x00", t)
    return len([p for p in SENT_SPLIT.split(t) if p.strip()])


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser()
    ap.add_argument("draft")
    ap.add_argument("--target", default="socs", choices=("socs", "bekasi"),
                    help="Target redaksi: socs (default) atau bekasi (override target-bekasi.md)")
    ap.add_argument("--keywords", default="", help="Keyword yang wajib muncul, dipisah koma")
    ap.add_argument("--klaim", default="", help="Path buku klaim (klaim.md) untuk memeriksa angka")
    args = ap.parse_args()
    bekasi = args.target == "bekasi"

    with open(args.draft, encoding="utf-8") as f:
        raw_lines = f.read().splitlines()

    findings = []  # (severity, message)

    def add(sev, msg):
        findings.append((sev, msg))

    title_idx = next((i for i, l in enumerate(raw_lines) if l.strip()), None)
    if title_idx is None:
        print("File kosong.")
        return 1
    title = raw_lines[title_idx].lstrip("#").strip().replace("**", "")
    title_words = len(title.split())
    if bekasi:
        if title_words > 15:
            add("Low", f"Judul {title_words} kata (maks 15 untuk Bekasi).")
        if len(title) > 110:
            add("Low", f"Judul {len(title)} karakter (maks 110 untuk Bekasi).")
    else:
        if title_words > 10:
            add("Medium", f"Judul {title_words} kata (maks 10).")
        if len(title) > 70:
            add("Medium", f"Judul {len(title)} karakter (maks 70).")
        if ":" not in title:
            add("Low", "Judul sebaiknya format 'Nama Teknologi: Tagline' (tanda ':' belum ada).")

    # Hitungan kata seperti Word: semua teks dihitung sekali, kecuali baris tabel pemisah dan blok kode.
    word_count = 0
    in_code = False
    for l in raw_lines:
        s = l.strip()
        if s.startswith("```"):
            in_code = not in_code
            continue
        if in_code or not s or TABLE_SEP.match(s):
            continue
        word_count += len(clean_words(s))

    in_refs = False
    refs_entries = []
    refs_heading_line = None
    headings = []  # (level, text, line_no)
    prose = []  # (line_no, text)
    captions = []  # (line_no, line)
    byline_check = []  # (line_no, text) baris setelah 'Penulis:'
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
            text = m.group(2).strip()
            headings.append((len(m.group(1)), text, i + 1))
            if is_refs_heading(text):
                in_refs = True
                if text.lower() not in REF_HEADINGS:
                    refs_heading_line = i + 1
            else:
                in_refs = False
            continue

        if BYLINE_LINE.match(stripped):
            byline_check.append((i + 1, stripped))
            in_refs = False
            continue

        if in_refs:
            refs_entries.append((i + 1, stripped))
            continue

        cap = ((CAPTION_ANY_DOT.match(stripped) or CAPTION_ANY_COLON.match(stripped))
               if bekasi else (CAPTION_DOT.match(stripped) or CAPTION_COLON.match(stripped)))
        if cap:
            captions.append((i + 1, stripped))
            continue

        if IMAGE.match(stripped):
            continue

        if SOURCE.match(stripped) or (bekasi and SOURCE_BEKASI.match(stripped)):
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

    # --- Panjang (SOCS 500-800; Bekasi 400-1100 dari 34 arsip published/bekasi-csse) ---
    if bekasi:
        if word_count < 400:
            add("High", f"Panjang artikel {word_count} kata (minimum 400 untuk Bekasi).")
        elif word_count > 1100:
            add("High", f"Panjang artikel {word_count} kata (maksimum 1100 untuk Bekasi).")
        elif not (600 <= word_count <= 800):
            add("Low", f"Panjang artikel {word_count} kata (target ideal 600-700).")
    elif word_count < 500:
        add("High", f"Panjang artikel {word_count} kata (minimum 500).")
    elif word_count > 800:
        add("High", f"Panjang artikel {word_count} kata (maksimum 800).")
    elif not (600 <= word_count <= 700):
        add("Low", f"Panjang artikel {word_count} kata (target ideal 600-700).")

    # --- Subjudul (SOCS: min 3 H2/H3; Bekasi: min 2, level bebas + bold-lead) ---
    h2h3 = [h for h in headings if h[0] in (2, 3)]
    if bekasi:
        bold_leads = [t for _, t in prose if BOLD_LEAD.match(t)]
        h_all = [h for h in headings if h[0] in (1, 2, 3)]
        if len(h_all) + len(bold_leads) < 2:
            add("Medium", f"Subjudul hanya {len(h_all) + len(bold_leads)} (minimum 2 untuk Bekasi).")
    elif len(h2h3) < 3:
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

    # --- Paragraf minimal 5 kalimat SOCS / 3 kalimat Bekasi (aturan.md bagian 4) ---
    para_min = 3 if bekasi else 5
    for line_no, text in prose:
        if LIST_ITEM.match(text) or text.startswith("|"):
            continue
        if BOLD_LEAD.match(text) and bekasi:
            text = BOLD_LEAD.sub("", text, count=1)
        if text.rstrip().endswith(":"):
            continue  # kalimat pengantar sebelum daftar bullet atau tabel
        n_sent = count_sentences(text)
        if n_sent < para_min:
            add("Medium", f"Baris {line_no}: paragraf hanya {n_sent} kalimat (minimal {para_min}; lengkapi di paragraf yang sama sebelum memulai paragraf baru).")

    # --- Hook pembuka ---
    if prose:
        first_para = clean_words(prose[0][1])
        if first_para and first_para[0].lower() not in (
            "bayangkan", "pernahkah", "pernah", "coba", "dulu", "beberapa", "di", "dalam", "dunia", "banyak", "peta",
        ):
            add("Low", "Pembuka sebaiknya dimulai adegan/fenomena konkret, misalnya 'Bayangkan ...' atau 'Pernahkah ...'.")

    # --- Figure: SOCS 'Figure N.' + baris '(URL)'; Bekasi 'Gambar N.' + sumber inline/(sumber:) ---
    if bekasi:
        if not captions:
            add("Medium", "Gambar 1 wajib ada untuk Bekasi (tidak ditemukan caption Gambar/Figure).")
        numbers = []
        for line_no, line in captions:
            if CAPTION_ANY_COLON.match(line):
                add("Medium", f"Baris {line_no}: caption memakai ':' setelah nomor, format wajib 'Gambar N. deskripsi'.")
            numbers.append(int((CAPTION_ANY_DOT.match(line) or CAPTION_ANY_COLON.match(line)).group(1)))
            if INLINE_SOURCE.search(line):
                continue  # sumber inline: 'Gambar 1. ... (sumber: URL)'
            next_line = next((l.strip() for l in raw_lines[line_no:line_no + 2] if l.strip()), "")
            if not SOURCE_BEKASI.match(next_line):
                add("Low", f"Baris {line_no}: sumber figure sebaiknya di baris berikutnya '(URL)' atau '(sumber: URL)', atau inline '(sumber: URL)'.")
        if numbers:
            if numbers[0] != 1:
                add("Medium", f"Penomoran figure dimulai dari {numbers[0]}, harus dari 1.")
            if numbers != list(range(1, len(numbers) + 1)):
                add("Medium", f"Penomoran figure tidak berurutan: {numbers}.")
        if len(captions) > 6:
            add("Low", f"Figure {len(captions)} (umumnya 1-6 untuk Bekasi).")
    else:
        if not captions:
            add("Medium", "Figure 1 wajib ada (tidak ditemukan caption Figure).")
        numbers = []
        for line_no, line in captions:
            if CAPTION_COLON.match(line):
                add("Medium", f"Baris {line_no}: caption memakai ':' setelah nomor, format wajib 'Figure N. deskripsi'.")
            numbers.append(int((CAPTION_DOT.match(line) or CAPTION_COLON.match(line)).group(1)))
            # Sumber figure harus di baris berikutnya yang tidak kosong.
            next_line = next((l.strip() for l in raw_lines[line_no:line_no + 2] if l.strip()), "")
            if not SOURCE.match(next_line):
                add("Medium", f"Baris {line_no}: sumber figure harus di baris berikutnya dalam kurung, misalnya '(https://...)' atau '(AI Generated)'.")
        if numbers:
            if numbers[0] != 1:
                add("Medium", f"Penomoran figure dimulai dari {numbers[0]}, harus dari 1.")
            if numbers != list(range(1, len(numbers) + 1)):
                add("Medium", f"Penomoran figure tidak berurutan: {numbers}.")
            # Setiap figure harus disebut di kalimat artikel, bukan hanya di caption (aturan.md bagian 6).
            body_text = "\n".join(t for _, t in prose)
            for n in numbers:
                mentions = len(re.findall(rf"Figure\s+{n}\b", body_text))
                if mentions == 0:
                    add("Low", f"Figure {n} tidak pernah disebut di kalimat artikel; tambahkan rujukan seperti 'seperti pada Figure {n}' di paragraf yang membahasnya.")
        if captions and len(captions) < 2:
            add("Low", "Disarankan 2-4 figure (saat ini hanya 1).")
        if len(captions) > 4:
            add("Low", f"Figure {len(captions)} (disarankan maksimal 4).")

    # --- Tabel dan blok kode ---
    if table_count == 0:
        add("Low", "Belum ada tabel. Disarankan minimal 1 tabel ringkasan atau perbandingan.")
    if code_found:
        add("Low", "Ada blok kode. Artikel ini explainer, bukan tutorial; batasi potongan kode kecil.")

    # --- Byline: SOCS wajib; Bekasi tanpa byline (34/34 arsip tanpa 'Penulis:'; 2 file bawa sisa 'Author:' pola lama, jangan ditiru) ---
    if bekasi:
        for line_no, text in byline_check:
            add("Low", f"Baris {line_no}: Bekasi tidak memakai baris 'Penulis:' di badan artikel; hapus.")
    else:
        if not byline_check:
            add("Medium", "Baris 'Penulis:' tidak ditemukan di bagian penutup.")
        for line_no, text in byline_check:
            if not BYLINE_OK.match(text):
                add("Medium", f"Baris {line_no}: format byline harus 'Penulis: Nama, Gelar – Jabatan' dalam satu baris, dengan en dash.")

    # --- Referensi (Bekasi: heading bebas, format bebas, tahun opsional, maks 8) ---
    if bekasi:
        if not any(is_refs_heading(h[1]) for h in headings if h[0] in (1, 2)):
            add("High", "Bagian 'Referensi' tidak ditemukan (diterima: Referensi, References, Daftar Referensi, Daftar Pustaka).")
        if refs_heading_line is not None:
            add("Medium", f"Baris {refs_heading_line}: heading referensi menempel dengan isi. Pisahkan jadi baris sendiri.")
        if len(refs_entries) < 3:
            add("High", f"Referensi hanya {len(refs_entries)} entri (minimum 3).")
        elif len(refs_entries) > 8:
            add("Low", f"Referensi {len(refs_entries)} entri (umumnya 3-8 untuk Bekasi).")
        for line_no, entry in refs_entries:
            if len(re.findall(r"https?://", entry)) > 1:
                add("Medium", f"Baris {line_no}: lebih dari satu referensi dalam satu baris, pisahkan.")
            if not URL.search(entry):
                add("High", f"Baris {line_no}: referensi tanpa URL.")
    else:
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

    # --- Placeholder yang tertinggal (mis. [Nama], [Gelar], [URL sumber]) ---
    placeholder_hits = re.findall(r"\[[^\[\]\n]+\](?!\()", "\n".join(raw_lines))
    if placeholder_hits:
        sample = ", ".join(sorted(set(placeholder_hits))[:5])
        add("High", f"Placeholder tertinggal di artikel: {sample}. Isi dengan data asli sebelum dibuat .docx.")

    # --- Gaya: SOCS wajib kamu/kita; Bekasi bebas (mayoritas sampel pakai Anda) ---
    if not bekasi:
        for i, l in enumerate(raw_lines):
            if re.search(r"\bAnda\b", l):
                add("Low", f"Baris {i + 1}: pakai 'kamu' atau 'kita', bukan 'Anda'.")
                break
    for i, l in enumerate(raw_lines):
        if re.match(r"^\s*Table\s+\d+[.:]", l):
            add("Low", f"Baris {i + 1}: caption tabel 'Table N.' tidak diatur, sebaiknya dihapus.")

    # --- Gaya anti-slop (references/gaya-menulis.md) ---
    slop_patterns = (
        (BINARY_CONTRAST, "kontras biner gimmick 'bukan X, melainkan Y'; tulis Y langsung"),
        (FILLER_PHRASES, "pembuka basa-basi (throat-clearing); hapus, langsung ke inti"),
        (META_COMMENTARY, "meta-komentar; artikel tidak perlu menceritakan strukturnya sendiri"),
        (FALSE_AGENCY, "agency palsu: benda mati melakukan aksi manusia; sebut pelakunya"),
        (EMPTY_DECLARATIVE, "declaratif kosong; sebut hal spesifik yang dimaksud"),
        (SWEEPING, "klaim melang; pakai spesifik, bukan 'semua orang'"),
        (INTENSIFIERS, "intensifier kosong; hapus atau ganti dengan data spesifik"),
    )
    slop_first = None
    for i, l in enumerate(raw_lines):
        for pat, hint in slop_patterns:
            m = pat.search(l)
            if m and slop_first is None:
                slop_first = (pat, hint)
            while m:
                add("Low", f"Baris {i + 1}: gaya anti-slop, {hint}. Temuan: \"{m.group(0).strip()}\".")
                m = pat.search(l, m.end())
    if slop_first:
        add(
            "Low",
            "Cek gaya lengkap ada di references/gaya-menulis.md (skoring self-check 5 dimensi).",
        )
    for i, l in enumerate(raw_lines):
        m = EM_DASH.search(l)
        if m:
            add("Medium", f"Baris {i + 1}: em dash (—) dilarang; pakai koma, titik, atau tanda kurung.")


    # --- Keyword ---
    keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]
    all_text = "\n".join(raw_lines).lower()
    for kw in keywords:
        if kw.lower() not in all_text:
            add("Medium", f"Keyword '{kw}' tidak muncul di artikel.")
    if keywords:
        main_kw = keywords[0].lower()
        if bekasi:
            heads = headings + [(0, t, n) for n, t in prose if BOLD_LEAD.match(t)]
            if not any(main_kw in h[1].lower() for h in heads):
                add("Medium", f"Keyword utama '{keywords[0]}' belum ada di salah satu subjudul.")
        elif not any(main_kw in h[1].lower() for h in h2h3 if h[0] == 2):
            add("Medium", f"Keyword utama '{keywords[0]}' belum ada di salah satu subjudul H2.")

    # --- Kata absolut (overclaim): Low, minta diperhalus atau diberi sumber yang sekuat itu ---
    for i, l in enumerate(raw_lines):
        for m in OVERCLAIM.finditer(l):
            add("Low", f"Baris {i + 1}: kata absolut '{m.group(0)}'. Perhalus, atau pastikan sumber memang mengatakannya sekuat itu.")

    # --- Buku klaim: setiap angka ber-satuan harus Terverifikasi ---
    def norm(num):
        return str(float(num.replace(",", ".")))

    draft_measures = {norm(m.group(1)) for m in MEASURE.finditer("\n".join(raw_lines))}
    draft_shown = {norm(m.group(1)): m.group(1) for m in MEASURE.finditer("\n".join(raw_lines))}
    if args.klaim:
        with open(args.klaim, encoding="utf-8") as kf:
            klaim_rows = [l.strip() for l in kf.read().splitlines() if l.strip().startswith("|")]
        verified_text = ""
        unverified = []
        for row in klaim_rows:
            cells = [c.strip() for c in row.strip("|").split("|")]
            if len(cells) < 6 or not cells[0] or cells[0].lower() == "no" or set(cells[0]) <= set("-: "):
                continue
            claim_text, status = cells[1], cells[-1]
            if status.lower() == "terverifikasi":
                verified_text += " " + claim_text + " " + cells[4]
            else:
                unverified.append((cells[0], claim_text, status))
        verified_measures = {norm(m.group(1)) for m in MEASURE.finditer(verified_text)}
        for num in sorted(draft_measures - verified_measures):
            add("Medium", f"Angka '{draft_shown[num]}' di draft tidak ada di buku klaim berstatus Terverifikasi.")
        for no, claim_text, status in unverified:
            nums = {norm(m.group(1)) for m in MEASURE.finditer(claim_text)}
            if nums & draft_measures:
                add("Medium", f"Klaim {no} berstatus '{status}' tetapi angkanya masih dipakai di draft: {claim_text[:60]}")
    elif draft_measures:
        add("Low", "Buku klaim tidak diberikan (--klaim); angka persen, ukuran, dan waktu tidak diperiksa mekanis.")

    # --- Laporan ---
    order = {"High": 0, "Medium": 1, "Low": 2}
    findings.sort(key=lambda x: order[x[0]])
    print(f"Target     : {args.target} ({'BINUS @Bekasi CSSE' if bekasi else 'SOCS BINUS'})")
    print(f"Judul      : {title}")
    print(f"Kata       : {word_count} (semua teks, seperti Word)")
    n_sub = (len([h for h in headings if h[0] in (1, 2, 3)])
             + len([t for _, t in prose if BOLD_LEAD.match(t)])) if bekasi else len(h2h3)
    print(f"Subjudul   : {n_sub} ({'H1/H2/H3+bold' if bekasi else 'H2/H3'})")
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

