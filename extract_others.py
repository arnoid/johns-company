import fitz
import sys
import os

files = [
    r'c:\Users\w196818\work\JohnCompany\original-rules\DrBo6s_Cheat_Sheet_for_John_Company_v13_-_Booklet.pdf',
    r'c:\Users\w196818\work\JohnCompany\original-rules\John_Company_Second_Edition_Reference.pdf'
]

for fpath in files:
    try:
        name = os.path.basename(fpath).replace('.pdf', '.txt')
        out_path = os.path.join(r'c:\Users\w196818\work\JohnCompany', f"extracted_{name}")
        doc = fitz.open(fpath)
        text = ""
        for page in doc:
            text += f"\n--- Page {page.number} ---\n"
            text += page.get_text()
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Extracted {fpath} to {out_path}")
    except Exception as e:
        print(f"Error extracting {fpath}: {e}", file=sys.stderr)
