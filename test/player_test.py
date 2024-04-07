import unittest
import sys
sys.path.append("/Users/benjamincooper/Documents/TAFE/advanced programming/AP_ass1/SRUS-BJC-Games/app")
from player import player 

class player_test(unittest.TestCase):
    person = player(1, "a")

    def test_uid(self):
        person = player(1, "a")
        self.assertEqual(person.uid, 1)

    def test_name(self):
        person = player(1, "a")
        self.assertEqual(person.name, "a")

    
    