import uuid


def create_ntuple_file(triples):
    file_name = str(uuid.uuid4()) + '.nt'
    f = open(file_name, "a")

    for triple_list in triples:
        for triple in triple_list:
            f.write('<urn:'+str(triple[0]).replace(' ', '_')+'> <urn:'+str(triple[1]).replace(' ', '_')+'> <urn:'+str(triple[2]).replace(' ', '_')+'> .\n')

    f.close()
    return file_name
