1. Data Preprocessing Challenge (preprocessing/README.md)
# Data Preprocessing Challenge

**Course:** Data Processing Techniques  
**Author:** Rithikka A  
**Date:** 16-Oct-2025  

## Aim
To preprocess IoT sensor datasets by:
- Handling missing values
- Fixing data type inconsistencies
- Removing duplicates
- Normalizing numerical data
- Feature engineering (Temperature-to-Humidity Ratio)

## Tools & Environment
- **Python:** 3.10
- **Apache Spark:** 3.5.0
- **PySpark:** 3.5.0
- **Pandas:** 2.1.1
- **NumPy:** 1.26.0
- **OS:** Ubuntu 22.04 LTS

## File Structure


preprocessing/
├── preprocessing.py
├── sample_data.csv
└── README.md


## Instructions
1. Install dependencies:
```bash
pip install -r requirements.txt


Run preprocessing script:

spark-submit preprocessing.py


The script performs:

Missing value handling

Duplicate removal

Normalization

Feature engineering

Sample Output
+---------+-----------+--------+--------+------+-------------------+---------------+-------------+--------------+
|sensor_id|temperature|humidity|pressure|status|timestamp          |temperature_norm|humidity_norm|temp_hum_ratio|
+---------+-----------+--------+--------+------+-------------------+---------------+-------------+--------------+
|S1       |25.3       |60.2    |1013    |ON    |2025-10-16 08:00:00|0.25           |0.6          |0.42          |
|S2       |26.8       |58.7    |1011    |OFF   |2025-10-16 08:01:00|0.27           |0.59         |0.46          |
|S3       |29.8       |59.63   |1012    |ON    |2025-10-16 08:02:00|0.3            |0.6          |0.5           |
+---------+-----------+--------+--------+------+-------------------+---------------+-------------+--------------+

Observations

Missing values replaced with column means.

Duplicates removed successfully.

Normalized data ready for ML tasks.

Feature temp_hum_ratio adds insight into temperature-humidity relationship.

Conclusion

The dataset is now clean and standardized, ready for downstream analytics or ML models.