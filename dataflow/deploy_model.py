from google.cloud import aiplatform

aiplatform.init(
    project="YOUR_PROJECT_ID",
    location="us-central1"
)

model = aiplatform.Model.upload(
    display_name="fraud-detection-model",
    artifact_uri="gs://YOUR_BUCKET/fraud_model",
    serving_container_image_uri=
    "us-docker.pkg.dev/vertex-ai/prediction/tf2-cpu.2-13:latest"
)

model.deploy(
    machine_type="n1-standard-4",
    min_replica_count=1,
    max_replica_count=2
)
