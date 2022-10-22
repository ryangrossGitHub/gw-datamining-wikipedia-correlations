from download_and_unzip_articles import download, unzip
from push_articles_to_queue import push

s3_file_path = 's3://ryangrossgwudatamining/'
file_name = 'enwiki20201020.zip'
local_unzip_directory = 'data'
sqs_url = 'https://sqs.us-east-1.amazonaws.com/991694008207/Articles.fifo'
sqs_region = 'us-east-1'

download(file_path=s3_file_path, file_name=file_name, local_directory=local_unzip_directory)
unzip(file_name=file_name, local_directory=local_unzip_directory)
push(directory=local_unzip_directory, sqs_url=sqs_url, sqs_region=sqs_region)
