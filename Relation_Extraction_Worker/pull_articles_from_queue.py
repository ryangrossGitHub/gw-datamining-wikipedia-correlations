import boto3


def receive_message(sqs_region, sqs_url):
    sqs_client = boto3.client("sqs", region_name=sqs_region)
    response = sqs_client.receive_message(
        QueueUrl=sqs_url,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=10
    )

    return response.get("Messages", [])


def delete_message(receipt_handle, sqs_region, sqs_url):
    sqs_client = boto3.client("sqs", region_name=sqs_region)
    response = sqs_client.delete_message(
        QueueUrl=sqs_url,
        ReceiptHandle=receipt_handle
    )
    print(response)
