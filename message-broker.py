import pika
import logging
import signal
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def send_message():
    try:
        # Establish connection to RabbitMQ server (default localhost)
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        logging.info("Connection to RabbitMQ server established.")

        channel.queue_declare(queue='test_queue')
        logging.info("Queue 'test_queue' declared.")

        # Send the message 'Hello, World!' to 'test_queue'
        channel.basic_publish(exchange='',
                              routing_key='test_queue',
                              body='Hello, World!')
        logging.info("Message 'Hello, World!' sent to 'test_queue'.")

    except pika.exceptions.AMQPConnectionError as e:
        logging.error(f"Failed to connect to RabbitMQ server: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        if 'connection' in locals() and connection.is_open:
            connection.close()
            logging.info("Connection to RabbitMQ server closed.")

def receive_messages():
    connection = None
    channel = None
    
    # Define a signal handler to gracefully shut down the consumer
    def signal_handler(sig, frame):
        try:
            if channel:
                channel.stop_consuming()
            if connection and connection.is_open:
                connection.close()
            logging.info("Gracefully shutting down consumer")
        except OSError:
            # Socket already closed, we can safely exit
            logging.info("Consumer already shut down")
        sys.exit(0)
    
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    try:
        # Establish connection to RabbitMQ server (default localhost)
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        channel = connection.channel()
        logging.info("Connection to RabbitMQ server established.")

        channel.queue_declare(queue='test_queue')
        logging.info("Queue 'test_queue' declared.")

        # Define the callback function to handle incoming messages
        def callback(ch, method, properties, body):
            logging.info(f"Received message: {body.decode()}")
            print(f" [x] Received {body.decode()}")

        # Set up the consumer to listen for messages from 'test_queue'
        channel.basic_consume(queue='test_queue', on_message_callback=callback, auto_ack=True)
        logging.info("Consumer set up to listen for messages from 'test_queue'.")

        print(' [*] Waiting for messages. To exit press Ctrl+C')
        channel.start_consuming()

    except pika.exceptions.AMQPConnectionError as e:
        logging.error(f"Failed to connect to RabbitMQ server: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        if 'connection' in locals() and connection.is_open:
            connection.close()
            logging.info("Connection to RabbitMQ server closed.")

if __name__ == '__main__':
    send_message()
    receive_messages()
