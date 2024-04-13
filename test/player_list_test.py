import unittest
import sys
sys.path.append("/Users/benjamincooper/Documents/TAFE/advanced programming/AP_ass1/SRUS-BJC-Games/app")
import player
import player_list
import player_node

class player_test(unittest.TestCase):
    
    #tests if the head key matches the right keuy
    def test_full(self):
        
        A = player.player(1, "Aaron")
        B = player.player(2, "Ben")

        An = player_node.Player_node(A)
        Bn = player_node.Player_node(B)

        List_Full = player_list.PlayerList()
        List_Full.insert_node(An)
        List_Full.insert_node(Bn)

        self.assertEqual(List_Full.get_head.key, 2)

    #tests if the head key matches the right key with insertion on an empty list
    def test_empty(self):
        #setup the list which is empty
        List_Empty = player_list.PlayerList()
        A = player.player(1, "Aaron")
        An = player_node.Player_node(A)
        List_Empty.insert_node(An)

        self.assertEqual(List_Empty.get_head.key, 1)
    
    #tests if that tail property returns the correct value for empty, 1 and 2 entried list
    def test_tail(self):
        An = player_node.Player_node(player.player(1, "Aaron"))
        Bn = player_node.Player_node(player.player(2, "Ben"))
      
    
        List_Tail = player_list.PlayerList()
        self.assertIsNone(List_Tail.get_tail)
        List_Tail.insert_node(An)
        self.assertEqual(List_Tail.get_tail.key, 1)
        List_Tail.insert_node(Bn)
        self.assertEqual(List_Tail.get_tail.key, 1)
    
    #tests if the tail updates when the insert at tail function is used
    def test_insert_at_tail(self):
        An = player_node.Player_node(player.player(1, "Aaron"))
        Bn = player_node.Player_node(player.player(2, "Ben"))
        List_Tail = player_list.PlayerList()
        List_Tail.insert_node(An)
        self.assertEqual(List_Tail.get_tail.key, 1)
        List_Tail.insert_at_tail(Bn)
        self.assertEqual(List_Tail.get_tail.key, 2)





    
