import unittest
import sys
sys.path.append("/Users/benjamincooper/Documents/TAFE/advanced programming/AP_ass1/SRUS-BJC-Games/app")
from player import player 
import argon2

#to run: python -m unittest player_test.py

class player_test(unittest.TestCase):
    
    person = player(1, "a")

    def test_uid(self):
        person = player(1, "a")
        self.assertEqual(person.uid, 1)

    def test_name(self):
        person = player(1, "a")
        self.assertEqual(person.name, "a")
    
    def test_add_password(self):
        person = player(1, "a")
        person.add_password("password69!")
        self.assertEqual(person.password_exists, True)

    def test_verify_password(self):
        person = player(1, "a")
        password = "password69!"
        person.add_password(password)
        self.assertTrue(person.verify_password(password))


    
    