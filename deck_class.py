import card_class
from random import shuffle

class Deck():

	def __init__(self):

		self.deck = []

		self.suits = ['Spades','Hearts','Clubs','Diamonds']
		self.values = ['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']

		for suit in self.suits:
			for value in self.values:
				self.deck.append(card_class.Card(suit,value))

	def shuffle_deck(self):
		shuffle(self.deck)

	def draw_card(self):
		return self.deck.pop(0)
