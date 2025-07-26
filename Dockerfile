# Simple Dockerfile for Django REST API
# This creates a container that runs our Django application

# Step 1: Use Python 3.11 as our base image
FROM python:3.11-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy our requirements file and install Python packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Step 4: Copy all our project files into the container
COPY . .

# Step 5: Set up the database and static files
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Step 6: Tell Docker which port our app uses
EXPOSE 8000

# Step 7: Command to run when container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]