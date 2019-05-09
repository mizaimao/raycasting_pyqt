#!/usr/bin/env python3
import random, sys

X = 16; Y = 10
START = (0, 0)
END = (X - 1, Y - 1)

def pm(m):
	for row in m: print(row)

def fill(m):
	dic = {	
			9: (-1, 0), 
			3: (1, 0), 
			0: (0, -1), 
			6: (0, 1)
		}
	xmax = len(m[0]); ymax = len(m)
	directions = [0, 3, 6, 9]

	def bfs(x, y, step, d):
		if x < 0 or x >= xmax: return
		if y < 0 or y >= ymax: return
		if m[y][x] >= 0: return
		m[y][x] = d
		random.shuffle(directions)
		for d in directions:
			nx = x + dic[d][0]; ny = y + dic[d][1]
			bfs(nx, ny, step + 1, d)
		return
	x, y = START
	for x in range(xmax):
		for y in range(ymax):
			bfs(x, y, 1, 3)
	return


def draw(m):	# convert maze to pixels
	WALL = 10
	CELL = 25
	
	rowOfCell = len(m)
	colOfCell = len(m[0])

	pixel = [[0 for x in range(colOfCell * (CELL + WALL) + WALL)] for y in range(rowOfCell * (CELL + WALL)+ WALL)]
	for w in range(WALL):
		for x in range(len(pixel[0])):
			pixel[w][x] = 1
			pixel[-w-1][x] = 1
	for w in range(WALL):
		for y in range(len(pixel)):
			pixel[y][w] = 1
			pixel[y][-w-1] = 1
	yOffSet = WALL
	for row in m:
		xOffSet = WALL
		for i, cell in enumerate(row):
			# draw right wall
			if cell == 9:
				for x in range(CELL, CELL+WALL):
					for y in range(0, CELL):
						pixel[y+yOffSet][x+xOffSet] = 0
			else:
				for x in range(CELL, CELL+WALL):
					for y in range(0, CELL+WALL):
						pixel[y+yOffSet][x+xOffSet] = 1
			# draw lower wall
			if cell == 0:
				for x in range(0, CELL):
					for y in range(CELL, CELL+WALL):
						pixel[y+yOffSet][x+xOffSet] = 0
			else:
				for x in range(0, CELL+WALL):
					for y in range(CELL, CELL+WALL):
						pixel[y+yOffSet][x+xOffSet] = 1
			# remove left wall if necessary
			if cell == 3:
				for x in range(-WALL, 0):
					for y in range(0, CELL):
						pixel[y+yOffSet][x+xOffSet] = 0
			else: pass
			# remove upper wall if necessary
			if cell == 6:
				for x in range(0, CELL):
					for y in range(-WALL, 0):
						pixel[y+yOffSet][x+xOffSet] = 0
			else: pass
			xOffSet += (WALL + CELL)
		yOffSet += (WALL + CELL)
	if True:
		# lower right
		for x in range(-WALL, 0):
			for y in range(-WALL-CELL, -WALL):
				pixel[y+yOffSet][x+xOffSet] = 0
		# uppper left
		for x in range(0, WALL):
			for y in range(WALL, WALL+CELL):
				pixel[y][x] = 0
	return pixel


# interface to generate 2D array
def generate(rows = X, cols = Y):
	m = [[-1 for x in range(rows)] for y in range(cols)]
	fill(m)
	return draw(m)


if __name__ == '__main__':
	try:
		x = int(sys.argv[1])
		y = int(sys.argv[2])
		pixel = generate(x, y)
	except:
		pixel = generate()
	
	import numpy as np
	import cv2
	a = np.asarray(pixel, dtype=np.uint8)
	a[a>0] = 100
	a[a==0]=255
	a[a==100]=0
	cv2.imshow('image', a)
	k = cv2.waitKey(0)
	if k:
    		cv2.destroyAllWindows()
