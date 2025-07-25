from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer

# Traditional Django view for the homepage
def home(request):
    return render(request, 'home.html')

# API Health check endpoint
@api_view(['GET'])
def health_check(request):
    """
    Simple health check endpoint
    """
    return Response({
        'status': 'healthy',
        'message': 'Django REST API is running successfully!',
        'version': '1.0.0'
    })

# ViewSets for CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions for Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions for Author model.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

# Custom API endpoint
@api_view(['GET'])
def book_stats(request):
    """
    Get statistics about books in the database
    """
    total_books = Book.objects.count()
    total_pages = sum(book.pages for book in Book.objects.all())
    avg_pages = total_pages / total_books if total_books > 0 else 0
    
    return Response({
        'total_books': total_books,
        'total_pages': total_pages,
        'average_pages': round(avg_pages, 2)
    })