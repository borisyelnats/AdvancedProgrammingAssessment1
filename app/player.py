class player:

    def __init__(self, uid, name):
        self.__uid = uid
        self.__name = name


    @property #getter methodology for calling the private attribute
    def name(self):
        return self.__name
    
    @property
    def uid(self):
        return self.__uid
    
    def __str__(self):
        return (str(self.__uid) + " " + self.__name)
    
    