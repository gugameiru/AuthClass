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





