# api/__init__.py (empty file)

# api/admin.py
from django.contrib import admin
from .models import Book, Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'publication_date', 'pages')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('publication_date', 'created_at')

@admin.register(Author) 
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')

# api/apps.py
from django.apps import AppConfig

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

# api/migrations/__init__.py (empty file)