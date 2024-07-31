from os import walk
from os.path import join
from shutil import rmtree

def clean(path='.'):
    for root, dirs, files in walk(path):
        if "__pycache__" in dirs:
            rmtree(join(root, "__pycache__"))
