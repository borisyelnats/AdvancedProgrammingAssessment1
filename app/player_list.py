
class PlayerList:

    #special methods
    
    def __init__(self):
        self.__head = None
        self.__tail = None
    
    #properties
    
    @property
    def get_head(self):
        if self.__head is None:
            return None
        else:
            return self.__head
        
    @property
    def get_tail(self):
        if self.__tail is None:
            return None
        else:
            return self.__tail
    
    #methods
    def has_head(self):
        if self.__head is None:
            return 0
        if self.__head is not None:
            return 1

    def insert_node(self, player):
        #inserts a node at the head, replacing current head 
        if self.has_head() == False:
            self.__head = player
            self.__tail = player 

        elif self.has_head() ==True:
            self.__head.set_previous(player)
            player.set_next(self.__head)
            self.__head = player

    def insert_at_tail(self, player):
        if self.has_head() == False:
            self.insert_node(player)

        elif self.has_head() == True:
            self.__tail.set_next(player)
            player.set_previous(self.__tail)
            self.__tail = player 

