import fitz
import os

input_folder = "pdfs"
output_folder = "images_fitz"

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.endswith(".pdf"):
        filepath = os.path.join(input_folder, filename)
        doc = fitz.open(filepath)
        base_name = os.path.splitext(filename)[0]

        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            pix = page.get_pixmap(dpi=200)  # 200 DPI sifati yaxshi
            output_file = f"{base_name}_page_{page_num + 1:02}.jpg"
            output_path = os.path.join(output_folder, output_file)
            pix.save(output_path)
            print(f"Saved: {output_path}")
