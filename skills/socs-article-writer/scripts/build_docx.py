#!/usr/bin/env python3
"""Ubah draft Markdown artikel SOCS atau Bekasi CSSE menjadi .docx.

SOCS: format meniru artikel acuan "Agentic Coding" (folder submitted/socs), kertas A4.
Bekasi CSSE: meniru pola dominan 34 arsip published/bekasi-csse (Pola A):
judul Title tengah, subjudul Heading 2, caption 'Gambar N. ... (sumber: URL)' rata tengah,
list bullet/numbered dan referensi rata kiri tanpa indent,

Pemakaian:
    python build_docx.py draft.md keluaran.docx [--target socs|bekasi]

Sintaks Markdown yang didukung:
    # Judul                        judul, tengah, tebal (baris pertama)
    ## Subjudul                    subjudul tebal, rata kiri-kanan
    ## Referensi                   heading referensi; baris setelahnya = entri referensi
    Penulis: Nama, Gelar - Jabatan  byline satu baris SOCS (dibuat tebal; Bekasi: tidak dipakai)
    ![](gambar.png){w=14.3cm}     gambar (path relatif terhadap file draft; w dan h opsional, dalam cm)
    Gambar N. deskripsi (sumber: URL)  caption Bekasi (sumber inline atau di baris berikutnya)
    Figure N. deskripsi            caption SOCS
    (https://sumber)              sumber figure di baris berikutnya, atau (AI Generated)
    | Kolom | Kolom |             tabel pipa; baris pertama = header (tebal)
    - item                        bullet
    1. item                       daftar bernomor (mulai ulang setiap daftar)
    **tebal**, *miring*           format inline; URL menjadi hyperlink
    baris lain                    paragraf isi, indent baris pertama 1,27 cm

Membutuhkan: python-docx==1.2.0
"""
import os
import re
import sys

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
from docx.shared import Inches, Mm, Pt, RGBColor

CM_TO_EMU = 360000
DEFAULT_IMG_WIDTH_CM = 14.3
FONT = "Times New Roman"
CAPTION_PT = 11

RE_IMAGE = re.compile(r"^!\[[^\]]*\]\(([^)]+)\)(?:\{([^}]*)\})?$")
RE_IMAGE_SIZE = re.compile(r"(w|h)=([\d.]+)cm")
RE_CAPTION_ANY = re.compile(r"^(?:Figure|Gambar)\s+(\d+)\.\s(.*)$", re.IGNORECASE)
RE_SOURCE_ANY = re.compile(r"^\(\s*(?:sumber:\s*)?(https?://\S+|AI Generated)\)$", re.IGNORECASE)
RE_INLINE_SOURCE = re.compile(r"^(.*?)\(\s*sumber:\s*(https?://\S+?)\)\s*$", re.IGNORECASE)
RE_BULLET = re.compile(r"^[-*+]\s+(.*)$")
RE_NUMBER = re.compile(r"^\d+\.\s+(.*)$")
RE_INLINE = re.compile(r"(\*\*.+?\*\*|(?<!\*)\*[^*\s][^*]*?\*(?!\*)|https?://[^\s)]+)")
RE_TABLE_SEP = re.compile(r"^\s*\|?[\s:\-|]+\|?\s*$")

# Penomoran: abstractNum 100 = bullet, 101 = desimal. Nilainya meniru artikel acuan.
ABSTRACT_BULLET = (
    f'<w:abstractNum {nsdecls("w")} w:abstractNumId="100">'
    '<w:multiLevelType w:val="hybridMultilevel"/>'
    '<w:lvl w:ilvl="0"><w:start w:val="1"/><w:numFmt w:val="bullet"/>'
    '<w:lvlText w:val="\uf0b7"/><w:lvlJc w:val="left"/>'
    '<w:pPr><w:tabs><w:tab w:val="num" w:pos="720"/></w:tabs><w:ind w:left="720" w:hanging="360"/></w:pPr>'
    '<w:rPr><w:rFonts w:ascii="Symbol" w:hAnsi="Symbol" w:hint="default"/><w:sz w:val="20"/></w:rPr>'
    '</w:lvl></w:abstractNum>'
)
ABSTRACT_DECIMAL = (
    f'<w:abstractNum {nsdecls("w")} w:abstractNumId="101">'
    '<w:multiLevelType w:val="hybridMultilevel"/>'
    '<w:lvl w:ilvl="0"><w:start w:val="1"/><w:numFmt w:val="decimal"/>'
    '<w:lvlText w:val="%1."/><w:lvlJc w:val="left"/>'
    '<w:pPr><w:tabs><w:tab w:val="num" w:pos="720"/></w:tabs><w:ind w:left="720" w:hanging="360"/></w:pPr>'
    '</w:lvl></w:abstractNum>'
)
NUM_BULLET_ID = 100
NUM_DECIMAL_BASE = 101

# Gaya tabel dan hyperlink dari artikel acuan (Grid Table Light, Hyperlink).
TABLE_STYLE = (
    f'<w:style {nsdecls("w")} w:type="table" w:styleId="TableGridLight">'
    '<w:name w:val="Grid Table Light"/><w:basedOn w:val="TableNormal"/><w:uiPriority w:val="40"/>'
    '<w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/></w:pPr>'
    '<w:tblPr><w:tblBorders>'
    + "".join(
        f'<w:{side} w:val="single" w:sz="4" w:space="0" w:color="BFBFBF"/>'
        for side in ("top", "left", "bottom", "right", "insideH", "insideV")
    )
    + "</w:tblBorders></w:tblPr></w:style>"
)
HYPERLINK_STYLE = (
    f'<w:style {nsdecls("w")} w:type="character" w:styleId="Hyperlink">'
    '<w:name w:val="Hyperlink"/><w:basedOn w:val="DefaultParagraphFont"/><w:uiPriority w:val="99"/>'
    '<w:unhideWhenUsed/><w:rPr><w:color w:val="467886"/><w:u w:val="single"/></w:rPr></w:style>'
)


def parse_blocks(lines, bekasi=False):
    """Ubah baris Markdown menjadi daftar blok (jenis, isi)."""
    blocks = []
    in_refs = False
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        i += 1
        if not s:
            continue
        m_head = re.match(r"^(#{1,6})\s+(.*)$", s)
        if m_head and (len(m_head.group(1)) > 1 or not any(k == "title" for k, _ in blocks)):
            # '# ' pertama = judul; '# '/lainnya setelah itu = subjudul (pola Bekasi).
            level = len(m_head.group(1))
            if level == 1 and any(k == "title" for k, _ in blocks):
                blocks.append(("heading", m_head.group(2).strip()))
            elif level == 1:
                blocks.append(("title", m_head.group(2).strip()))
            else:
                heading = m_head.group(2).strip()
                in_refs = heading.lower() in ("referensi", "references", "daftar referensi", "daftar pustaka")
                blocks.append(("heading", heading))
            continue
        if s.startswith("Penulis:"):
            blocks.append(("byline", s))
            continue
        m = RE_IMAGE.match(s)
        if m:
            blocks.append(("image", (m.group(1), m.group(2) or "")))
            continue
        m = RE_CAPTION_ANY.match(s)
        if m:
            label = "Gambar" if bekasi else "Figure"
            tail = m.group(2).strip()
            inline = RE_INLINE_SOURCE.match(tail)
            if inline:
                blocks.append(("caption", f"{label} {m.group(1)}. {inline.group(1).strip()}"))
                src = f"(sumber: {inline.group(2)})" if bekasi else f"({inline.group(2)})"
                blocks.append(("source", src))
            else:
                # Label caption mengikuti target: 'Figure N.' (SOCS) vs 'Gambar N.' (Bekasi).
                blocks.append(("caption", f"{label} {m.group(1)}. {tail}"))
            continue
        if RE_SOURCE_ANY.match(s):
            url = RE_SOURCE_ANY.match(s).group(1)
            if bekasi:
                blocks.append(("source", f"(sumber: {url})" if not s.lower().startswith("(sumber:") else s))
            else:
                # SOCS: baris sumber polos '(URL)'.
                blocks.append(("source", f"({url})"))
            continue
        if s.startswith("|"):
            rows = [s]
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append(lines[i].strip())
                i += 1
            blocks.append(("table", rows))
            continue
        m = RE_BULLET.match(s)
        if m and not in_refs:
            blocks.append(("bullet", m.group(1)))
            continue
        m = RE_NUMBER.match(s)
        if m and not in_refs:
            blocks.append(("number", m.group(1)))
            continue
        if in_refs:
            blocks.append(("ref", s))
            continue
        blocks.append(("body", s))
    return blocks


def set_auto_spacing(p, before_auto=True):
    """Spasi otomatis seperti artikel acuan: before/after 100 dengan autospacing, baris 1,5."""
    p.paragraph_format.line_spacing = 1.5
    sp = p._p.pPr.find(qn("w:spacing"))
    sp.set(qn("w:before"), "100")
    sp.set(qn("w:after"), "100")
    if before_auto:
        sp.set(qn("w:beforeAutospacing"), "1")
        sp.set(qn("w:afterAutospacing"), "1")


def run_format(run, bold=False, italic=False, size_pt=None):
    run.font.color.rgb = RGBColor(0, 0, 0)
    if bold:
        run.bold = True
        run._r.get_or_add_rPr().find(qn("w:b")).addnext(OxmlElement("w:bCs"))
    if italic:
        run.italic = True
        run._r.get_or_add_rPr().find(qn("w:i")).addnext(OxmlElement("w:iCs"))
    if size_pt:
        run.font.size = Pt(size_pt)
        run._r.get_or_add_rPr().find(qn("w:sz")).addnext(OxmlElement("w:szCs"))


def add_hyperlink(p, url, bold=False, italic=False, size_pt=None):
    r_id = p.part.relate_to(url, RT.HYPERLINK, is_external=True)
    hl = OxmlElement("w:hyperlink")
    hl.set(qn("r:id"), r_id)
    r = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    rstyle = OxmlElement("w:rStyle")
    rstyle.set(qn("w:val"), "Hyperlink")
    rpr.append(rstyle)
    if bold:
        rpr.append(OxmlElement("w:b"))
        rpr.append(OxmlElement("w:bCs"))
    if italic:
        rpr.append(OxmlElement("w:i"))
        rpr.append(OxmlElement("w:iCs"))
    color = OxmlElement("w:color")
    color.set(qn("w:val"), "000000")
    rpr.append(color)
    if size_pt:
        sz = OxmlElement("w:sz")
        sz.set(qn("w:val"), str(int(size_pt * 2)))
        rpr.append(sz)
        szcs = OxmlElement("w:szCs")
        szcs.set(qn("w:val"), str(int(size_pt * 2)))
        rpr.append(szcs)
    r.append(rpr)
    t = OxmlElement("w:t")
    t.set(qn("xml:space"), "preserve")
    t.text = url
    r.append(t)
    hl.append(r)
    p._p.append(hl)


def add_inline(p, text, bold=False, italic=False, size_pt=None):
    """Tambahkan teks dengan markup **tebal**, *miring*, dan URL (menjadi hyperlink)."""
    for part in RE_INLINE.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**") and len(part) > 4:
            add_inline(p, part[2:-2], True, italic, size_pt)
        elif part.startswith("*") and part.endswith("*") and len(part) > 2 and not part.startswith("**"):
            add_inline(p, part[1:-1], bold, True, size_pt)
        elif part.startswith("http://") or part.startswith("https://"):
            add_hyperlink(p, part, bold, italic, size_pt)
        else:
            run = p.add_run(part)
            run_format(run, bold, italic, size_pt)


def add_table(doc, rows):
    cells_rows = []
    for r in rows:
        if RE_TABLE_SEP.match(r):
            continue
        cells_rows.append([c.strip() for c in r.strip("|").split("|")])
    ncols = max(len(r) for r in cells_rows)
    cells_rows = [r + [""] * (ncols - len(r)) for r in cells_rows]

    table = doc.add_table(rows=len(cells_rows), cols=ncols)
    table.style = doc.styles["Grid Table Light"]
    tbl_pr = table._tbl.tblPr
    tbl_w = tbl_pr.find(qn("w:tblW"))
    tbl_w.set(qn("w:w"), "0")
    tbl_w.set(qn("w:type"), "auto")
    look = tbl_pr.find(qn("w:tblLook"))
    if look is not None:
        for k, v in {"w:val": "04A0", "w:firstRow": "1", "w:lastRow": "0", "w:firstColumn": "1",
                     "w:lastColumn": "0", "w:noHBand": "0", "w:noVBand": "1"}.items():
            look.set(qn(k), v)

    for r_idx, row in enumerate(cells_rows):
        for c_idx, text in enumerate(row):
            cell = table.cell(r_idx, c_idx)
            tc_w = cell._tc.get_or_add_tcPr().get_or_add_tcW()
            tc_w.set(qn("w:w"), "0")
            tc_w.set(qn("w:type"), "auto")
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            set_auto_spacing(p)
            add_inline(p, text, bold=(r_idx == 0))
    return table


def add_numbered(p, num_id):
    p._p.get_or_add_pPr().get_or_add_numPr()
    numpr = p._p.pPr.numPr
    numpr.get_or_add_ilvl().val = 0
    numpr.get_or_add_numId().val = num_id


def inject_definitions(doc):
    """Tambahkan gaya tabel, hyperlink, dan penomoran acuan ke dokumen baru."""
    styles = doc.styles.element
    styles.append(parse_xml(TABLE_STYLE))
    styles.append(parse_xml(HYPERLINK_STYLE))
    numbering = doc.part.numbering_part.element
    first_num = numbering.find(qn("w:num"))
    for xml in (ABSTRACT_BULLET, ABSTRACT_DECIMAL):
        node = parse_xml(xml)
        if first_num is not None:
            first_num.addprevious(node)
        else:
            numbering.append(node)
    numbering.append(parse_xml(
        f'<w:num {nsdecls("w")} w:numId="{NUM_BULLET_ID}"><w:abstractNumId w:val="100"/></w:num>'
    ))


def new_decimal_num(doc, counter):
    """Setiap daftar bernomor memakai num baru dengan startOverride, supaya mulai dari 1 lagi."""
    num_id = NUM_DECIMAL_BASE + counter
    doc.part.numbering_part.element.append(parse_xml(
        f'<w:num {nsdecls("w")} w:numId="{num_id}"><w:abstractNumId w:val="101"/>'
        '<w:lvlOverride w:ilvl="0"><w:startOverride w:val="1"/></w:lvlOverride></w:num>'
    ))
    return num_id


def build(md_path, out_path, target="socs"):
    bekasi = target == "bekasi"
    base_dir = os.path.dirname(os.path.abspath(md_path))
    with open(md_path, encoding="utf-8") as f:
        blocks = parse_blocks(f.read().splitlines(), bekasi)

    doc = Document()
    body = doc.element.body
    for child in list(body):
        if child.tag != qn("w:sectPr"):
            body.remove(child)

    # Kertas: SOCS A4 sesuai kebutuhan redaksi; Bekasi CSSE Letter (21,59 x 27,94 cm)
    # sesuai 34 arsip published/bekasi-csse.
    sec = doc.sections[0]
    if bekasi:
        sec.page_width = Inches(8.5)
        sec.page_height = Inches(11)
    else:
        sec.page_width = Mm(210)
        sec.page_height = Mm(297)

    normal = doc.styles["Normal"]
    normal.font.name = FONT
    normal.font.size = Pt(12)
    normal.font.color.rgb = RGBColor(0, 0, 0)
    rpr = normal.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    for attr in ("w:eastAsia", "w:cs"):
        rfonts.set(qn(attr), FONT)
    lang = OxmlElement("w:lang")
    lang.set(qn("w:val"), "en-ID")
    lang.set(qn("w:eastAsia"), "en-US")
    rpr.append(lang)
    normal.paragraph_format.line_spacing = 1.5
    normal.paragraph_format.space_after = Pt(8)

    inject_definitions(doc)

    cp = doc.core_properties
    cp.author = ""
    cp.last_modified_by = ""

    decimal_counter = 0
    prev_kind = None
    for kind, value in blocks:
        if kind == "number" and prev_kind != "number":
            decimal_counter += 1
            num_id = NUM_DECIMAL_BASE + decimal_counter
            new_decimal_num(doc, decimal_counter)
        elif kind == "number":
            num_id = NUM_DECIMAL_BASE + decimal_counter

        if kind == "title":
            if bekasi:
                p = doc.add_paragraph(style="Title")
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.paragraph_format.line_spacing = 1.5
            add_inline(p, value, bold=(not bekasi))
            cp.title = value

        elif kind == "heading":
            if bekasi:
                p = doc.add_paragraph(style="Heading 2")
                add_inline(p, value)
            else:
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                set_auto_spacing(p)
                add_inline(p, value, bold=True)

        elif kind == "byline":
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            set_auto_spacing(p)
            add_inline(p, value, bold=True)

        elif kind == "image":
            path_value, attrs = value
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            set_auto_spacing(p)
            img_path = path_value if os.path.isabs(path_value) else os.path.join(base_dir, path_value)
            if not os.path.exists(img_path):
                raise SystemExit(f"Gambar tidak ditemukan: {img_path} (simpan gambar di folder draft, lalu perbaiki path di Markdown)")
            size = {k: float(v) for k, v in RE_IMAGE_SIZE.findall(attrs)}
            width_cm = size.get("w", DEFAULT_IMG_WIDTH_CM)
            width = int(round(width_cm * CM_TO_EMU))
            height = int(round(size["h"] * CM_TO_EMU)) if "h" in size else None
            p.add_run().add_picture(img_path, width=width, height=height)

        elif kind == "caption":
            if bekasi:
                p = doc.add_paragraph(style="Caption")
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                add_inline(p, value)
                continue
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            set_auto_spacing(p)
            add_inline(p, value, size_pt=CAPTION_PT)

        elif kind == "source":
            if bekasi:
                # Sumber inline sudah menyatu di caption ('Gambar N. ... (sumber: URL)');
                # baris sumber terpisah tetap dirender di bawah caption.
                p = doc.add_paragraph(style="Caption")
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                add_inline(p, value)
                continue
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            set_auto_spacing(p)
            add_inline(p, value)
            spacer = doc.add_paragraph()
            spacer.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            set_auto_spacing(spacer)

        elif kind == "table":
            spacer = doc.add_paragraph()
            spacer.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            set_auto_spacing(spacer)
            add_table(doc, value)
            spacer = doc.add_paragraph()
            spacer.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            set_auto_spacing(spacer)

        elif kind == "bullet":
            if bekasi:
                p = doc.add_paragraph(style="List Paragraph")
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                p.paragraph_format.left_indent = Inches(0)
                p.paragraph_format.first_line_indent = Inches(0)
                add_numbered(p, NUM_BULLET_ID)
                add_inline(p, value)
                prev_kind = kind
                continue
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            set_auto_spacing(p)
            add_numbered(p, NUM_BULLET_ID)

        elif kind == "number":
            if bekasi:
                p = doc.add_paragraph(style="List Paragraph")
                p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                p.paragraph_format.left_indent = Inches(0)
                p.paragraph_format.first_line_indent = Inches(0)
                add_numbered(p, num_id)
                add_inline(p, value)
                prev_kind = kind
                continue
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            set_auto_spacing(p)
            add_numbered(p, num_id)

        elif kind == "ref":
            if bekasi:
                # Arsip Bekasi: referensi numbered/bare URL, tanpa hyperlink aktif.
                p = doc.add_paragraph(style="List Paragraph")
                p.paragraph_format.left_indent = Inches(0)
                p.paragraph_format.first_line_indent = Inches(0)
                add_inline(p, value)
                prev_kind = kind
                continue
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            set_auto_spacing(p)
            add_inline(p, value)

        else:  # body
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            # Artikel acuan: paragraf diindent, kecuali yang diakhiri ':' atau tepat setelah daftar.
            if not (prev_kind in ("bullet", "number") or value.rstrip().endswith(":")):
                p.paragraph_format.first_line_indent = Inches(0.5)
            set_auto_spacing(p)
            add_inline(p, value)

        prev_kind = kind

    doc.save(out_path)


def main():
    import argparse
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("draft")
    ap.add_argument("output")
    ap.add_argument("--target", default="socs", choices=("socs", "bekasi"),
                    help="Target redaksi: socs (default, kertas A4) atau bekasi (kertas Letter)")
    args = ap.parse_args()
    build(args.draft, args.output, args.target)
    print(f"Tersimpan: {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
