# Instructions
1. Create IAM roles for an EC2 instance to read from SQS and write to S3
2. Create an EC2 instance and give it the IAM role https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/LaunchingAndUsingInstances.html
3. Move folder contents to EC2
4. run ```sh run.sh```

## Notes
 - This is tested on the AWS linux distro
 - This instance needs ram or the OOM will kill it. Recommendation is >= 8 GB
 - This instance needs >= 20 GB hard drive space for libraries and trained seq2seq model
 - Ensure you are creating things in the same region and VPC
 - Folder contents can be moved to EC2 via git clone or sftp
 - If you want to launch multiple EC2 instances at once you can enter the contents of the ec2_user_data.sh into the user data field in EC2 so that run.sh will auto launch on all the servers that get deployed. This prevents you from having to ssh into all the servers to start them.