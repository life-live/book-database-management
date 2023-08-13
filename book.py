# -*- coding: utf-8 -*-

# Это дата класс. Дата классы это особые классы, которые зачастую используются для хранения данных.
class Book:
    # Магический метод, который является инициализатором класса.
    def __init__(self, number: int, title: str, author: str, year: int) -> None:
        """
        :param number: Number in the database
        :type number: int

        :param title: Title of the book
        :type title: str

        :param author: Author of the book
        :type author: str

        :param year: Year of publication of the book
        :type year: int
        """
        if not title or not author:
            raise ValueError("Название и автор книги не могут быть пустыми")
        self.number = number
        self.title = title
        self.author = author
        self.year = year

    # Магический метод __str__ возвращает строковое представление книги
    def __str__(self) -> str:
        return f"[{self.number}] {self.title} - {self.author} ({self.year})"
