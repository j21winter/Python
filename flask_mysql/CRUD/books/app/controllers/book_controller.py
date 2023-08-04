from app import app
from flask import Flask, render_template, redirect, request
from app.models.book_model import Book
from app.models import author_model

@app.route('/books')
def books():
    all_books = Book.get_all()
    return render_template('books.html', all_books = all_books)

@app.route('/books/new', methods=['POST'])
def add_book():
    print(request.form)
    Book.save(request.form)
    return redirect('/books')

@app.route('/books/show/<int:id>')
def books_show(id):
    data = {'id':id}
    book = Book.get_book_with_authors(data)
    all_authors = author_model.Author.get_all()
    print(f'sending books: {book} \n Sending all authors: {all_authors}')
    for author_fave in book.authors_list:
        for author in all_authors:
            if author.id == author_fave.id:
                all_authors.remove(author)
            else:
                pass
    return render_template('books_show.html', book = book, all_authors = all_authors)

@app.route('/add/favorite/book', methods=['POST'])
def add_favorite_author():
    data = {
        'author_id': request.form['author'],
        'book_id': request.form['book_id']
    }
    Book.add_new_fave_author(data)
    return redirect (f'/books/show/{request.form["book_id"]}')