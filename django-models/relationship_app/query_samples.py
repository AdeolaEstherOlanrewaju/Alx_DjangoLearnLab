import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author_name = "Chinua Achebe"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = author.books.all()
    print(f"Books by {author_name}: {[book.title for book in books_by_author]}")
except Author.DoesNotExist:
    print(f"Author '{author_name}' not found.")

# List all books in a library
library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    library_books = library.books.all()
    print(f"Books in {library_name}: {[book.title for book in library_books]}")
except Library.DoesNotExist:
    print(f"Library '{library_name}' not found.")

# Retrieve the librarian for a library
try:
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(f"Librarian for {library_name}: {librarian.name}")
except Library.DoesNotExist:
    print(f"Library '{library_name}' not found.")
except Librarian.DoesNotExist:
    print(f"No librarian assigned to '{library_name}'.")
