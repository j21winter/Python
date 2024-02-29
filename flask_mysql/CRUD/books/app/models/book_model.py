from app.config.mysqlconnection import connectToMySQL
from app.models import author_model

class Book:
    DB = 'books_schema'

    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors_list = []
    
    @classmethod
    def get_all(cls):
        query = '''
                SELECT *
                FROM books;
                '''
        results = connectToMySQL(cls.DB).query_db(query)
        all_books = []
        for book in results:
            all_books.append(cls(book))
        print(f'all books are: {all_books}')
        return all_books
    
    @classmethod
    def save(cls, data):
        query = '''
                INSERT
                INTO books(title, num_of_pages)
                VALUES (%(title)s, %(num_of_pages)s);
                '''
        return connectToMySQL(cls.DB).query_db(query,data)
    
    @classmethod
    def get_book_with_authors(cls, data):
        query = '''
                SELECT *
                FROM books
                LEFT JOIN favorites ON books.id = favorites.book_id
                LEFT JOIN authors ON favorites.author_id = authors.id
                WHERE books.id = %(id)s;
                '''
        results = connectToMySQL(cls.DB).query_db(query,data)
        print(f'results are:\n {results}')
        book = cls(results[0])
        for author in results:
            if author['authors.id'] == None:
                break
            author_data = {
                'id': author['authors.id'],
                'name': author['name'],
                'created_at': author['created_at'],
                'updated_at': author['updated_at'],
            }
            book.authors_list.append(author_model.Author(author_data))
        return book
    
    @classmethod
    def add_new_fave_author(cls, data):
        query = '''
                INSERT INTO favorites (author_id, book_id)
                VALUES (%(author_id)s, %(book_id)s);
                '''
        return connectToMySQL(cls.DB).query_db(query,data)