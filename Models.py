class Player:
    def __init__(self):
        self.__money = 20
        self.__cards = []
        self.__score = 0
        self.__bet = 0
        self.__win_loose = True  
        self.__turn = True  
        self.__ace = False 

    def clean_cards(self):
        self.__cards=[]          

    def show_card_append(self):
        return self.__cards         

    def get_money(self):
        return self.__money

    def set_bet(self):
        print("Type you bet")
        bet_num=int(input())
        if(bet_num<=int(self.__money) and bet_num>0):
            self.__bet=bet_num
            return False
        else:
            return True     

    def set_win_loose(self, win_loose):
        self.__win_loose= win_loose        

    def set_money(self):
        if(self.__win_loose):
            self.__money = self.__money  + int(self.__bet) 
        else:
            self.__money = self.__money  - int(self.__bet)     
    def get_score(self):
        return self.__score

    def set_score(self):
        score = 0
        for x in self.__cards:
            score= score + int(x.get_value())
            if (int(x.get_value())==11):
                self.__ace=True
        self.__score =  score

    def set_score_ace(self):
        self.__score= self.__score - 10        
    
    def get_cards(self,cards):
        self.__cards.append(cards[0])
        cards.pop(0)
        return cards

    def show_cards(self):
        print("Player cards")
        if(self.__turn):
            for x in self.__cards:
                print(x.get_name())
        else:   
            for x in range(1,len(self.__cards)):
                print(self.__cards[x].get_name())
    def get_turn(self):
        return self.__turn

    def set_turn(self, turn):
        self.__turn = turn 

    def set_ace(self, ace):
        self.__ace = ace   

    def get_ace(self):
        return self.__ace    


class Dealer:
    def __init__(self):
        self.__score = 0
        self.__cards = []
        self.__turn = False 
        self.__ace = False        
    def show_card_append(self):
        return self.__cards

    def get_score(self):
        return self.__score

    def set_score(self):
        score = 0
        for x in self.__cards:
            score= score + int(x.get_value())
            if (int(x.get_value())==11):
                self.__ace=True
        self.__score =  score
    
    def get_cards(self,cards):
        self.__cards.append(cards[0])
        cards.pop(0)
        return cards

    def show_cards(self):
        print("Dealer cards")
        if(self.__turn):
            for x in self.__cards:
                print(x.get_name())
        else:   
            for x in range(1,len(self.__cards)):
                print(self.__cards[x].get_name())
    def get_turn(self):
        return self.__turn

    def set_turn(self, turn):
        self.__turn = turn 

    def set_score_ace(self):
        self.__score= self.__score - 10   

    def set_ace(self, ace):
        self.__ace = ace   

    def get_ace(self):
        return self.__ace           

    def clean_cards(self):
        self.__cards=[]          

class Card:
    def __init__(self, value, name):
        self.__value = value
        self.__name = name

    def get_value(self):
        return self.__value

    def get_name(self):
        return self.__name




