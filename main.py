from Models import *
import random
player= Player()
dealer= Dealer()
cards = []
play = True
def read_cards():
	global cards
	with open("cards.txt") as f:
		lines_of_text = f.read().splitlines()
	for x in range(0,len(lines_of_text)):
		value_name=lines_of_text[x].split("/")
		cards.append(Card(value_name[0],value_name[1]))   

def play_game():
	global cards
	global player
	random.shuffle(cards)	
	print("Player money: "+str(player.get_money()))
	player_play()

def player_play():
	global cards
	global player
	global dealer	
	bet_real=True
	player.set_ace(False)
	while bet_real:
		bet_real=player.set_bet()
	cards=player.get_cards(cards)
	cards=player.get_cards(cards)
	cards=dealer.get_cards(cards)
	cards=dealer.get_cards(cards)
	player.set_score()
	dealer.set_score()
	while player.get_turn():
		player.show_cards()
		player.set_score()
		dealer.show_cards()	
		if(int(player.get_score())==21):
			print("21")
			player.set_win_loose(True)
			player.set_money()
			player.set_turn(False)
		else:
			if (int(player.get_score())>21):
				if (player.get_ace):
					player.set_score_ace()
			if (int(player.get_score())>21):
				print("busted")
				player.set_win_loose(False)
				player.set_money()
				player.set_turn(False)
			else:	
				print("Get another card")
				res=input()
				if (res=="yes"):
					cards=player.get_cards(cards)
					player.set_score()
					player.set_turn(True)
				else: 	
					player.set_turn(False)
					dealer.set_turn(True)
	while dealer.get_turn():
		dealer.show_cards()
		print(dealer.get_score())
		print(dealer.get_score()<17)
		while(dealer.get_score()<17):
			cards=dealer.get_cards(cards)
			dealer.show_cards()
			dealer.set_score()
			
		if(int(dealer.get_score())!=int(player.get_score())):	
			if(int(dealer.get_score())>int(player.get_score())):
				player.set_win_loose(False)
			else:
				player.set_win_loose(True)
			dealer.set_turn(False)
			player.set_money()			

def reset_game():
	global player
	global cards
	global dealer
	player.set_turn(True)
	dealer.set_turn(False)
	for x in player.show_card_append():
		cards.append(x)
	for x in dealer.show_card_append():
		cards.append(x)
	player.clean_cards()
	dealer.clean_cards()
		
def play_again():
	global player
	global plays
	print("Player money: "+str(player.get_money()))
	print("paly agin?")
	text=input()
	if (text=="yes"):
		play=True
		reset_game()
	else:
		play=False	

read_cards()
while play:
	play_game()
	play_again()

	

