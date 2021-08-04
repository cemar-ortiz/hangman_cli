
# Game class encapsulates the game logic. Useful if I want to implement a menu outside of it, for example.
class Game:
	def __init__(self):
		self._word = 'secret'
	
	def setup(self):
		self.letrero = ['_' for x in self._word]
		self._word = [x for x in self._word]
		print(self.letrero)

		
	def midgame(self):
		count_intent = len(self._word)
		
		while (self._word != self.letrero) and count_intent != 0:
			intent = input('Intenta con una letra: ')
			os.system('clear')
			_bool_test = list(map(lambda x: x==intent, self._word))
			for x in range(0,len(self._word)):
				if intent==self._word[x]:
					self.letrero[x]=intent
			print(self.letrero)
			count_intent -= 1
			print(count_intent)
	
	def run(self):
		self.setup()
		self.midgame()
	
# Entry-point
if __name__ == '__main__':
	import os
	game = Game()
	game.run()
