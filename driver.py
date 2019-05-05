#!/usr/bin/env python3

import pdplayer
import pdmap
import pdview
from PyQt5.QtWidgets import QWidget, QApplication
import sys

if __name__ == '__main__':
	player = pdplayer.player(location=[300,300], height=1,hview=90, vview = 60)
	level = pdmap.level_class()
	level.add_block()
	app = QApplication(sys.argv)
	view = pdview.display(level, player)
	sys.exit(app.exec_())
