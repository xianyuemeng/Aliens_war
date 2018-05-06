class GameStats():
	
	def __init__(self,ai_settings):
		self.ai_settings = ai_settings
		self.reset_stats()
		self.game_active = False
		with open('highscore.txt','r') as hs:
			highscore = hs.read()
		self.high_score = int(highscore)
		
	def get_high_score(self):
		with open('highscore.txt','r') as hs:
			highscore = hs.read()
		return highscore
	
	def reset_stats(self):
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1
	
