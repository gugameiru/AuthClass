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

    def create_db(self):
        self.filename = input('Введите имя файла с данными пользователей ')
        if os.path.exists(self.filename):
            self.dataname=self.filename
            print("Данные пользователей хранятся в файле " + self.dataname)
            return 
        else:
            self.is_create=input("Создать новый файл данных для пользователей? Введите имя файла если да или 0 если нет ")
            if self.is_create != '0':
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

    def add_user(self):
        print("Добавление нового пользователя\n")
        self.name = input('Введите логин: ')
        self.passwd = input('Введите пароль: ')
        self.passwd_hash = hashlib.md5(bytes(self.passwd, "UTF-8")).hexdigest()
        if self.name not in self.names:
            self.names[self.name]=self.passwd_hash
            myfile = open(self.dataname, mode='w')
            json.dump(self.names, myfile)
            myfile.close()
            print('Пользователь добавлен')
            return
        print('Такой пользователь уже есть')
        return

    def check_user(self):
        print("Аутентификация пользователя\n")
        self.check_name=input('Введите логин: ')
        self.check_passwd = input('Введите пароль: ')
        self.check_passwd_hash = hashlib.md5(bytes(self.check_passwd, "UTF-8")).hexdigest()
        if self.check_name not in self.names:
            print("Неверно указано имя")
            return
        if self.names[self.check_name] != self.check_passwd_hash:
            print('Неверно указан пароль')
            return
        print('Пользователь аутентифицирован')
        return

    def delete_user(self):
        print("Удаление пользователя\n")
        self.del_name = input('Введите логин: ')
        self.del_passwd = input('Введите пароль: ')
        self.del_passwd_hash = hashlib.md5(bytes(self.del_passwd, "UTF-8")).hexdigest()
        if self.del_name not in self.names:
            print("Неверно указано имя")
            return
        if self.names[self.del_name] != self.del_passwd_hash:
            print('Неверно указан пароль')
            return
        del self.names[self.del_name]
        myfile = open(self.dataname, mode='w')
        json.dump(self.names, myfile)
        myfile.close()
        print('Пользователь удален')
        return
        
        
            
            


    
user1 = auth()

#user1.create_db()
#user1.add_user()
#user1.check_user()
#user1.delete_user()

