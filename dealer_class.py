import card_class

class Dealer():

	def __init__(self):

		self.hand = []
		self.blind = []

	def receive_to_hand(self,card):
		self.hand.append(card)

	def receive_to_blind(self,card):
		self.blind.append(card)

	def blind_to_hand(self):
		self.hand.append(self.blind[0])
		self.blind = []

	def remove_cards(self):
		cards = self.hand
		cards.extend(self.blind)
		self.hand = []
		self.blind = []
		return cards

	def print_hand(self):
		for card in self.hand:
			print(f"|| {card.card_string()} || ")

		if self.blind:
			print("|| Face-Down Card || ")