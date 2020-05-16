import card_class
import deck_class
import player_class
import dealer_class

value_conversion = {'Ace':11,'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10}

def display_message(message):
	print(f"\n===== {message} =====")

def initialize_deck():
	return deck_class.Deck()

def initialize_dealer():
	return dealer_class.Dealer()

def initialize_player():

	player_name = input("\nWhat is the player's name? ")

	display_message(f"HI, {player_name.upper()}")

	starting_amount_invalid = True

	while starting_amount_invalid:

		player_starting_amount = input("\nHow much money would you like to start with? ")

		try:
			player_starting_amount = int(player_starting_amount)
		except:
			print("\nOops: Entered amount was not an integer. Please try again.")
			continue

		starting_amount_invalid = False

	display_message(f"CHANGING ${player_starting_amount}")

	return player_class.Player(player_name, player_starting_amount)

def take_player_bet(player):
	
	bet_amount_invalid = True

	while bet_amount_invalid:

		bet = input(f"\n{player.name}, you have ${player.amount}, how much would you like to bet? ")

		try:
			bet = int(bet)
		except:
			print("\nOops: Please enter an integer.")
			continue

		if bet > player.amount:
			print(f"\nOops: You have ${player.amount}. Please enter an amount less than or equal to that.")
			continue

		bet_amount_invalid = False

	player.withdraw(bet)

	display_message(f"${bet} BET")

	return bet

def deal_card_to_player(deck,player):
	card = deck.draw_card()
	player.receive_card(card)

def deal_card_to_dealer(deck,dealer):
	card = deck.draw_card()
	dealer.receive_to_hand(card)

def deal_blind_to_dealer(deck,dealer):
	card = deck.draw_card()
	dealer.receive_to_blind(card)

def deal_starting_hands(deck,player,dealer):

	display_message("DEALING CARDS")
	deal_card_to_player(deck,player)
	deal_card_to_dealer(deck,dealer)
	deal_card_to_player(deck,player)
	deal_blind_to_dealer(deck,dealer)

def total_hand(hand):

	total = 0

	for card in hand:
		total += value_conversion[card.value]

	if total > 21:
		for card in hand:
			if card.value == 'Ace' and total > 21:
				total -= 10
	return total

def glimpse_player_hand(player):

	display_message(f"{player.name.upper()}'S HAND")

	player.print_hand()

	print(f"\n{player.name}'s value: {total_hand(player.hand)}")

	if total_hand(player.hand) == 21:
		display_message("BLACKJACK")
	

def glimpse_dealer_hand(dealer):

	display_message("DEALER'S HAND")

	dealer.print_hand()

	if not dealer.blind:

		print(f"\nDealer's value: {total_hand(dealer.hand)}")

		if total_hand(dealer.hand) == 21:
			display_message("BLACKJACK")

def get_hit_option():

	option_invalid = True

	while option_invalid:

		option = input("\nWould you like to Hit or Stay? H/S: ").lower()

		if option != 'h' and option != 's':
			print("Please enter H for Hit, or S for Stay.")
			continue

		option_invalid = False

	return option

def check_bust(player):
	return total_hand(player.hand) > 21

def get_replay_option():

	option_invalid = True

	while option_invalid:

		option = input("\nWould you like to play again? Y/N: ").lower()

		if option != 'y' and option != 'n':
			print("Please enter Y for Yes, or N for No.")
			continue

		option_invalid = False

	return option

def player_turn_loop(deck,player):

	player_bust = False

	hit_option = get_hit_option()

	while hit_option == 'h':

		display_message(f"{player.name.upper()}HIT")

		deal_card_to_player(deck,player)

		glimpse_player_hand(player)

		if check_bust(player):

			display_message(f"{player.name.upper()} BUST")
			player_bust = True
			hit_option = 's'
			input("\nHit Enter to Continue")
			break

		else:
			hit_option = get_hit_option()

	return player_bust

def dealer_turn_loop(deck,dealer):

	dealer_bust = False

	display_message("DEALER'S TURN")

	dealer.blind_to_hand()

	glimpse_dealer_hand(dealer)

	input("\nHit Enter to Continue")

	while total_hand(dealer.hand) < 17:

		display_message("DEALER HIT")

		deal_card_to_dealer(deck,dealer)

		glimpse_dealer_hand(dealer)

		if check_bust(dealer):

			display_message("DEALER BUST")
			dealer_bust = True
			input("\nHit Enter to Continue")
			break

		input("\nHit Enter to Continue")

	return dealer_bust

'''
MAIN
'''

if __name__ == '__main__':

	deck = initialize_deck()

	dealer = initialize_dealer()

	player = initialize_player()

	replay_flag = True

	while replay_flag:

		display_message("SHUFFLING")
		deck.shuffle_deck()

		bet = take_player_bet(player)

		deal_starting_hands(deck,player,dealer)

		glimpse_player_hand(player)

		glimpse_dealer_hand(dealer)

		player_bust = player_turn_loop(deck,player)

		if not player_bust:

			display_message(f"{player.name.upper()} STAY")

			dealer_bust = dealer_turn_loop(deck,dealer)

		if player_bust or (not dealer_bust and (total_hand(dealer.hand) > total_hand(player.hand))):

			display_message("DEALER WINS")
			print(f"You lose ${bet}")
			player.loss_count += 1

		elif dealer_bust or (total_hand(player.hand) > total_hand(dealer.hand)):

			display_message(f"{player.name.upper()} WINS")
			display_message(f"${bet}")
			player.win_count += 1
			player.deposit(bet*2)

		else:
			display_message("TIE")
			print(f"You get ${bet} back")
			player.tie_count += 1
			player.deposit(bet)

		display_message("END OF HAND")

		deck.deck.extend(player.remove_cards())
		deck.deck.extend(dealer.remove_cards())

		print(player.history_string())

		if player.amount == 0:
			print("\nYou're out of money!")
			break

		replay_option = get_replay_option()

		if replay_option == 'n':
			replay_flag = False

	print(f"\nThanks for playing, {player.name}!\n")