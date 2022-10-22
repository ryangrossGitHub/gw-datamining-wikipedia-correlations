import boto3
import json
import os


def send_message(message, id, sqs_url, sqs_region):
    sqs_client = boto3.client("sqs", region_name=sqs_region)

    response = sqs_client.send_message(
        QueueUrl=sqs_url,
        MessageBody=json.dumps(message),
        MessageGroupId=id
    )
    print(response)


def push(directory, sqs_url, sqs_region):
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        content = open(directory + '/' + filename, encoding="utf8")
        json_array = json.load(content)

        for json_object in json_array:
            send_message(json_object, json_object['id'], sqs_url, sqs_region)
