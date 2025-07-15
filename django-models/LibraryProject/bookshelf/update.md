from bookshelf.models import Book

# Update the book's title

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Output:

# Book title updated to 'Nineteen Eighty-Four'
