
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
    
    def has_tail(self):
        if self.__tail is None:
            return 0
        if self.__tail is not None:
            return 1
    

    def insert_node(self, player):
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
    
    def delete_head(self):
        if self.has_head() == False:
            return
        elif self.has_head() ==True:
            if self.__head.next is None:
                self.__head = None
                self.__tail = None
            elif self.__head.next is not None:
                self.__head.next.set_previous = None
                self.__head = self.__head.next

    def delete_tail(self):
        if self.has_tail() ==False: 
            return
        elif self.has_tail() == True:
            if self.__tail == self.__head:
                self.__tail = None
                self.__head = None
            else:
                self.__tail.previous.set_next(None)
                self.__tail = self.__tail.previous


    def display(self, forward=True):

        if forward:
            print("printing in forward direction")
            i = self.get_head
            while i is not None:
                print(i.key, end = ">")
                i = i.next
            
        elif not forward:
            print("printing in reverse direction")
            i = self.get_tail
            while i is not None:
                print(i.key, end = ">")
                i = i.previous
        
        print("\n")



