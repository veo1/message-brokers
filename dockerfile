# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port RabbitMQ uses if necessary (5672 by default)
EXPOSE 5672

# Run the Python script when the container launches
CMD ["python", "message-broker.py"]
