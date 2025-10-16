from kafka import KafkaConsumer
import json
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression

consumer = KafkaConsumer(
    'sensor_data',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    consumer_timeout_ms=1000
)

window_size = 5
temp_window, hum_window, status_window = [],[],[]

reg_model = LinearRegression()
clf_model = LogisticRegression()

for message in consumer:
    data = message.value
    temp = data['temperature']
    hum = data['humidity']
    status = 1 if data['status']=="ON" else 0

    temp_window.append(temp)
    hum_window.append(hum)
    status_window.append(status)

    if len(temp_window) > window_size:
        temp_window.pop(0)
        hum_window.pop(0)
        status_window.pop(0)

    avg_temp = round(np.mean(temp_window),2)
    avg_hum = round(np.mean(hum_window),2)

    # Regression
    X_reg = np.array(temp_window).reshape(-1,1)
    y_reg = np.array(hum_window)
    reg_model.fit(X_reg, y_reg)
    pred_hum = round(reg_model.predict([[temp]])[0],2)

    # Classification
    X_clf = np.array(list(zip(temp_window,hum_window)))
    y_clf = np.array(status_window)
    pred_status = "Unknown"
    if len(X_clf) >= 2:
        clf_model.fit(X_clf, y_clf)
        pred_status = "ON" if clf_model.predict([[temp,hum]])[0]==1 else "OFF"

    print(f"Consumed: {data}")
    print(f"Rolling Avg Temp: {avg_temp} | Rolling Avg Hum: {avg_hum}")
    print(f"Predicted Humidity: {pred_hum}")
    print(f"Predicted Status: {pred_status}")
    print("="*80)
