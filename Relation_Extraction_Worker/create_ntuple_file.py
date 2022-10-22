import uuid


def create_ntuple_file(triples):
    file_name = str(uuid.uuid4()) + '.nt'
    f = open(file_name, "a")

    for triple_list in triples:
        for triple in triple_list:
            f.write('<urn:'+str(triple[0])+'> <urn:'+str(triple[1])+'> <urn:'+str(triple[2])+'> .\n')

    f.close()
    return file_name
