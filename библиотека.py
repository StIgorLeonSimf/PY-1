from typing import List, Optional, Tuple, Dict
from datetime import datetime, timedelta


class BookNotFoundException(Exception):
    """Книга не найдена"""


class BookLimitExceededException(Exception):
    """Читатель достиг лимита книг"""


class BookAlreadyBorrowedException(Exception):
    """Книга уже выдана"""


class ReaderNotFoundException(Exception):
    """Читатель не нгайден"""


class Book:
    """ Класс, представляющий книгу """

    def __init__(self, title: str, author: str, isbn: str, year: int):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__year = year
        self.__is_borrowed = False
        self.__borrowed_by: Optional['Reader'] = None
        self.__due_date: Optional[datetime] = None

    @property
    def title(self) -> str:
        return self.__title

    @property
    def author(self) -> str:
        return self.__author

    @property
    def isbn(self) -> str:
        return self.__isbn

    @property
    def year(self) -> int:
        return self.__year

    @property
    def is_borrowed_by(self) -> bool:
        return self.__is_borrowed_by

    @property
    def borrowed_by(self) -> Optional['Reader']:
        return self.__borrowed_by

    @property
    def due_date(self) -> Optional[datetime]:
        return self.__due_date

    def borrow(self, reader: 'Reader'):
        """Выдать книгу читателю."""
        if self.__is_borrowed_by:
            raise BookAlreadyBorrowedException(
                f'Книга {self.__title}  уже выдана!')
        self.__is_borrowed_by = True
        self.__borrowed_by = reader
        self.__due_date = datetime.now() + timedelta(days=14)

    def return_book(self) -> None:
        "Вернуть книгу в библиотеку."
        self.__is_borrowed_by = False
        self.__borrowed_by = None
        self.__due_date = None

    def __str__(self):
        status = 'Доступна' if not self.__is_borrowed else \
            f'Книга выдана {self.__borrowed_by.name}'
        return (f'{self.__title}, {self.__author}, '
                f' {self.__isbn}, {self.__year}) - {status}')

    def __repr__(self):
        return f'Book (title = {self.__title}, author = {self.__author}) '


class Reader:
    """Класс представляющий читателя."""
    MAX_BOOKS = 3

    def __init__(self, name: str, card_number: str):
        self.__name = name
        self.__card_number = card_number
        self.__borrowed_books: List[Book] = []

        @property
        def name(self) -> str:
            return self.__name

        @property
        def card_number(self) -> str:
            return self.__card_number

        @property
        def borrowed_books(self) -> List[Book]:
            """Возвращает копию списка для защиты инкапсуляции"""
            return self.__borrowed_books.copy()

        @property
        def borrowed_count(self) -> int:
            return len(self.__borrowed_books)

        def borrow_book(self, book: Book) -> None:
            """Взять книгу."""
            if len(self.__borrowed_books) >= Reader.MAX_BOOKS:
                raise BookLimitExceededException(f'{self.__name} Вы достигли предела в'
                                                 f'{Reader.MAX_BOOKS} книги')
            book.borrow()
            self.__borrowed_books.append(book)

        def return_books(self, book: Book) -> None:
            """Возврат книги."""
            if book in self.__borrowed_books:
                book.return_book()
                self.__borrowed_books.remove(book)

        def __str__(self):
            book_count = len(self.__borrowed_books)
            return (f'Читатель: {self.__name}, №{self.__card_number}, '
                    f'Книг на руках: {book_count}')

        def __repr__(self):
            return f'Читатель: (имя = {self.__name}, Читательский билет № {self.__card_number}) '