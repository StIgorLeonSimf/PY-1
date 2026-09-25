from typing import List, Optional, Tuple, Dict
from datetime import datetime, timedelta

from pandas.core.config_init import reader_engine_doc


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
    def is_borrowed(self) -> bool:
        return self.__is_borrowed

    @property
    def borrowed_by(self) -> Optional['Reader']:
        return self.__borrowed_by

    @property
    def due_date(self) -> Optional[datetime]:
        return self.__due_date

    def borrow(self, reader: 'Reader'):
        """Выдать книгу читателю."""
        if self.__is_borrowed:
            raise BookAlreadyBorrowedException(
                f'Книга {self.__title}  уже выдана!')
        self.__is_borrowed = True
        self.__borrowed_by = reader
        self.__due_date = datetime.now() + timedelta(days=14)

    def return_book(self) -> None:
        "Вернуть книгу в библиотеку."
        self.__is_borrowed = False
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
        book.borrow(self)
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


class Library:
    """Класс, представляющий библиотеку."""
    def __init__(self, name: str):
        self.__name = name
        self.__readers: Dict[str, Reader] = {}  # card_number: Reader
        self.__books: Dict[str, Book] = {}  # ISBN: Book

    @property
    def name(self) -> str:
        return self.__name

    def add_book(self, book: Book) -> None:
        """Добавить книгу в библиотеку."""
        if not isinstance(book, Book):
            raise TypeError('Добавить можно только объект класса Book')
        self.__books[book.isbn] = book

    def remove_book (self, isbn: str) -> None:
        """Удалить книгу из библиотеки."""
        if not isbn in self.__books:
            raise BookNotFoundException(f'Книга с ISBN {isbn} не найдена')

        book = self.__books[isbn]
        if book.is_borrowed_by:
            raise BookAlreadyBorrowedException(f'Книга {book.title} выдана читателю')

        del self.__books[isbn]

    def register_reader(self, reader: Reader) -> None:
        """Регистрация нового читателя."""
        if not isinstance(reader, Reader):
            raise TypeError('Добавить можно только объект класса Reader')
        self.__readers[reader.card_number] = reader

    def unregister_reader(self, card_number: str) -> None:
        """ Удалить читателя из библиотеки."""
        if not card_number in self.__readers:
            raise ReaderNotFoundException(f'Читатель с номером  {card_number} отсутствует')
        reader = self.__readers[card_number]

        if reader.borrowed_count > 0:
            raise Exception(f'Запрет. У читателя {reader.name} не сданы книги.')
        del self.__readers[card_number]

    def borrow_book(self, card_number: str, isbn: str) -> None:
        """Выдать книгу читателю."""
        # Проверка книги
        if not isbn in self.__books:
            raise BookNotFoundException(f'Книга с {isbn} не найдена')

        # Проверка читателя
        if not card_number in self.__readers:
            raise ReaderNotFoundException(f'Читатель с {card_number} не найден.')

        reader = self.__readers[card_number]
        book = self.__books[isbn]

        reader.borrow_book(book)
        print(f'Книга {book.title} выдана {reader.name}')

    def return_book(self, card_number: str, isbn: str) -> None:
        """Вернуть книгу в библиотеку."""

        # Проверка книги
        if not isbn in self.__books:
            raise BookNotFoundException(f'Книга с {isbn} не найдена')

        # Проверка читателя
        if not card_number in self.__readers:
            raise ReaderNotFoundException(f'Читатель с {card_number} не найден.')

        reader = self.__readers[card_number]
        book = self.__books[isbn]

        reader.return_books(book)
        print(f'Книга {book.title} возвращена читателем {reader.name}')

    def get_available_books(self) -> List[Book]:
        """Список доступных книг."""
        return [book for book in self.__books.values() if not book.is_borrowed]

    def get_debitors(self) -> List[Reader]:
        """Получить список читателей не вернувших книги вовремя"""
        debitors = []
        now = datetime.now()
        for reader in self.__readers.values():
            over_books = [book for book in reader.borrowed_books
                          if book.due_date and book.due_date < now]

            if over_books:
                debitors.append(reader)
        return debitors

    def __str__(self) -> str:
        total_book = len(self.__books)
        available_books = len(self.get_available_books())
        total_readers = len(self.__readers)

        return (f'Библиотека: {self.__name}\n'
                f'Всего книг: {total_book}\n'
                f'Доступных книг: {available_books}\n'
                f'Всего читателей: {total_readers}')


if __name__ == '__main__':
    # Создаем библиотеку
    library = Library('Городская библиотека')

    # Создаем книги
    book1 = Book("Война и мир", 'Лев Толстой', '978-5-17-123456-2', 1869)
    book2 = Book("Преступление и наказание", 'Федор Достоевский', '978-5-17-654321-1', 1866)
    book3 = Book('Мастер и Маргарита','Михаил Булгаков','978-5-17-321567-1',1967)
    book4 = Book('Анна Каренина','Лев Толстой','978-5-17-987123-1',1877)

    # Добавляем книги в библиотеку
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)

    # Регистрация читателей
    reader1 = Reader('Иван Иванов', 'LIB-001')
    reader2 = Reader('Петр Петров', 'LIB-002')
    reader3 = Reader('Александра Александорова', 'LIB-003')

    library.register_reader(reader1)
    library.register_reader(reader2)
    library.register_reader(reader3)

    # Выдаем книги
    try:
        library.borrow_book('LIB-001', '978-5-17-654321-1')
        library.borrow_book('LIB-001', '978-5-17-321567-1')
        library.borrow_book('LIB-003', '978-5-17-123456-2')
        # пробуем взять то что выдано
        library.borrow_book('LIB-002', '978-5-17-123456-2')


    except BookAlreadyBorrowedException as err:
        print(f'Ошибка: {err}')
    except BookLimitExceededException as err:
        print(f'Ошибка: {err}')

    # Смотрим доступные книги
    print('Доступные книги:')
    for book in library.get_available_books():
        print(book)

    # Возврат книги
    # library.return_book('LIB-001', '978-5-17-321567-1')

    print(library)

    print(reader1)
    print(f'Книги на руках: {', '.join([book.title for book in reader1.borrowed_books])}')
