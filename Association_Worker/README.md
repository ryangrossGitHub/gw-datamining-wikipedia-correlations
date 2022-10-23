# Instructions
1. Create an AWS Neptune cluster with a Notebook https://docs.aws.amazon.com/neptune/latest/userguide/intro.html
2. Create IAM roles and trust relationships required for Neptune to be able to bulk load from S3 https://docs.aws.amazon.com/neptune/latest/userguide/bulk-load-tutorial-IAM.html
3. From the AWS Neptune Notebook run the bulk load command ```%load```
4. Fill in the form, making sure to select the S3 location that the Relation Extraction Workers pushed files to, choose the IAM role ARN from step #2, and choose the file format ```ntuples``` since that with what the RE Workers created.
5. Submit the load form and wait for completion.
6. Once data is loaded to Neptune, upload the Association_Miner notebook file.
7. Run the notebook to completion. The final output is a ranked list of associations.

## Notes
 - There are a lot of steps here, don't depend on this README to explain everything. Search for answers to problems in the AWS docs.
 - Tested on a db.r5.large Neptune instance
 - Tested on a ml.t3.medium Notebook instance