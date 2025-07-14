from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')       # Show these fields in the list view
    list_filter = ('publication_year',)                          # Enable filtering by year
    search_fields = ('title', 'author')                          # Enable search by title or author
