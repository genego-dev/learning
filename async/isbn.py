import asyncio
import httpx
import time


async def get_book_name(index: int, isbn: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}")
        response_dict = response.json()
        title = response_dict["items"][0]["volumeInfo"]["title"]
        print(f"{index}: {title}")


async def main():
    isbn_list = [
        9780007355143,
        9780008108298,
        9780547249643,
        9781405882583,
        9780316095860,
        9780930289232,
        9780486415871,
    ]

    task_list = []
    for index, isbn in enumerate(isbn_list):
        task_list.append(get_book_name(index, isbn))
    await asyncio.gather(*task_list)



if __name__ == "__main__":
    start_time = time.monotonic()
    asyncio.run(main())
    print(f"Time Taken:{time.monotonic() - start_time}")
