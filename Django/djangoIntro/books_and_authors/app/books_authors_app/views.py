from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def index(request):
    context = {
        "all_books" : Book.objects.all()
    }
    return render(request, 'index.html', context)

def create_book(request):
    Book.objects.create(title = request.POST['title'], desc = request.POST['desc'])
    return redirect('/')

def show_book(request, book_id):
    context = {
        "book" : Book.objects.get( id = book_id), 
        "optional_authors": Author.objects.exclude(books__id = book_id)
    }

    return render(request, 'book.html', context)

def add_author(request):
    book = Book.objects.get(id = request.POST['book_id'])
    author = Author.objects.get(id = request.POST['author_id'])

    book.authors.add(author)

    return redirect(f"/book/{request.POST['book_id']}")

def all_authors(request):
    context = {
        "authors" : Author.objects.all()
    }

    return render(request, 'author_index.html', context)

def create_author(request):
    Author.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], notes = request.POST['notes'])

    return redirect('/authors')

def show_author(request, author_id):
    context = {
        "author" : Author.objects.get( id = author_id), 
        "optional_books" : Book.objects.exclude(authors__id = author_id)
    }

    return render(request, "author.html", context)

def add_book(request):
    book = Book.objects.get(id = request.POST['book_id'])
    author = Author.objects.get(id = request.POST['author_id'])

    author.books.add(book)
    print(request.POST['author_id'])

    return redirect(f"/author/{request.POST['author_id']}")