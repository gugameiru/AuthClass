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

    def create_db(self, filename):
        self.filename = filename
        if os.path.exists(self.filename):
            self.dataname=self.filename
            print("Данные пользователей хранятся в файле " + self.dataname)
            return


