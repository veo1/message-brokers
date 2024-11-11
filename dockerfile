# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5672 for RabbitMQ (if necessary for external connections)
EXPOSE 5672

# Define an environment variable to specify the default command to run
ENV FUNCTION_TO_RUN="send_message"

# Run the specified function (send_message or receive_messages)
CMD ["python", "-c", "import message-broker; getattr(message-broker, '${FUNCTION_TO_RUN}')()"]
