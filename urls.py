# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
]

# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('health/', views.health_check, name='health'),
    path('api/hello/', views.api_hello, name='api_hello'),
    path('api/tasks/', views.api_tasks, name='api_tasks'),
]
