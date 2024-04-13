
class Player_node():
    
    #SPECIAL METHODS
    def __init__(self, player):
        self.__player = player
        self.__next = None
        self.__previous = None

    def __str__(self):
        return(str(self.key))
    #GETTERS

    @property #getter methodology for calling the private attribute
    def next(self):
        return self.__next
    
    @property
    def previous(self):
        return self.__previous

    @property 
    def key(self):
        return self.__player.uid
    
    #setters

    def set_next(self, value):
        self.__next = value 

    def set_previous(self, value):
        self.__previous = value
    

    
