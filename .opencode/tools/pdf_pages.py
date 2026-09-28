from __future__ import annotations

import sys
from pathlib import Path

try:
    from pypdf import PdfReader
except Exception:
    print("ERROR: pypdf is not installed. Install it once with: pip install pypdf", file=sys.stderr)
    raise SystemExit(2)

def inside(child: Path, parent: Path) -> bool:
    try:
        child.relative_to(parent)
        return True
    except ValueError:
        return False

def main() -> int:
    if len(sys.argv) != 5:
        print("usage: pdf_pages.py <path> <start_page> <end_page> <max_chars>", file=sys.stderr)
        return 2
    cwd = Path.cwd().resolve()
    papers = (cwd / "Papers").resolve()
    requested = Path(sys.argv[1])
    pdf = requested.resolve() if requested.is_absolute() else (cwd / requested).resolve()
    if not inside(pdf, papers):
        print("ERROR: pdf_pages may read only files inside Papers/", file=sys.stderr)
        return 3
    if pdf.suffix.lower() != ".pdf":
        print("ERROR: requested file is not a PDF", file=sys.stderr)
        return 4
    if not pdf.exists():
        print(f"ERROR: file not found: {pdf}", file=sys.stderr)
        return 5
    start = int(sys.argv[2]); end = int(sys.argv[3]); max_chars = int(sys.argv[4])
    reader = PdfReader(str(pdf)); total = len(reader.pages)
    if start < 1 or end < start:
        print("ERROR: invalid page range", file=sys.stderr); return 6
    if start > total:
        print(f"ERROR: start page {start} exceeds PDF length ({total} pages)", file=sys.stderr); return 7
    end = min(end, total)
    if end - start + 1 > 4:
        print("ERROR: at most 4 pages may be extracted per call", file=sys.stderr); return 8
    out=[f"PDF: {pdf.relative_to(cwd)}",f"TOTAL_PAGES: {total}",f"REQUESTED_PAGES: {start}-{end}",""]
    used=sum(len(x)+1 for x in out); truncated=False; any_text=False
    for page_no in range(start,end+1):
        text=reader.pages[page_no-1].extract_text() or ""
        any_text = any_text or bool(text.strip())
        block=f"\n--- PAGE {page_no}/{total} ---\n{text.strip()}\n"
        remaining=max_chars-used
        if remaining<=0:
            truncated=True; break
        if len(block)>remaining:
            out.append(block[:remaining]); truncated=True; break
        out.append(block); used += len(block)
    if truncated:
        out.append("\n[TRUNCATED: output reached max_chars. Re-read a smaller page range.]")
    if not any_text:
        out.append("\n[WARNING: no extractable text was found. The PDF may be scanned.]")
    print("".join(out)); return 0

if __name__ == "__main__":
    raise SystemExit(main())
