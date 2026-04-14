import pymupdf4llm
import sys

print("Extracting...")
try:
    md_text = pymupdf4llm.to_markdown(r"c:\Users\w196818\work\JohnCompany\original-rules\John_Company_Rules_-BGG-_Final.pdf")
    with open(r"c:\Users\w196818\work\JohnCompany\extracted_rules.md", "w", encoding="utf-8") as f:
        f.write(md_text)
    print("Extraction complete.")
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
