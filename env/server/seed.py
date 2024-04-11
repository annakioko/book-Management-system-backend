from random import choice
from faker import Faker

from app import app, db
from models import Author, Genre, Book, Reader

fake = Faker()

genres = ['fantasy', 'Romance', 'Fiction', 'comedy', 'thriller', 'action']


authors = []
for _ in range(20):
    author = Author(name=fake.first_name())
    authors.append(author)

genre_objects = []
for genre_name in genres:
    genre = Genre(name=genre_name)
    genre_objects.append(genre)


with app.app_context():
    db.session.add_all(genre_objects)
    db.session.commit()


books = []
for _ in range(20):
    author = choice(authors)
    genre = choice(genre_objects)
    book = Book(title=fake.sentence(), author=author, genre=genre)
    books.append(book)


readers = []
for _ in range(15):
    reader = Reader(name=fake.first_name())
    readers.append(reader)


with app.app_context():
    db.session.add_all(books)
    db.session.add_all(readers)
    db.session.commit()
