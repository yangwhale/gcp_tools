import base64
import json
import requests
from google.cloud import storage

def process_pubsub(event, context):
   
    s3_base_url = "<your-base-url>"
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    s3_notification = json.loads(pubsub_message)
    s3_object = s3_notification["Records"][0]["s3"]["object"]["key"]
    print(s3_object)
    s3_object_url = s3_base_url + s3_object
    r = requests.get(s3_object_url)
    storage_client = storage.Client()
    bucket = storage_client.bucket("<your-gcs-bucketname>")
    blob = bucket.blob(s3_object)
    blob.upload_from_string(
        data=r.content,
        content_type='application/octet-stream',
        client=storage_client
    )
