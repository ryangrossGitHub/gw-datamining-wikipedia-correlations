import os


def push_to_s3(file_name, s3_path):
    os.system('aws s3 cp ' + file_name + ' ' + s3_path + '/' + file_name)