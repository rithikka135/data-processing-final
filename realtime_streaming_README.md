## **2. Real-Time Data Streaming Challenge (`kafka_streaming/README.md`)**

```markdown
# Real-Time Data Streaming Challenge

**Course:** Data Processing Techniques  
**Author:** Rithikka A  
**Date:** 16-Oct-2025  

## Aim
To create a real-time streaming application using Apache Kafka and Python:
- Produce simulated IoT sensor data
- Consume data in real-time
- Perform analytics:
  - Rolling averages
  - Regression prediction
  - Classification prediction

## Tools & Environment
- **Python:** 3.10
- **Kafka:** 3.9.0
- **kafka-python:** 2.0.2
- **Scikit-learn:** 1.3.0
- **Pandas / NumPy:** 2.1.1 / 1.26.0
- **OS:** Ubuntu 22.04 LTS

## File Structure
kafka_streaming/
├── producer.py
├── consumer.py
└── README.md

bash
Copy code

## Kafka Setup
1. Start Zookeeper:
```bash
bin/zookeeper-server-start.sh config/zookeeper.properties
Start Kafka broker:

bash
Copy code
bin/kafka-server-start.sh config/server.properties
Create topic:

bash
Copy code
bin/kafka-topics.sh --create --topic sensor_data --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
Instructions
Run producer to send simulated sensor data:

bash
Copy code
python3 producer.py
Run consumer to process real-time data:

bash
Copy code
python3 consumer.py
Observe rolling averages, predicted humidity, and sensor status in terminal.

Observations
Kafka streams IoT data in real-time.

Rolling averages smooth fluctuations.

Regression predicts humidity from temperature.

Classification predicts sensor status ON/OFF.