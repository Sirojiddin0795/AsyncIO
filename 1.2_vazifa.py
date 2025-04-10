import asyncio
import os
import fitz

input_folder = "pdfs"
output_folder = "images_fitz_async"

os.makedirs(output_folder, exist_ok=True)

async def convert_pdf(pdf_path):
    loop = asyncio.get_event_loop()
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]

    def sync_convert():
        doc = fitz.open(pdf_path)
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            pix = page.get_pixmap(dpi=200)
            output_file = f"{base_name}_page_{page_num + 1:02}.jpg"
            output_path = os.path.join(output_folder, output_file)
            pix.save(output_path)
            print(f"[Async] Saved: {output_path}")

    await loop.run_in_executor(None, sync_convert)

async def main():
    tasks = []

    for file in os.listdir(input_folder):
        if file.endswith(".pdf"):
            full_path = os.path.join(input_folder, file)
            tasks.append(convert_pdf(full_path))

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
