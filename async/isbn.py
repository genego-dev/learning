import requests
import time


def print_book_name(index: int, isbn: int) -> str:
    response = requests.get(f"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}")
    response_dict = response.json()
    title = response_dict["items"][0]["volumeInfo"]["title"]
    print(f"{index}: {title}")


def main():
    isbn_list = [
        9780007355143,
        9780008108298,
        9780547249643,
        9781405882583,
        9780316095860,
        9780930289232,
        9780486415871,
        9780765350381,
    ]

    start_time = time.monotonic()
    for index, isbn in enumerate(isbn_list):
        print_book_name(index, isbn)

    print(f"Time Taken:{time.monotonic() - start_time}")


if __name__ == "__main__":
    main()
