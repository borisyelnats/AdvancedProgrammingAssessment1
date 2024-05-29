from player import player
from player_bnode import PlayerBNode

class PlayerBST:
    
    def __init__(self):
        self.__root = None
        self.__instances = 0

    @property
    def instances(self):
        return self.__instances

    def instance_increment(self):
        self.__instances += 1


    @property
    def root(self):
        return self.__root
    
    @root.setter
    def root(self, player):
        self.__root = PlayerBNode(player)

    

    '''
    Insert Function:
    1. left subnode only smaller than
    2. right subnode only larger than
    3. no repeat nodes    
    '''

    def insert(self, player):
        self.instance_increment()

        if self.root is None:
            self.root = player
            return
        else: 
            self.recursive_insert_player_node(self.root, player)
            return
        
    def recursive_insert_player_node(self, node, player):
        if player.name < node.name:
            if node.left is None:
                node.left = PlayerBNode(player)
                return
            else:
                self.recursive_insert_player_node(node.left, player)
        elif player.name > node.name:
            if node.right is None:
                node.right = PlayerBNode(player)
                return
            else:
                self.recursive_insert_player_node(node.left, player)
        elif player.name == node.name:
            node = PlayerBNode(player)
