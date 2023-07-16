import csv
from typing import Dict


def get_from_csv(data_file: str) -> Dict:
    data = dict()

    with open(data_file, "r") as file:
        rows = csv.reader(file)
        prev_author = ""
        for author, title in rows:
            if not author:
                author = prev_author
            else:
                prev_author = author

            data[author] = title

    return data


# For testing
if __name__ == "_main__":
    books_file = "data/books.csv"
    books = get_from_csv(books_file)
    print(books)

    movies_file = "data/movies.csv"
    movies = get_from_csv(movies_file)
    print(movies)
