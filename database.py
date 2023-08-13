# -*- coding: utf-8 -*-
import sqlite3


# Создаем класс Database, который будет представлять базу данных книг
class Database:
    # Магический метод, который является инициализатором класса.
    def __init__(self, filename, book) -> None:
        self.book = book
        self.connection = sqlite3.connect(filename)
        self.cursor = self.connection.cursor()
        self.create_database()

    # Метод create_database создает базу данных, есл ее нет
    def create_database(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER)""")
        self.connection.commit()

    # Метод add_book принимает объект книги и добавляет его в базу данных
    def add_book(self, book):
        self.cursor.execute("""INSERT INTO books (title, author, year) VALUES (?, ?, ?)""",
                            (book.title, book.author, book.year))
        self.connection.commit()
        return self.cursor.lastrowid

    # Метод find_book принимает параметры поиска (название, автор, год издания) и возвращает список книг из базы данных
    def find_book(self, title=None, author=None, year=None) -> list:
        condition = []
        parameters = []
        if title:
            condition.append("title LIKE ?")
            parameters.append(f"%{title}%")
        if author:
            condition.append("author LIKE ?")
            parameters.append(f"%{author}%")
        if year:
            condition.append("year = ?")
            parameters.append(year)
        if not condition:
            return []
        query = f"SELECT * FROM books WHERE {' AND '.join(condition)}"
        self.cursor.execute(query, parameters)
        result = self.cursor.fetchall()
        books = [self.book(row[0], row[1], row[2], row[3]) for row in result]
        return books

    # Метод delete_book принимает параметры поиска (название, автор, год издания) и удаляет ее из базы данных
    def delete_book(self, title=None, author=None, year=None) -> None:
        condition = []
        parameters = []
        if title:
            condition.append("title LIKE ?")
            parameters.append(f"%{title}%")
        if author:
            condition.append("author LIKE ?")
            parameters.append(f"%{author}%")
        if year:
            condition.append("year = ?")
            parameters.append(year)
        if not condition:
            return
        query = f"DELETE FROM books WHERE {' AND '.join(condition)}"
        self.cursor.execute(query, parameters)
        self.connection.commit()
        count_del = self.cursor.execute("SELECT changes();")
        return count_del.fetchone()[0]

    # Метод edit_book принимает id книги и данные о книге (название, автор, год издания)
    # и обновляет данные в базе данных
    def edit_book(self, book_id, title=None, author=None, year=None):
        fields = []
        values = []
        if title:
            fields.append("title = ?")
            values.append(title)
        if author:
            fields.append("author = ?")
            values.append(author)
        if year:
            fields.append("year = ?")
            values.append(year)
        if not fields:
            return
        values.append(book_id)
        query = f"UPDATE books SET {', '.join(fields)} WHERE id = ?"
        self.cursor.execute(query, values)
        self.connection.commit()

    # Метод get_all_books возвращает список всех книг из базы данных
    def get_all_books(self) -> list:
        self.cursor.execute("SELECT * FROM books")
        result = self.cursor.fetchall()
        books = [self.book(row[0], row[1], row[2], row[3]) for row in result]
        return books

    # Метод close закрывает соединение с базой данных
    def close(self) -> None:
        self.connection.close()

    # Магический метод, который вызывается при завершении работы интерпретатора, он вызывает метод close
    def __del__(self):
        self.close()
