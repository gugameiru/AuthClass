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
            myfile = open(self.dataname, mode='w')
            json.dump(self.names, myfile)
            myfile.close()
            print('Пользователь добавлен')
            return

    def check_user(self, name, password):
        self.check_name=name
        self.check_passwd = password
        self.check_passwd_hash = hashlib.md5(bytes(self.check_passwd, "UTF-8")).hexdigest()
        if self.check_name not in self.names:
            return('Неверно указано имя')
        if self.names[self.check_name] != self.check_passwd_hash:
            return('Неверно указан пароль')
        return('Пользователь аутентифицирован')

    def delete_user(self, name, password):
        self.permission = self.check_user(name, password)
        if self.permission == 'Неверно указано имя' or self.permission == 'Неверно указан пароль':
            return self.permission
        if self.permission == 'Пользователь аутентифицирован':
            del self.names[self.name]
            myfile = open(self.dataname, mode='w')
            json.dump(self.names, myfile)
            myfile.close()
            return('Пользователь удален')      










