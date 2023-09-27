import requests
import os
import time
# Patrick Elser pte6144@rit.edu

MAXIMUM_FILE_SIZE = 1000000000                          # Sets some basic settings
DIRECTORIES = ["C:\\Users\\patri\\Documents\\test"]
SERVER = "http://localhost:5000"
DELAY = 10


def load_directory(directory, foreign_name):
    """
    Recursively finds all files in a directory and sends them in post requests
    :param directory: The directory to start in
    :param foreign_name: The first part of the key for the post request
    :return: Nothing.
    """
    os.chdir(directory)
    files = os.listdir()
    for file in files:
        if os.path.isfile(file):
            if os.path.getsize(file) > MAXIMUM_FILE_SIZE:
                continue
            with open(file, 'rb') as data:
                requests.post(SERVER, {foreign_name + "\\" + file: data.read()})
            time.sleep(10)
        else:
            load_directory(file, foreign_name + "\\" + file)
            os.chdir(directory)


for directory in DIRECTORIES:
    names = directory.split("\\")
    load_directory(directory, names[-1] if names[-1] != "" else names[-2])
