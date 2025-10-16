## **3. Incremental Data Processing Challenge (`incremental_processing/README.md`)**

```markdown
# Incremental Data Processing Challenge

**Course:** Data Processing Techniques  
**Author:** Rithikka A  
**Date:** 16-Oct-2025  

## Objective
Implement Incremental Data Processing using Change Data Capture (CDC):
- Track inserts, updates, and deletes in real-time
- Update models incrementally
- Maintain online metrics (Accuracy, Precision, Recall, F1-score)

## Tools & Technologies
- Python (Simulated CDC)
- Apache Kafka / Kafka Connect (optional in real deployment)
- Apache Flink (optional)
- Scikit-learn (incremental updates)
- Pickle for persistence

## File Structure
incremental_processing/
├── cdc_simulation.py
└── README.md

markdown
Copy code

## Instructions
1. Run CDC simulation:
```bash
python3 cdc_simulation.py
The script will:

Process insert/update/delete events

Update the model dictionary

Display updated counts and online metrics

Save final model as saved_model.pkl

Observations
Incremental updates only affect changed records

Metrics improve as more events are processed

Delete events remove records and maintain consistency