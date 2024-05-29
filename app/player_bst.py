from player import player
from player_bnode import PlayerBNode

class PlayerBST:
    '''
    instantiating this Binary Search Tree requires no inputs
    '''
    
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
                self.recursive_insert_player_node(node.right, player)
        elif player.name == node.name:
            node = PlayerBNode(player)
    

    
    def search(self, player):
        name = player.name
        if self.root.name == name:
            return name
        else:
            searching = self.search_recursive(self.root, name)
            return searching

    def search_recursive(self, node, name):
        if name < node.name:

            if node.left == None:
                return None
            elif name == node.left.name:
                return node.left
            else:
                searching = self.search_recursive(node.left, name)
                return searching

        if name > node.name:

            if node.right == None:
                return None
            elif name == node.right.name:
                return node.right
            else:
                searching = self.search_recursive(node.right, name)
                return searching
        
