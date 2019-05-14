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
