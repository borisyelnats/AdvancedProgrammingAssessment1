from player import player
from player_bnode import PlayerBNode

class PlayerBST:
    
    def __init__(self):
        self.__root = None

    @property
    def root(self):
        return self.__root
    
    #root setter
    def root_set(self, player):
        self.__root = PlayerBNode(player)

    

    def insert_player_node(self, player):
        if self.root is None:
            self.root = PlayerBNode(player)
        else:
            self.recursive_insert_player_node(self.root, player)

    def recursive_insert_player_node(self, node, player):
        if node is None:
            node = PlayerBNode(player)
            return
        elif player.name < node.name: 
            self.recursive_insert_player_node(node.left, player)
        elif player.name > node.name: 
            self.recursive_insert_player_node(node.right, player)
        elif player.name == node.name:
            node = PlayerBNode(player)
            return

        

'''
psuedo code
objects name property is key (alphabetical)
1. does node exist? if no, insert RETURN, if yes test
2. Is KEY > node? yes -> R, no -> L, is key == Node? if yes, update but retain L and R 
3. RECURSION

two functions
insert and recursive insert

1. Insert: if root empty, insert, else recursive insert 
(takes one input, the player)

2. Recursive INsert: 
requires node, self, player



'''
