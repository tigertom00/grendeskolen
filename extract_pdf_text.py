import sys
from pathlib import Path
from PyPDF2 import PdfReader

def extract_text(pdf_path, out_path=None):
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        print(f"File not found: {pdf_path}")
        return
    reader = PdfReader(str(pdf_path))
    text = ""
    for i, page in enumerate(reader.pages):
        page_text = page.extract_text()
        text += f"\n----- PAGE {i+1} -----\n"
        text += page_text if page_text else "[NO TEXT FOUND]\n"
    if out_path:
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Text extracted to {out_path}")
    else:
        print(text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_pdf_text.py <pdf_file> [output_txt_file]")
        sys.exit(1)
    pdf_file = sys.argv[1]
    out_file = sys.argv[2] if len(sys.argv) > 2 else None
    extract_text(pdf_file, out_file)
