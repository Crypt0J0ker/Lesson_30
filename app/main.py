from kafka import KafkaConsumer, KafkaProducer
import time

def produce_message():
    producer = KafkaProducer(bootstrap_servers=['localhost:29092'])  # 👈 ВАЖНО
    message = b'hello Johnnie'
    producer.send('test-topic', message)
    
    producer.flush()
    print("Message sent: " + message.decode('utf-8'))

def consume_message():
    consumer = KafkaConsumer(
        'test-topic',
        bootstrap_servers=['localhost:29092'],  # 👈 ВАЖНО
        auto_offset_reset='earliest',
        consumer_timeout_ms=5000
    )
    for message in consumer:
        print("Message received: " + message.value.decode('utf-8'))
        time.sleep(1)

if __name__ == '__main__':
    produce_message()
    time.sleep(2)
    consume_message()
