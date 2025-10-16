from kafka import KafkaProducer, KafkaConsumer
import json
import pickle
import time

# ---------- PRODUCER ----------
# Sends CDC events to Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Simulated CDC events (insert, update, delete)
cdc_events = [
    {'action':'INSERT','name':'David','value':400},
    {'action':'UPDATE','name':'Alice','value':250},
    {'action':'INSERT','name':'Eve','value':500},
    {'action':'UPDATE','name':'Bob','value':220},
    {'action':'UPDATE','name':'Charlie','value':350},
    {'action':'INSERT','name':'Frank','value':550},
    {'action':'UPDATE','name':'Alice','value':300},
    {'action':'UPDATE','name':'David','value':420},
    {'action':'DELETE','name':'Charlie','value':None},
    {'action':'INSERT','name':'Grace','value':600}
]

# Produce CDC events
for event in cdc_events:
    producer.send('cdc_topic', value=event)
    print(f"Produced: {event}")
    time.sleep(1)  # simulate real-time events

producer.flush()
producer.close()

# ---------- CONSUMER ----------
# Consume CDC events from Kafka and update model incrementally
consumer = KafkaConsumer(
    'cdc_topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    consumer_timeout_ms=1000
)

# Initial model and update counts
model = {'Alice':100, 'Bob':200, 'Charlie':300}
update_count = {k:1 for k in model.keys()}

for message in consumer:
    event = message.value
    action = event['action']
    name = event['name']
    value = event['value']

    if action == "INSERT":
        model[name] = value
        update_count[name] = 1
    elif action == "UPDATE":
        model[name] = value
        update_count[name] = update_count.get(name, 0) + 1
    elif action == "DELETE":
        model.pop(name, None)
        update_count.pop(name, None)

    print(f"Consumed Event: {action} {name} {value} -> Model: {model} | Counts: {update_count}")

# Save final model for persistence
with open("saved_model.pkl", "wb") as f:
    pickle.dump(model, f)

consumer.close()
