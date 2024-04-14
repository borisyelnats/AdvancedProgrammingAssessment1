import unittest
import sys
sys.path.append("/Users/benjamincooper/Documents/TAFE/advanced programming/AP_ass1/SRUS-BJC-Games/app")
import player
import player_list
import player_node

class player_test(unittest.TestCase):

    #A = player.player(1, "Aaron")
    #B = player.player(2, "Ben")
    An = player_node.Player_node(player.player(1, "Aaron"))
    Bn = player_node.Player_node(player.player(2, "Ben"))
    
    #1 tests if the head key matches the right keuy
    def test_full(self):
        An = player_node.Player_node(player.player(1, "Aaron"))
 
        List_Full = player_list.PlayerList()
        List_Full.insert_node(self.An)

        self.assertEqual(List_Full.get_head.key, An.key)


    #2 tests if the head key matches the right key with insertion on an empty list
    def test_empty(self):
        #setup the list which is empty
        List_Empty = player_list.PlayerList()

        List_Empty.insert_node(self.An)

        self.assertEqual(List_Empty.get_head.key, self.An.key)
    
    #3 tests if that tail property returns the correct value for empty, 1 and 2 entried list
    def test_tail(self):

        An = player_node.Player_node(player.player(1, "Aaron"))
        Bn = player_node.Player_node(player.player(2, "Ben"))
    
        List_Tail = player_list.PlayerList()
        self.assertIsNone(List_Tail.get_tail)
        List_Tail.insert_node(An)
        self.assertEqual(List_Tail.get_tail.key, An.key)
        List_Tail.insert_node(Bn)
        self.assertEqual(List_Tail.get_tail.key, An.key)
    
    #4 tests if the tail updates when the insert at tail function is used
    def test_insert_at_tail(self):
        
        List_Tail = player_list.PlayerList()
        List_Tail.insert_node(self.An)
        self.assertEqual(List_Tail.get_tail.key, self.An.key)
        List_Tail.insert_at_tail(self.Bn)
        self.assertEqual(List_Tail.get_tail.key, self.Bn.key)

    #5 tests head deletion
    def test_delete_head(self):
            
        List = player_list.PlayerList()
        List.delete_head()
        self.assertIsNone(List.get_head)
        
        List.insert_node(self.An)
        List.delete_head()
        self.assertIsNone(List.get_head)

        List.insert_node(self.An)
        List.insert_node(self.Bn)
        List.delete_head()
        self.assertEqual(List.get_head.key, self.An.key)
            
    def test_delete_tail(self):
        An = player_node.Player_node(player.player(1, "Aaron"))
        Bn = player_node.Player_node(player.player(2, "Ben"))

        List = player_list.PlayerList()
        #List.delete_tail()
        #self.assertIsNone(List.get_tail)
        
        
        List.insert_node(An)
        List.delete_tail()
        self.assertIsNone(List.get_tail)


        List.insert_node(An) #head
        List.insert_node(Bn) #new head, An becomes tail
        List.delete_tail() #deletes An, Bn should become tail
        self.assertEqual(List.get_tail.key, Bn.key)







    
