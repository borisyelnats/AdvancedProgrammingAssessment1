
import argon2
import sys
sys.path.append("/Users/benjamincooper/Documents/TAFE/advanced programming/AP_ass1/SRUS-BJC-Games/app")
from scoresort import scoresort


class player:


    '''
    instantiates a player object by uid and name, with pwrd and score variables set to None
    the list of player instances is updated for each instance of player 
    '''

    player_instances = [] #classvariable 

    def __init__(self, uid, name):
        self.__uid = uid
        self.__name = name
        self.__pword = None
        self.__score = 0
        player.player_instances.append(self)

    # PROPERTIES
    @property #getter methodology for calling the private attribute
    def name(self):
        return self.__name
    
    @property
    def uid(self):
        return self.__uid
    
    @property
    def password_exists(self):
        if self.__pword is not None:
            return True
        elif self.__pword is None:
            return False
    
    @property
    def score(self):
        return self.__score



    # METHODS

    #dunder methods

    def __str__(self):
        return (str(self.__uid) + " " + self.__name)
    
    def __ge__(self, x):
        if self.score >= x.score:
            return True
        else:
            return False
        
    def __eq__(self, x):
        if self.score == x.score:
            return True
        else:
            return False
    
    def __repr__(self):
        return f"player({self.name} score={self.score})"    
    
    #normal methods

    def add_password(self, pword):
        self.__pword = argon2.PasswordHasher().hash(pword)
    
    def verify_password(self, pword_try):
        return argon2.PasswordHasher().verify(self.__pword, pword_try)

    def set_score(self, score):
        self.__score = score

       #static methods

    @staticmethod
    def get_all_instances():
        return player.player_instances
    
    @staticmethod
    def sort_all_instances():
        player.player_instances = scoresort(player.player_instances, AscendingOrder=False)

