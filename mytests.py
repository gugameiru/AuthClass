import unittest
from AuthClass import auth
import json
import hashlib




class AuthClassTest(unittest.TestCase):

    #@unittest.skip
    def test_data_load(self):
        self.names = {'Kolya':'123456'}
        self.dataname = 'db_names.txt'
        self.myfile = open(self.dataname, mode='w')
        json.dump(self.names, self.myfile)
        self.myfile.close()
        self.user1 = auth()
        self.assertEqual(self.names, self.user1.names)

    def test_empty_file(self):
        self.names = {}
        self.dataname = 'db_names.txt'
        self.myfile = open('db_names.txt', 'tw', encoding='utf-8')
        self.myfile.close()
        self.myfile = open(self.dataname, mode='r')
        try:
            json_data = json.load(self.myfile)
        except json.decoder.JSONDecodeError as err:
            json_data = {}
        self.names = json_data
        self.myfile.close()
        self.user2 = auth()
        self.assertEqual(self.names, self.user2.names)

    def test_is_using_existing_file(self):
        
        self.dataname = 'db_names_2.txt'
        self.myfile = open('db_names_2.txt', 'tw', encoding='utf-8')
        self.myfile.close()
        self.user3 = auth()
        self.user3.create_db(self.dataname,1)
        self.assertEqual(self.dataname, self.user3.dataname)

    def test_is_creating_new_file(self):
        self.dataname = 'db_names_3.txt'
        self.user4 = auth()
        self.user4.create_db(self.dataname)
        self.assertEqual(self.dataname, self.user4.dataname)

    def test_is_using_default_file(self):
        self.dataname = 'db_names_8.txt'
        self.user5 = auth()
        self.user5.create_db(self.dataname,0)
        self.assertEqual('db_names.txt', self.user5.dataname)

    def test_is_user_existing(self):
        self.name = 'Misha'
        self.password = '123456'
        self.names = {self.name:self.password}
        self.dataname = 'db_names.txt'
        self.myfile = open(self.dataname, mode='w')
        json.dump(self.names, self.myfile)
        self.myfile.close()
        self.user6 = auth()
        self.assertRaises(ValueError, self.user6.add_user, self.name, self.password)

    def test_is_password_secured(self):
        self.name = 'Vasya'
        self.password = '123456'
        self.names = {self.name:self.password}
        self.dataname = 'db_names.txt'
        self.myfile = open(self.dataname, mode='w')
        json.dump(self.names, self.myfile)
        self.myfile.close()
        self.user7 = auth()
        self.user7.add_user(self.name, self.password)
        self.assertNotEqual(self.password, self.user7.passwd_hash)

    def test_is_user_in_memory(self):
        self.name = 'Petya'
        self.password = '123489'
        self.passwd_hash = hashlib.md5(bytes(self.password, "UTF-8")).hexdigest()
        self.user8 = auth()
        self.user8.add_user(self.name, self.password)
        if self.name in self.user8.names:
            self.assertTrue(True)
        else:
            self.assertTrue(False)
        self.assertEqual(self.user8.names[self.name], self.passwd_hash)

    def test_is_user_in_file(self):
        self.name = 'Zhenya'
        self.password = '123456'
        self.passwd_hash = hashlib.md5(bytes(self.password, "UTF-8")).hexdigest()
        self.names = {self.name:self.passwd_hash}
        
        self.user9 = auth()
        self.user9.add_user(self.name, self.password)
        
        self.dataname = 'db_names.txt'
        self.myfile = open(self.dataname, mode='r')
        try:
            json_data = json.load(self.myfile)
        except json.decoder.JSONDecodeError as err:
            json_data = {}
        
        self.names2 = json_data
        self.myfile.close()

        if self.name in self.names2 and self.names2[self.name]==self.passwd_hash:
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    def test_is_right_name(self):
        self.name = 'Senya'
        self.fake_name = 'Ssenya'
        self.password = '124456'
                
        self.user10 = auth()
        self.user10.add_user(self.name, self.password)
                self.assertEqual(self.user10.check_user(self.fake_name, self.password),'Неверно указано имя')

    def test_is_right_password(self):
        self.name = 'Manya'
        self.password = '124456'
        self.fake_password = '124564'
                
        self.user11 = auth()
        self.user11.add_user(self.name, self.password)
        self.assertEqual(self.user11.check_user(self.name, self.fake_password),'Неверно указан пароль')
                








