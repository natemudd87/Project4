# Use Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY lexical_analyzer.py /app/
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 5000

# Command to run the application
CMD ["python", "lexical_analyzer.py"]
