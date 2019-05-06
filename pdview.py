#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPolygonF, QPolygon, QColor, QBrush
from PyQt5.QtCore import Qt, QPointF, QPoint
import sys, random
import math


STEP_MOVE = 10
STEP_ROTATE = 8

class display(QWidget):
	def __init__(self, level, player):
		super().__init__()
		self.width = level.X
		self.height = level.Y
		self.diagonal = math.hypot(self.width, self.height)
		self.initUI()
		self.level = level
		self.player = player
		self.X = 130
		self.Y = 150
		self.direction = 146
		self.dt = 1

	def initUI(self):	  
		self.setGeometry(300, 300, self.width, self.height)
		self.setWindowTitle('Raycasting')
		self.show()
	
	def keyPressEvent(self, event):
		key = event.key()
		if key == Qt.Key_Left:
			self.X -= STEP_MOVE
		elif key == Qt.Key_Right:
			self.X += STEP_MOVE
		elif key == Qt.Key_Down:
			self.Y += STEP_MOVE
		elif key == Qt.Key_Up:
			self.Y -= STEP_MOVE
		elif key == Qt.Key_Q:
			self.updateDirection(STEP_ROTATE)
		elif key == Qt.Key_E:
			self.updateDirection(-STEP_ROTATE)
		else:
			pass
		self.update()

	def updateDirection(self, delta):
		old = self.direction + delta
		if old < -180: old += 360
		elif old > 180: old -= 360
		else: pass
		self.direction = old

		if old == 0: self.dt = 1
		elif old == -90: self.dt = math.tan(math.radians(-89))
		elif old == 90: self.dt = math.tan(math.radians(89))
		elif old == -180: self.dt = math.tan(math.radians(-179))
		elif old == 180: self.dt = math.tan(math.radians(179))
		else: self.dt = math.tan(math.radians(old))

		
	def paintEvent(self, e):
		qp = QPainter(self)
		#qp.begin(self)
		X = self.X 
		Y = self.Y
		qp.setPen(Qt.black)	# mark standing point
		qp.drawPoint(X, Y)
		#qp.drawLine(0,self.height/2,self.width, self.height/2)
		
		direction = self.direction
		gamma = self.player.hview
		alpha = self.player.vview
		qp.setPen(Qt.green)
		drawx_counter = 0
		last_low = 0; last_high = 0; last_x = 0
		#print('angel%d'%direction)
		for ray in range(1, self.width + 1): # range(-gamma//2, gamma//2+1):
			theta = gamma / self.width * ray - gamma / 2
			x = X; y = Y; dx = 1; dy = dx * math.tan(math.radians(theta))
			qp.setPen(Qt.green)
			path_counter = 0
			while x < self.width and x > -10 and y < self.height and y > -10 and self.level.level[int(x)][int(y)].high == 0:
				dt = self.dt 
				if direction >= 0:
					y = y + dy + dx/dt
					x = x + dx - dy/dt
				else:
					y = y - dy - dx/dt
					x = x - dx + dy/dt
				if path_counter % 2 == 0:
					qp.drawPoint(x, y)
				path_counter += 1
			qp.setPen(Qt.red)
			qp.drawPoint(x, y)
			
			p = abs((y-Y) * math.cos(math.radians(theta-direction))) + abs( (x-X) * math.sin(math.radians(theta-direction)))
			#p = math.hypot(x - X, y - Y)	# slow but more intuitive
			#p = abs( p * math.cos(math.radians(theta)))
			if p == 0: continue # the case when player is outside map
			
			wall = 60
			halfview = abs(p * math.tan(alpha/2))
			if halfview > wall - self.player.height: # ceiling
				upperview = (wall - self.player.height) / halfview 
			else:	# sees entire upper part of wall
				upperview = 1 / 2

			if halfview > self.player.height:	# sees floor
				lowerview = self.player.height / halfview / 2
			else:	# sees entire lower part of wall
				lowerview = 1 / 2
			#adrawx = round(self.width/gamma * drawx_counter)
			drawx = drawx_counter
			#print(self.height/2 + self.height * upperview, self.height/2 - self.height * lowerview)
			drawy_low = self.height/2 - self.height * upperview
			drawy_high = self.height/2 + self.height * lowerview
			if drawx_counter > 0:	# first line on the left is omitted
				polygon = QPolygonF()
				polygon.append(QPointF(last_x, last_low))
				polygon.append(QPointF(last_x, last_high))
				polygon.append(QPointF(drawx, drawy_high))
				polygon.append(QPointF(drawx, drawy_low))
				wallcolor = QColor(255,p/self.diagonal*255,  p/self.diagonal*255)
				qp.setPen(wallcolor)
				qp.drawConvexPolygon(polygon)
				qp.setBrush(QBrush(wallcolor))
	
			last_low = drawy_low
			last_high = drawy_high
			last_x = drawx
			#qp.drawLine(drawx, self.height/2 - self.height * upperview, drawx, self.height/2 + self.height * lowerview)
			drawx_counter += 1
		qp.end()
		
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = display()
	sys.exit(app.exec_())
