import time
import requests
import multiprocessing

def pdf_to_images(start: int, end: int):
    total_images = 0
    for i in range(start, end):
        url = f'https://example.com/page_{i}.pdf'
        response = requests.get(url)
        with open(f'file1/image_{i+1}.jpg', 'wb') as f:
            f.write(response.content)
        print(f"{i+1}-sahifa rasm sifatida saqlandi!")
        total_images += 1
    return total_images

def main():
    started = time.time()
    start_range = 1
    end_range = 100
    step = (end_range - start_range) // 10
    pool = multiprocessing.Pool(processes=10)

    ranges = [
        (start_range + i * step, start_range + (i + 1) * step)
        for i in range(10)
    ]
    ranges[-1] = (ranges[-1][0], end_range)

    results = pool.starmap(pdf_to_images, ranges)

    total_images = sum(results)
    print(f"Jami saqlangan rasmlar: {total_images}")
    finished = time.time()
    print(f"{finished - started} sekund")

if __name__ == "__main__":
    main()
