import asyncio
import aiohttp
import aiofiles
import sqlite3
import time
import os

os.makedirs("files_100", exist_ok=True)

async def get_pdf_from_url(session, name: str, url: str):
    try:
        async with session.get(url) as response:
            content = await response.text()

            index = content.find('href="/public/uploads/')
            if index != -1:
                start_url = index + 6
                end_url = content.find('.pdf"') + 4
                pdf_url = f"https://vexillum.uz{content[start_url:end_url]}"

                async with session.get(pdf_url) as pdf_response:
                    if pdf_response.status == 200:
                        file_path = f"files_100/{name}.pdf"
                        async with aiofiles.open(file_path, "wb") as file:
                            await file.write(await pdf_response.read())
                        print(f"{name}.pdf has been downloaded")
                    else:
                        print(f"Failed to download {name}.pdf from {pdf_url}")
            else:
                print(f"{name} not found in url {url}")
    except Exception as e:
        print(f"Error downloading {name}: {e}")


async def main():
    started_at = time.time()

    with sqlite3.connect('standards.db') as conn:
        c = conn.cursor()
        sql = "SELECT name, link FROM standards WHERE has_pdf=1 LIMIT 100;"
        rows = c.execute(sql).fetchall()

    async with aiohttp.ClientSession() as session:
        tasks = [
            get_pdf_from_url(session, name, url)
            for name, url in rows
        ]
        await asyncio.gather(*tasks)

    finished_at = time.time()
    print(f"Finished in {finished_at - started_at:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())
