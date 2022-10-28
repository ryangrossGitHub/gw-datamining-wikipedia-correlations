# Instructions
1. Create IAM roles for an EC2 instance to read S3 and write to SQS
2. Create an EC2 instance and give it the IAM role https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.html
3. Create a SQS Fifo Queue https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html
4. Move folder contents to EC2
5. run ```sh run.sh```

## Notes
 - EC2 should have >= 40GB
 - This is tested on the AWS linux distro with a t2.large
 - Ensure you are creating things in the same region and VPC
 - Folder contents can be moved to EC2 via git clone or sftp