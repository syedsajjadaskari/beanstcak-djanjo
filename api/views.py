from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http import JsonResponse
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
import os
import socket
import datetime


# Traditional Django view for the homepage
def home(request):
    return render(request, "home.html")


# API Health check endpoint
@api_view(["GET"])
def health_check(request):
    """
    Health check endpoint for load balancer monitoring
    """
    return Response(
        {
            "status": "healthy",
            "message": "Django REST API is running successfully!",
            "version": "1.0.0",
            "hostname": socket.gethostname(),
            "timestamp": datetime.datetime.now().isoformat(),
        }
    )


# System info endpoint for demo purposes
@api_view(["GET"])
def system_info(request):
    """
    Show system information - perfect for demonstrating load balancing
    """
    return Response({
        "hostname": socket.gethostname(),
        "deployment_platform": "AWS Elastic Beanstalk" if "elasticbeanstalk" in socket.gethostname().lower() else "Local Development",
        "environment": os.environ.get("ENVIRONMENT", "development"),
        "aws_region": os.environ.get("AWS_DEFAULT_REGION", "not set"),
        "timestamp": datetime.datetime.now().isoformat(),
        "server_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC"),
        "django_version": "4.2.7",
    })


# Load test endpoint for scaling demonstration
@api_view(["GET"])
def load_test(request):
    """
    Generate some CPU load to demonstrate auto-scaling
    """
    import time
    import random
    
    start_time = time.time()
    # Simulate some computational work
    result = sum(i * i for i in range(10000))
    processing_time = time.time() - start_time
    
    return Response({
        "message": "Load test completed",
        "hostname": socket.gethostname(),
        "processing_time_seconds": round(processing_time, 4),
        "result": result,
        "random_number": random.randint(1, 1000),
        "timestamp": datetime.datetime.now().isoformat(),
    })


# ViewSets for CRUD operations
class BookViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides default CRUD operations for Book model.
    Demonstrates REST API patterns in the cloud.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides default CRUD operations for Author model.
    Demonstrates REST API patterns in the cloud.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# Custom API endpoint
@api_view(["GET"])
def book_stats(request):
    """
    Get statistics about books in the database
    Perfect for demonstrating API functionality
    """
    total_books = Book.objects.count()
    total_pages = sum(book.pages for book in Book.objects.all())
    avg_pages = total_pages / total_books if total_books > 0 else 0

    return Response(
        {
            "total_books": total_books,
            "total_pages": total_pages,
            "average_pages": round(avg_pages, 2),
            "hostname": socket.gethostname(),
            "timestamp": datetime.datetime.now().isoformat(),
        }
    )