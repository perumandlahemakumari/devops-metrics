# Use official Python image as base
FROM python:3.9

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . .

# Expose Flask application port
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]

