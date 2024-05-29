import unittest
import sys
sys.path.append("/Users/benjamincooper/Documents/TAFE/advanced programming/AP_ass1/SRUS-BJC-Games/")
from app.player import player 
from app.player_bnode import PlayerBNode
from app.player_bst import PlayerBST

#to run: python -m unittest player_bst_test.py

class player_bst_test(unittest.TestCase):
    
    a = (player(1,"A"))
    b = (player(1,"B"))
    c = (player(1,"C"))
    d = (player(1,"D"))
    e = (player(1,"E"))
    f = (player(1,"F"))
    bst = PlayerBST()
    
    def test_insertroot(self):
        '''
        tests if insertion works
        '''
        a = (player(1,"A"))
        bst = PlayerBST()
        bst.insert(a)
        self.assertEqual(a.name, bst.root.name)
    
    def test_insert_replace(self):
        '''
        tests if insertion and replacement of existing node with same nameworks
        '''
        a = (player(1,"A"))
        b = (player(2,"A"))
        bst = PlayerBST()
        bst.insert(a)
        bst.insert(b)
        self.assertEqual(b.name, bst.root.name)

    def test_left(self):
        a = (player(1,"B"))
        b = (player(2,"A"))
        bst = PlayerBST()
        bst.insert(a)
        bst.insert(b)
        self.assertLess(bst.root.left.name, bst.root.name)

    def test_right(self):
        a = (player(1,"B"))
        b = (player(2,"D"))
        bst = PlayerBST()
        bst.insert(a)
        bst.insert(b)
        self.assertGreater(bst.root.right.name, bst.root.name)

    
    
    

