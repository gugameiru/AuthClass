import json
import hashlib
import sys
import os

class auth:

    
    def __init__(self):
        self.names = {}
        self.dataname = 'db_names.txt'
        self.myfile = open(self.dataname, mode='r')
        try:
            json_data = json.load(self.myfile)
        except json.decoder.JSONDecodeError as err:
            json_data = {}
        self.names = json_data
        self.myfile.close()

