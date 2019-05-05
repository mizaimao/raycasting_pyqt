class mdot:	# stands for a dot on map
	def __init__(self, low, high, low_type, high_type):
		self.low = low
		self.high = high
		self.low_type = low_type
		self.high_type = high_type

	def get(self):
		return self.low, self.high, self.low_type, self.high_type

class level_class:
	def __init__(self, width = 300, height = 300, margin = 20):
		self.X = width
		self.Y = height
		level_list = []
		for x in range(self.X):
			row = []
			for y in range(self.Y):
				if (x <= margin or x >= self.X - 1 - margin):
					row.append(mdot(low=0, high=100,low_type=0, high_type=1))	
				elif (y <= 0 + margin or y >= self.Y - 1 - margin):
					row.append(mdot(low=0, high=100,low_type=0, high_type=1))
				else:
					row.append(mdot(low=0, high=0, low_type=0, high_type=1))
			level_list.append(row)				
		#self.add_block(120, 180, 100, 100)
		self.level = tuple(level_list)


	def add_block(self, startX=120, startY=180, lengthX=100, lengthY=100):
		for x in range(lengthX):
			for y in range(lengthY):
				self.level[y][x].high=100
				


