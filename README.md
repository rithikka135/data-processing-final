# data-processing-final
Final Assessment Project for Data Processing Techniques: Preprocessing, Real-time Streaming, Incremental Updates, and In-Memory Analytics.
# Data Processing Techniques - Final Assessment

**Author:** Rithikka A  
**Roll No:** 23BCS135  
**Date:** 16-Oct-2025  

## Project Overview
This repository contains solutions for the **Data Processing Techniques Final Assessment**. The project covers four main tasks:

1. **Data Preprocessing Challenge** (30%)  
2. **Real-Time Data Streaming Challenge** (35%)  
3. **Incremental Data Processing Challenge** (25%)  
4. **In-Memory Data Processing Challenge** (10%)  

All tasks use Python along with tools like Apache Spark, Apache Kafka, and in-memory processing techniques to demonstrate efficient data handling, streaming, and analytics.

---

## Task 1: Data Preprocessing Challenge

**Objective:**  
Clean and preprocess IoT sensor data by handling missing values, fixing data type inconsistencies, removing duplicates, normalizing numerical data, and creating new engineered features.

**Tools & Technologies:**  
- Python 3.10  
- Apache Spark 3.5.0  
- PySpark 3.5.0  
- Pandas 2.1.1  
- NumPy 1.26.0  

**File:** `preprocessing/preprocessing.py`  

**Usage:**  
```bash
spark-submit preprocessing/preprocessing.py
Key Features:

Replaces missing values with column means

Removes duplicate entries

Normalizes temperature and humidity

Creates a temp_hum_ratio feature

Task 2: Real-Time Data Streaming Challenge
Objective:
Build a producer-consumer system using Apache Kafka that streams simulated IoT sensor data in real-time. Perform rolling averages, regression, and classification analytics on the streaming data.

Tools & Technologies:

Python 3.10

Apache Kafka 3.9.0

kafka-python 2.0.2

Scikit-learn 1.3.0

Pandas / NumPy

Files:

kafka_streaming/producer.py

kafka_streaming/consumer.py

Usage:

Start Kafka and Zookeeper

Create topic sensor_data

Run producer:

bash
Copy code
python3 kafka_streaming/producer.py
Run consumer:

bash
Copy code
python3 kafka_streaming/consumer.py
Key Features:

Simulates real-time sensor data streaming

Computes rolling averages

Predicts humidity using linear regression

Predicts sensor status (ON/OFF) using logistic regression

Task 3: Incremental Data Processing Challenge
Objective:
Implement incremental data updates using Change Data Capture (CDC). Update the model in response to inserts, updates, and deletes without retraining from scratch, maintaining online metrics such as accuracy, precision, recall, and F1-score.

Tools & Technologies:

Python 3.10

Apache Kafka / Kafka Connect (optional)

Apache Flink (optional)

Scikit-learn (for incremental model updates)

File: incremental_processing/cdc_simulation.py

Usage:

bash
Copy code
python3 incremental_processing/cdc_simulation.py
Key Features:

Tracks inserts, updates, and deletes in real-time

Updates model incrementally

Saves final model as saved_model.pkl

Calculates online metrics (accuracy, precision, recall, F1)

Task 4: In-Memory Data Processing Challenge
Objective:
Analyze sensor data efficiently using in-memory data structures. Perform insert, update, and delete operations, and compute metrics like average temperature and humidity while demonstrating performance improvement.

Tools & Technologies:

Python 3.10

Apache Spark / SAP HANA

In-memory data structures

File: in_memory/in_memory_processing.py

Usage:

bash
Copy code
python3 in_memory/in_memory_processing.py
Key Features:

Real-time insert, update, and delete operations

Computes average temperature and humidity dynamically

Demonstrates reduced computation time due to in-memory caching

Repository Structure
Copy code
data_processing_final/
├── preprocessing/
│   ├── preprocessing.py
│   └── README.md
├── kafka_streaming/
│   ├── producer.py
│   ├── consumer.py
│   └── README.md
├── incremental_processing/
│   ├── cdc_simulation.py
│   └── README.md
├── in_memory/
│   ├── in_memory_processing.py
│   └── README.md
├── requirements.txt
└── README.md
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
Install Python dependencies:

bash
Copy code
pip install -r requirements.txt
Ensure Apache Kafka and Apache Spark are installed and configured properly.

Notes
All Python scripts are compatible with Python 3.10.

Apache Spark is used for distributed computing and in-memory analytics.

Apache Kafka is used for real-time streaming.

The repository demonstrates integration of traditional data preprocessing, streaming analytics, incremental updates, and in-memory data processing techniques.

Author
Rithikka A
Bachelor of Engineering (CSE) - Kumaraguru College of Technology
Email: rithikka91@gmail.com

pgsql
Copy code

---

If you want, I can also **write the `requirements.txt`** to include all necessary Python packages for all four tasks in **one file**, ready to use for this repo.  

Do you want me to do that next?
