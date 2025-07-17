# myproject/myapp/views.py
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def home(request):
    return render(request, 'home.html')

def health_check(request):
    return JsonResponse({'status': 'healthy', 'message': 'App is running!'})

@api_view(['GET'])
def api_hello(request):
    return Response({
        'message': 'Hello from Django REST API!',
        'status': 'success'
    })

@api_view(['GET', 'POST'])
def api_tasks(request):
    if request.method == 'GET':
        tasks = [
            {'id': 1, 'title': 'Learn Django', 'completed': False},
            {'id': 2, 'title': 'Deploy to AWS', 'completed': False},
            {'id': 3, 'title': 'Test API', 'completed': True}
        ]
        return Response({'tasks': tasks})
    
    elif request.method == 'POST':
        title = request.data.get('title')
        if title:
            new_task = {
                'id': 4,
                'title': title,
                'completed': False
            }
            return Response({'task': new_task}, status=status.HTTP_201_CREATED)
        return Response({'error': 'Title is required'}, status=status.HTTP_400_BAD_REQUEST)
