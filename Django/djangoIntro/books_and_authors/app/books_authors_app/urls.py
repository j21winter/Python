from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('book/new', views.create_book),
    path('book/<int:book_id>', views.show_book),
    path('book/update', views.add_author),
    path('authors', views.all_authors),
    path('author/new', views.create_author),
    path('author/<int:author_id>', views.show_author),
    path('author/update', views.add_book)
]