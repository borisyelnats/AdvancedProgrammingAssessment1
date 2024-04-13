
class PlayerList:
    
    def __init__(self):
        self.__head = None
        self.__tail = None
    
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
        
    def has_head(self):
        if self.__head is None:
            return 0
        if self.__head is not None:
            return 1

    def insert_node(self, player):

        if self.has_head() == False:
            self.__head = player
            self.__tail = player #for an empty list, make the head the tail, this will remain the tail

        elif self.has_head() ==True:
            self.__head.set_previous(player)
            player.set_next(self.__head)
            self.__head = player

            

