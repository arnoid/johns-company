import fitz
import sys

try:
    doc = fitz.open(r'c:\Users\w196818\work\JohnCompany\original-rules\John_Company_Rules_-BGG-_Final.pdf')
    text = ""
    for page in doc:
        text += f"\n--- Page {page.number} ---\n"
        text += page.get_text()
    with open(r'c:\Users\w196818\work\JohnCompany\extracted_pymupdf.txt', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Done")
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
