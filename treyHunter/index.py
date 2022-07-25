from datetime import date
import datetime


class Books:
    def __init__(self, title: str, author: str, year: int) -> None:
        self.title = title
        self.author = author
        self.year = year

    def __str__(self) -> str:
        return "All books"

    @property
    def getAge(self) -> int:
        return 'datetime.date(date.today())'


# print(dir(Books))
book = Books("James", "Mike", 1990)
print(book.getAge)
