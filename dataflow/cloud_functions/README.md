## Real-Time ML Fraud Detection System (GCP)

A real-time fraud detection platform built using Pub/Sub, Dataflow, and
Vertex AI for low-latency transaction classification and automated alerts.

### Features
- Streaming ingestion via Pub/Sub
- Real-time ML inference using Vertex AI
- Automated alerting using Cloud Functions
- Scalable, cloud-native architecture

### Architecture
Pub/Sub → Dataflow → Vertex AI → BigQuery → Cloud Functions


flowchart LR
    A[Transaction Events] --> B[Pub/Sub]
    B --> C[Dataflow Streaming]
    C --> D[Vertex AI Endpoint]
    D --> E[Fraud Predictions]
    E --> F[BigQuery]
    E --> G[Cloud Functions Alerts]
