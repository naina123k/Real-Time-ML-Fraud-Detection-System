def fraud_alert(event, context):
    import base64
    import json

    data = json.loads(
        base64.b64decode(event["data"]).decode("utf-8")
    )

    if data.get("is_fraud"):
        print(f"🚨 FRAUD ALERT: {data['transaction_id']} | Amount: {data['amount']}")
