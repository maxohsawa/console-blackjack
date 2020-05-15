class Card():

	def __init__(self,suit,value):
		self.value = value
		self.suit = suit

	def card_string(self):
		return f"{self.value} of {self.suit}"