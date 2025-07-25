#!/usr/bin/env python3
"""
API Testing Script for Django REST API Demo
This script tests all the API endpoints after deployment
"""

import requests
import json
import sys

def test_api(base_url):
    """Test all API endpoints"""
    
    print(f"🧪 Testing API at: {base_url}")
    print("=" * 50)
    
    # Test health check
    print("1. Testing health check endpoint...")
    try:
        response = requests.get(f"{base_url}/health/")
        if response.status_code == 200:
            print("✅ Health check passed")
            print(f"   Response: {response.json()}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Health check error: {e}")
    
    print("\n" + "-" * 30)
    
    # Test books endpoint
    print("2. Testing books endpoint...")
    try:
        response = requests.get(f"{base_url}/books/")
        if response.status_code == 200:
            print("✅ Books GET endpoint working")
            data = response.json()
            print(f"   Found {data.get('count', 0)} books")
        else:
            print(f"❌ Books GET failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Books GET error: {e}")
    
    # Test creating a book
    print("\n3. Testing book creation...")
    book_data = {
        "title": "Test Book",
        "author": "Test Author",
        "isbn": "1234567890123",
        "publication_date": "2024-01-01",
        "pages": 200
    }
    
    try:
        response = requests.post(
            f"{base_url}/books/",
            json=book_data,
            headers={'Content-Type': 'application/json'}
        )
        if response.status_code == 201:
            print("✅ Book creation successful")
            created_book = response.json()
            print(f"   Created book ID: {created_book.get('id')}")
            
            # Test getting the created book
            book_id = created_book.get('id')
            if book_id:
                print(f"\n4. Testing get specific book (ID: {book_id})...")
                response = requests.get(f"{base_url}/books/{book_id}/")
                if response.status_code == 200:
                    print("✅ Get specific book successful")
                else:
                    print(f"❌ Get specific book failed: {response.status_code}")
        else:
            print(f"❌ Book creation failed: {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"❌ Book creation error: {e}")
    
    print("\n" + "-" * 30)
    
    # Test authors endpoint
    print("5. Testing authors endpoint...")
    try:
        response = requests.get(f"{base_url}/authors/")
        if response.status_code == 200:
            print("✅ Authors GET endpoint working")
            data = response.json()
            print(f"   Found {data.get('count', 0)} authors")
        else:
            print(f"❌ Authors GET failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Authors GET error: {e}")
    
    # Test creating an author
    print("\n6. Testing author creation...")
    author_data = {
        "name": "Test Author",
        "email": "test@example.com",
        "bio": "A test author for API testing"
    }
    
    try:
        response = requests.post(
            f"{base_url}/authors/",
            json=author_data,
            headers={'Content-Type': 'application/json'}
        )
        if response.status_code == 201:
            print("✅ Author creation successful")
            created_author = response.json()
            print(f"   Created author ID: {created_author.get('id')}")
        else:
            print(f"❌ Author creation failed: {response.status_code}")
            print(f"   Response: {response.text}")
    except Exception as e:
        print(f"❌ Author creation error: {e}")
    
    print("\n" + "-" * 30)
    
    # Test stats endpoint
    print("7. Testing stats endpoint...")
    try:
        response = requests.get(f"{base_url}/stats/")
        if response.status_code == 200:
            print("✅ Stats endpoint working")
            stats = response.json()
            print(f"   Stats: {stats}")
        else:
            print(f"❌ Stats endpoint failed: {response.status_code}")
    except Exception as e:
        print(f"❌ Stats endpoint error: {e}")
    
    print("\n" + "=" * 50)
    print("🎉 API testing completed!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python test_api.py <base_url>")
        print("Example: python test_api.py http://your-app.us-east-1.elasticbeanstalk.com")
        sys.exit(1)
    
    base_url = sys.argv[1].rstrip('/')
    test_api(base_url)