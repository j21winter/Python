from app.config.mysqlconnection import connectToMySQL
from app.models import book_model

class Author:
    DB = 'books_schema'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['created_at']
        self.books_list = []
    
    @classmethod
    def get_all(cls):
        query = '''
                SELECT *
                FROM authors;
                '''
        results = connectToMySQL(cls.DB).query_db(query)
        all_authors = []
        for author in results:
            all_authors.append(cls(author))
        return all_authors
    
    @classmethod
    def save(cls, data):
        query = '''
                INSERT
                INTO authors(name)
                VALUES (%(name)s);
                '''
        return connectToMySQL(cls.DB).query_db(query,data)
    
    @classmethod
    def get_author_with_books(cls, data):
        query = '''
                SELECT *
                FROM authors
                LEFT JOIN favorites ON authors.id = favorites.author_id
                LEFT JOIN books ON favorites.book_id = books.id
                WHERE authors.id = %(id)s;
                '''
        results = connectToMySQL(cls.DB).query_db(query,data)
        print(f'results are:\n {results}')
        author = cls(results[0])
        for book in results:
            if book['books.id'] == None:
                break
            book_data = {
                'id': book['books.id'],
                'title': book['title'],
                'num_of_pages': book['num_of_pages'],
                'created_at': book['created_at'],
                'updated_at': book['updated_at'],
            }
            author.books_list.append(book_model.Book(book_data))
        return author
    
    @classmethod
    def add_new_fave(cls, data):
        query = '''
                INSERT INTO favorites (author_id, book_id)
                VALUES (%(author_id)s, %(book_id)s);
                '''
        return connectToMySQL(cls.DB).query_db(query,data)
