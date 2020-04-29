# gcp_tools
## s3_to_gcs
* This tool will sync s3 object created event to gcp pubsub, and a cloud function will be triggered by pubsub event, and pull the newly created s3 object with customized URL(CDN, cloudfront URL) and stored in GCS. 
