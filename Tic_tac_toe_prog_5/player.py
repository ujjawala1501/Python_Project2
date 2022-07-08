import math
import random

class player:
	def __init__(self,letter):
		#letter is x or o
		self.letter = letter
#we want all players to get their next move given a game
	def get_move(self,game):
		pass

class RandomComputerPlayer(player): # Used inheritance inheriting player class
	def __init__(self,letter):
		super().__init__(letter)

	def get_move(self,game):
		square = random.choice(game.available_moves())
		return square

class HumanPlayer(player):           # Used inheritance inheriting player class
	def __init__(self,letter):
		super().__init__(letter)

	def get_move(self,game):
		valid_square = False
		val= None
		while not valid_square:
			square = input(self.letter + '\'s turn. Input move (0-8):')
			#we're going to check that this is correct value by trying to cast
			#it to and integer,and if its not,then we say its valid
			#if that spot is not available on the board, we also say its valid
			try:
				val=int(square)
				if val not in game.available_moves():
					raise ValueError
				valid_square =True #if these are successful,then yay!

			except ValueError:
				print('Invalid square,Try again.')
		return val
		