from flask_app.config.mysqlconnection import connectToMySQL

class Book:
    def __init__(self, data):
            self.id = data['id']
            self.title = data['title']
            self.pages = data['pages']
            self.language = data['language']
            self.description = data['description']
            self.author_id = data['author_id']
            self.created_at = data['created_at']
            self.updated_at = data['updated_at']

    @classmethod
    def create_book( cls, data ):
        query = "INSERT INTO books (title, pages, language, description, author_id, created_at, updated_at) VALUES (%(title)s, %(pages)s, %(language)s, %(description)s, %(author_id)s, NOW(), NOW());"
        results = connectToMySQL('authors_books').query_db(query, data)
        return results