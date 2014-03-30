class Subscriber():
    """docstring for Subscriber"""
    def __init__(self, name, email):
        self.__id = -1
        self.__name = name
        self.__email = email

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def update_subscriber(self, name, email):
        self.__name = name
        self.__email = email

