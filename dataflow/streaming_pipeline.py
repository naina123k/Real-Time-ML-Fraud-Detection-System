import apache_beam as beam
import json
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions
from google.cloud import aiplatform

PROJECT = "YOUR_PROJECT_ID"
REGION = "us-central1"
ENDPOINT_ID = "VERTEX_ENDPOINT_ID"

aiplatform.init(project=PROJECT, location=REGION)
endpoint = aiplatform.Endpoint(ENDPOINT_ID)

class PredictFraud(beam.DoFn):
    def process(self, element):
        data = json.loads(element.decode("utf-8"))

        prediction = endpoint.predict(
            instances=[[data["amount"]]]
        ).predictions[0][0]

        data["prediction"] = prediction
        data["is_fraud"] = prediction > 0.8
        yield data

options = PipelineOptions(
    project=PROJECT,
    region=REGION,
    temp_location="gs://YOUR_BUCKET/temp"
)
options.view_as(StandardOptions).streaming = True

with beam.Pipeline(options=options) as p:
    (
        p
        | "ReadPubSub" >> beam.io.ReadFromPubSub(
            subscription="projects/YOUR_PROJECT/subscriptions/transactions-sub"
        )
        | "PredictFraud" >> beam.ParDo(PredictFraud())
        | "WriteToBQ" >> beam.io.WriteToBigQuery(
            "fraud_detection.transactions",
            write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
        )
    )
