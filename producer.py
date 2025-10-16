from kafka import KafkaProducer
import json, time, random

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

sensor_ids = ["S1","S2","S3","S4","S5"]

while True:
    temp = round(random.uniform(20,35),2)
    hum = round(random.uniform(40,80),2)
    status = "OFF" if temp > 30 else "ON"
    
    data = {
        "sensor_id": random.choice(sensor_ids),
        "temperature": temp,
        "humidity": hum,
        "status": status,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    producer.send('sensor_data', value=data)
    print(f"Produced: {data}")
    time.sleep(1)
