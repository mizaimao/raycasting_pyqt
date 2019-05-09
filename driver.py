#!/usr/bin/env python3

import pdplayer
import pdmap
import pdmaze
import pdview
from PyQt5.QtWidgets import QWidget, QApplication
import sys

if __name__ == '__main__':
	player = pdplayer.player(location=[300,300], height=1,hview=90, vview = 60)
	level = pdmap.level_by_block(400, 600,20)
	level.add_block(startX=20, startY=180, lengthX=100, lengthY=100)
	level.add_block(startX=180, startY=180, lengthX=100, lengthY=100)
	level.add_block(startX=480, startY=180, lengthX=100, lengthY=100)
	#pixel = pdmaze.generate(X = 16 , Y = 10) # cell count, not pixel
	#level = pdmap.level_by_list(pixel)
	app = QApplication(sys.argv)
	view = pdview.display(level, player)
	sys.exit(app.exec_())
