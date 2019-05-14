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

    def create_db(self, filename, default):
        
        self.filename = filename
        if os.path.exists(self.filename):
            self.dataname=self.filename
            print("Данные пользователей хранятся в файле " + self.dataname)
            return
        else:
            self.is_create=default
            if self.is_create != 0:
                self.dataname = self.is_create
                my_file = open(self.dataname, 'w')
                my_file.close()
                print("Данные пользователей хранятся в файле " + self.dataname)
                return
            self.dataname = 'db_names.txt'
            my_file = open(self.dataname, 'w')
            my_file.close()
            
            print("Данные пользователей хранятся в файле " + self.dataname)
            return

    def add_user(self, name, password):
        
        self.name = name
        
        self.passwd = hashlib.md5(bytes(password, "UTF-8")).hexdigest()
        
        if self.name in self.names:
            return("Такой пользователь уже есть")
        else:
            self.names[self.name]=self.passwd
            
            print('Пользователь добавлен')
            return






