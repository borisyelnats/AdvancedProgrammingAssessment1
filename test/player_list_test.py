import unittest
import sys
sys.path.append("/Users/benjamincooper/Documents/TAFE/advanced programming/AP_ass1/SRUS-BJC-Games/app")
import player
import player_list
import player_node

class player_test(unittest.TestCase):
    

    def test_full(self):
        #set up the list which contains elements
        A = player.player(1, "Aaron")
        B = player.player(2, "Ben")

        An = player_node.Player_node(A)
        Bn = player_node.Player_node(B)

        List_Full = player_list.PlayerList()
        List_Full.insert_node(An)
        List_Full.insert_node(Bn)

        self.assertEqual(List_Full.get_head.key, 2)


    def test_empty(self):
        #setup the list which is empty
        List_Empty = player_list.PlayerList()
        A = player.player(1, "Aaron")
        An = player_node.Player_node(A)
        List_Empty.insert_node(An)

        self.assertEqual(List_Empty.get_head.key, 1)
        #self.