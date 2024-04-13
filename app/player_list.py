
class PlayerList:
    
    def __init__(self):
        self.__head = None
    
    @property
    def get_head(self):
        if self.__head is None:
            return None
        else:
            return self.__head
        
    def has_head(self):
        if self.__head is None:
            return 0
        if self.__head is not None:
            return 1

    def insert_node(self, player):

        if self.has_head() == False:
            self.__head = player

        elif self.has_head() ==True:
            self.__head.set_previous(player)
            player.set_next(self.__head)
            self.__head = player

            

