import os

def datafile(name):
    return open(os.path.join(os.path.dirname(__file__), 'files', name))