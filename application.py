# -*- coding: utf-8 -*-
import sys


class Application:
    # Магический метод, который является инициализатором класса.
    def __init__(self, database, book) -> None:
        self.book = book
        self.database = database

    # Метод run запускает приложение
    def run(self) -> None:
        print("Добро пожаловать в приложение для управления базой данных книг!")
        print("Выберите одну из следующих опций:")
        print("1 - Добавить книгу")
        print("2 - Найти книгу")
        print("3 - Удалить книгу")
        print("4 - Редактировать данные о книге")
        print("5 - Вывести список всех книг")
        print("6 - Выход")
        choice = input("Ваш выбор: ")
        if choice == "1":
            self.add_book()
        elif choice == "2":
            self.find_book()
        elif choice == "3":
            self.delete_book()
        elif choice == "4":
            self.edit_book()
        elif choice == "5":
            self.get_all_books()
        elif choice == "6":
            self.exit()
        else:
            print("Неверный выбор, попробуйте еще раз.")
            self.run()

    # Метод add_book добавляет книгу в базу данных
    def add_book(self) -> None:
        title = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        year = input("Введите год издания книги: ")
        try:
            year = int(year)
        except ValueError:
            print("Год издания должен быть целым числом.")
            self.run()
        book = self.book(title, author, year)
        book_id = self.database.add_book(book)
        print(f"Книга {book} добавлена в базу данных под номером {book_id}.")
        self.run()

    # Метод find_book находит книгу в базе данных по заданным параметрам
    def find_book(self) -> None:
        title = input("Введите название книги или часть названия (оставьте пустым, если не знаете): ")
        author = input("Введите автора книги или часть автора (оставьте пустым, если не знаете): ")
        year = input("Введите год издания книги (оставьте пустым, если не знаете): ")
        if year:
            try:
                year = int(year)
            except ValueError:
                print("Год издания должен быть целым числом или пустой строкой.")
                self.run()
        else:
            year = None
        books = self.database.find_book(title, author, year)
        if books:
            print(f"Найдено {len(books)} книг(и) по вашему запросу:")
            for book in books:
                print(book)
        else:
            print("К сожалению, по вашему запросу ничего не найдено.")
        self.run()

    # Метод delete_book удаляет книгу из базы данных по заданным параметрам
    def delete_book(self) -> None:
        title = input("Введите название книги или часть названия (оставьте пустым, если не знаете): ")
        author = input("Введите автора книги или часть автора (оставьте пустым, если не знаете): ")
        year = input("Введите год издания книги (оставьте пустым, если не знаете): ")
        if year:
            try:
                year = int(year)
            except ValueError:
                print("Год издания должен быть целым числом или пустой строкой.")
                self.run()
        else:
            year = None
        deleted = self.database.delete_book(title, author, year)
        print(f"Удалено {deleted} книг(и) из базы данных.")
        self.run()

    # Метод edit_book редактирует данные о книге в базе данных по id книги
    def edit_book(self) -> None:
        book_id = input("Введите номер книги, данные о которой хотите изменить: ")
        try:
            book_id = int(book_id)
        except ValueError:
            print("Номер книги должен быть целым числом.")
            self.run()
        title = input("Введите новое название книги или оставьте пустым, если не хотите менять: ")
        author = input("Введите нового автора книги или оставьте пустым, если не хотите менять: ")
        year = input("Введите новый год издания книги или оставьте пустым, если не хотите менять: ")
        if year:
            try:
                year = int(year)
            except ValueError:
                print("Год издания должен быть целым числом или пустой строкой.")
                self.run()
        else:
            year = None
        self.database.edit_book(book_id, title, author, year)
        print(f"Данные о книге с номером {book_id} обновлены в базе данных.")
        self.run()

    # Метод get_all_books выводит список всех книг из базы данных
    def get_all_books(self) -> None:
        books = self.database.get_all_books()
        print(f"В базе данных находится {len(books)} книг(и):")
        for book in books:
            print(book)
        self.run()

    # Метод exit закрывает приложение и соединение с базой данных
    def exit(self) -> None:
        self.database.close()
        print("Спасибо за использование консольного приложения для управления базой данных книг\n.")
        sys.exit()
