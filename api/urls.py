from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'authors', views.AuthorViewSet)

urlpatterns = [
    # Homepage
    path('', views.home, name='home'),
    
    # API endpoints
    path('health/', views.health_check, name='health_check'),
    path('stats/', views.book_stats, name='book_stats'),
    
    # Include the router URLs
    path('', include(router.urls)),
]