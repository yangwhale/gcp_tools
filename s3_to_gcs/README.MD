## Sync AWS S3 object created event from SNS to GCP PubSub
* Go to folder sns2pubsub
```bash
npm init
npm install --save sns-validator
npm install --save --save-exact @google-cloud/pubsub
gcloud beta functions deploy receiveNotification --trigger-http --stage-bucket gs://<your-backet-name> --runtime nodejs8 --allow-unauthenticated
```
