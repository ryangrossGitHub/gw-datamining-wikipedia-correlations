# Instructions
1. Create IAM roles for an EC2 instance to read from SQS and write to S3
2. Create an EC2 instance and give it the IAM role https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.html
3. Move folder contents to EC2
4. run ```sh run.sh```

## Notes
 - This is tested on the AWS linux distro
 - This instance needs ram or the OOM will kill it. Recommendation is >= 16 GB
 - Ensure you are creating things in the same region and VPC
 - Folder contents can be moved to EC2 via git clone or sftp