import card_class

class Player():

	def __init__(self,name,starting_amount):

		self.name = name
		self.amount = starting_amount
		self.hand = []
		self.win_count = 0
		self.loss_count = 0
		self.tie_count = 0

	def withdraw(self,change):
		self.amount -= change

	def deposit(self,change):
		self.amount += change

	def history_string(self):
		return f"\nMONEY: ${self.amount}\nWINS: {self.win_count}\nLOSSES: {self.loss_count}\nTIES: {self.tie_count}"

	def receive_card(self,card):
		self.hand.append(card)

	def remove_cards(self):
		cards = self.hand
		self.hand = []
		return cards

	def print_hand(self):
		for card in self.hand:
			print(f"|| {card.card_string()} || ")