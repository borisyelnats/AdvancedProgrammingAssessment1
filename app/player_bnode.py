

class PlayerBNode:
    
    def __init__(self, player):
        self.__player = player
        self.__name = player.name
        self.__left = None
        self.__left = None

    @property
    def player(self): 
        return self.__player
    
    @property
    def name(self):
        return self.__name 

    #LEFT
    @property
    def left(self):
        return self.__left
    
    @left.setter
    def left(self, leftnode):
        self.__left = leftnode
    
    #RIGHT
    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, rightnode):
        self.__right = rightnode  
