# -*- coding: utf-8 -*-
from application import Application
from database import Database
from book import Book


def main():
    # Вызов класса, отвечающего за работу с базой данных
    database = Database("database.sqlite", Book)
    # Вызов класса, отвечающего за основную работу консольного приложения
    app = Application(database=database, book=Book)
    # Вызов метода из класса app, который запускает само приложение
    app.run()


if __name__ == "__main__":
    main()
