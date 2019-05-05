class player:
	def __init__(self, location: list, height: int, hview: int, vview):
		self.x, self.y = location
		self.height = height
		self.hview = hview
		self.vview = vview

	def get_location(self):
		return self.x, self,y

	def get_heigh(self):
		return self.height

