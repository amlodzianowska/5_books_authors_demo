from flask_app.config.mysqlconnection import connectToMySQL


class Author:

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_author(cls, data):
        query = "INSERT INTO authors (first_name, last_name, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, NOW(), NOW());"
        results = connectToMySQL('authors_books').query_db(query, data)
        return results

    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL('authors_books').query_db(query)
        authors = []
        for author in results:
            authors.append( cls(author))
        return results