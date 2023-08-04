from app import app
from flask import Flask, render_template, redirect, request
from app.models.author_model import Author
from app.models import book_model

@app.route('/')
def home():
    return redirect('/authors')


@app.route('/authors')
def authors():
    all_authors = Author.get_all()
    return render_template('authors.html', all_authors = all_authors)

@app.route('/authors/new', methods=['POST'])
def add_author():
    print(request.form)
    Author.save(request.form)
    return redirect('/authors')

@app.route('/authors/show/<int:id>')
def authors_show(id):
    data = {'id':id}
    author = Author.get_author_with_books(data)
    all_books = book_model.Book.get_all()
    print(f'sending Author: {author} \n Sending all books: {all_books}')
    for author_book in author.books_list:
        for book in all_books:
            if book.id == author_book.id:
                all_books.remove(book)
            else:
                pass
    return render_template('authors_show.html', author = author, all_books = all_books)

@app.route('/add/favorite', methods=['POST'])
def add_favorite_book():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book']
    }
    Author.add_new_fave(data)
    return redirect (f'/authors/show/{request.form["author_id"]}')