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

