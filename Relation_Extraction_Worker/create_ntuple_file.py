import uuid
import urllib.parse


def create_ntuple_file(triples):
    file_name = str(uuid.uuid4()) + '.nt'
    f = open(file_name, "a")

    for triple_list in triples:
        for triple in triple_list:
            subject = urllib.parse.quote_plus(str(triple[0]))
            predicate = urllib.parse.quote_plus(str(triple[1]))
            object = urllib.parse.quote_plus(str(triple[2]))
            f.write('<urn:'+subject+'> <urn:'+predicate+'> <urn:'+object+'> .\n')

    f.close()
    return file_name
