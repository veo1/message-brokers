# RabbitMQ Messaging Example

This project demonstrates basic messaging between a Python script and a RabbitMQ server using the `pika` library. The script includes two main functions: one for sending messages to a queue (`test_queue`) and another for receiving messages from the queue. This setup is Dockerized for easy deployment and configuration.

## Getting Started

### Prerequisites

- Python 3.7 or later (for local installation)
- `pip` for package installation
- Docker (for running the script in a container)
- RabbitMQ running locally or in a container

### Installation

#### Running Locally

1. **Clone the repository**:

   ```bash
   git clone https://github.com/veo1/message-brokers.git
   cd <message-brokers>
    ```

2. **Set up a virtual environment (recommended)**:

    ```bash
    python -m venv venv
    source venv/bin/activate   # On macOS and Linux
    venv\Scripts\activate      # On Windows
    ```

3. **Install required packages**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Running the application**:

To send a default message:
    ```bash
    python message-broker.py 
    ```

#### Using Docker

Alternatively, you can run the API in a Docker container.
1. **Build the Docker image**:

    ```bash
    docker build -t message-broker .
    ```
2. **Run the Docker image**: 
To send a default message:
    ```bash
    docker run --rm  message-broker
    ```

### Using the Script

You can test the script by running the the script which automatically sends a default "Hello World" message to the queue.


### Directory Structure

    ```plaintext
    ├── message-broker.py   # Main Python script containing send and receive functions
    ├── requirements.txt    # List of Python dependencies
    ├── Dockerfile          # Docker configuration file (optional)
    ├── README.md           # Documentation file
    └── message-broker.gif  # GIF of the application running
    ```

#### File Descriptions

- `message-broker.py`: Contains the RabbitMQ message sender and receiver functions.
- `requirements.txt`: List of Python dependencies.
- `Dockerfile`: Docker configuration file.
- `README.md`: Documentation file.
- `message-broker.gif`: GIF of the application running.