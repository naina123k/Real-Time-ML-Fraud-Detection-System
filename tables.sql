CREATE TABLE fraud_detection.transactions (
  transaction_id STRING,
  user_id STRING,
  amount FLOAT64,
  merchant STRING,
  prediction FLOAT64,
  is_fraud BOOL,
  event_time TIMESTAMP
)
PARTITION BY DATE(event_time);
