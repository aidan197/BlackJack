
class Player:
    def __init__(self):
        self.__money = 20
        self.__cards = {}
        self.__score = 0


class Dealer:
    def __init__(self):
        self.__score = 0
        self.__cards = {}


class Card:
    def __init__(self, value, name):
        self.__value = value
        self.__name = name


