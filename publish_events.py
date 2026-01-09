import json
import random
from google.cloud import pubsub_v1

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path("YOUR_PROJECT_ID", "transactions")

for i in range(100):
    event = {
        "transaction_id": f"tx_{i}",
        "user_id": f"user_{random.randint(1, 50)}",
        "amount": round(random.uniform(1, 5000), 2),
        "merchant": "online_store"
    }

    publisher.publish(
        topic_path,
        json.dumps(event).encode("utf-8")
    )

print("Events published")
