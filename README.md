# gcp_tools

## Sync AWS S3 object created SNS to GCP PubSub
```bash
gcloud beta functions deploy receiveNotification --trigger-http --stage-bucket gs://<your-backet-name> --runtime nodejs8 --allow-unauthenticated
```
