# Use an official Python runtime as a parent image
FROM python:3.11.7-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    sqlite3 \
    pkg-config \
    libmariadb-dev-compat \
    libmariadb-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app/
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt \
    && pip3 install mysqlclient 

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define the command to run your app using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "stoplight.wsgi:application"]
