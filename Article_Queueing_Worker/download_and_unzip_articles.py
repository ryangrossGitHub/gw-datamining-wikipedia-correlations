import os


def download(file_path, file_name, local_directory):
    os.system('mkdir ' + local_directory)
    os.system('aws s3 cp ' + file_path + file_name + ' ' + local_directory + '/.')


def unzip(file_name, local_directory):
    os.system('unzip ' + local_directory + '/' + file_name + ' -d ' + local_directory)
    os.system('rm ' + local_directory + '/' + file_name)