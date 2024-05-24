
import argon2


class player:

    def __init__(self, uid, name):
        self.__uid = uid
        self.__name = name
        self.__pword = None


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

    
    def __str__(self):
        return (str(self.__uid) + " " + self.__name)
    
    def add_password(self, pword):
        self.__pword = argon2.PasswordHasher().hash(pword)
    
    def verify_password(self, pword_try):
        return argon2.PasswordHasher().verify(self.__pword, pword_try)
