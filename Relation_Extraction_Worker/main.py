from time import time
from create_ntuple_file import create_ntuple_file
from relationship_extractor import RelationShipExtractor
from push_to_s3 import push_to_s3
from pull_articles_from_queue import receive_message, delete_message
import os
import json

sqs_region = 'us-east-1'
sqs_url = 'https://sqs.us-east-1.amazonaws.com/991694008207/Articles.fifo'
s3_path = ' s3://ryangrossgwudatamining/extractions'

re = RelationShipExtractor()

text = 'Wood plays golf. Woods likes cars.'

def process_text(text):
    start = time()
    triples = []
    for sentence in text.split('.'):
        if sentence.strip():
            triples.append(re.run(sentence))

    file_name = create_ntuple_file(triples)
    push_to_s3(file_name=file_name, s3_path=s3_path)
    os.system('rm ' + file_name)

    end = time()
    print(end - start)

while True:
    try:
        for message in receive_message(sqs_region=sqs_region, sqs_url=sqs_url):
            text = json.loads(message['Body'])['text']
            process_text(text)
            delete_message(receipt_handle=message['ReceiptHandle'], sqs_region=sqs_region, sqs_url=sqs_url)
    except:
        print('Error processing message')

