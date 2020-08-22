# gcp_tools
This is a hash repo where you can find useful tools which can make your life better in GCP.
## s3_to_gcs
* This tool will sync s3 object created event to gcp pubsub, and a cloud function will be triggered by pubsub event, and pull the newly created s3 object with customized URL(CDN, cloudfront URL) and stored in GCS. 

## Sync AWS S3 object-created event from SNS to GCP PubSub
### Setting up the SNS topic
Create AWS SNS topic, set S3 object created event to SNS topic.
Copy the SNS topic ARN for later use.

### Create your Cloud Pub/Sub topic and subscription
```bash
gcloud pubsub topics create sns-events
gcloud pubsub subscriptions create sns-watcher --topic sns-events
```

### Go to folder sns2pubsub
Update expectedTopicArn in index.js with the ARN from last step.
```bash
npm init
npm install --save sns-validator
npm install --save --save-exact @google-cloud/pubsub
gcloud beta functions deploy receiveNotification --trigger-http --stage-bucket gs://<your-backet-name> --runtime nodejs8 --allow-unauthenticated
```
Copy the httpsTrigger URL in the output after the function deploys. You use the URL in the next step.

### Creating the SNS subscription
* In the AWS console, go to your SNS topic and create a subscription.
* Choose HTTPS as the protocol.
* Enter the Cloud Function URL that you copied earlier.
* Click Create Subscription.


## process pubsub message and transfer object from s3 to gcs

### Go to folder trans_s3_to_gcs
Update mail.py
* replace <your-base-url> with your s3 endpoint base URL or CDN base URL.
* replace <your-gcs-bucketname> with your destination bucket name.

```bash
gcloud beta functions deploy process_pubsub --trigger-topic <your-topic> --stage-bucket gs://<your-bucket-name> --runtime python37
```
