from kafka import KafkaProducer
import time
producer = KafkaProducer(bootstrap_servers="pkc-l7pr2.ap-south-1.aws.confluent.cloud:9092")
producer.send('lock', b'lock status')
print("produced to broker of kafka")
producer.flush()