#!/usr/bin/python3

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
import sys

"""
The QPen is an elementary graphics object. It is used to draw lines,
curves and outlines of rectangles, ellipses, polygons, or other shapes.
"""
	
class Example(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.setGeometry(300, 300, 280, 270)
		self.setWindowTitle('Pen styles')
		self.show()

	def paintEvent(self, e):
		qp = QPainter()
		qp.begin(self)
		self.drawLines(qp)
		qp.end()

	def drawLines(self, qp):
		pen = QPen(Qt.black, 2, Qt.SolidLine)

		qp.setPen(pen)
		# SolidLine
		qp.drawLine(20, 40, 250, 40)

		pen.setStyle(Qt.DashLine)
		qp.setPen(pen)
		# DashLine
		qp.drawLine(20, 80, 250, 80)

		pen.setStyle(Qt.DashDotLine)
		qp.setPen(pen)
		# DashDotLine
		qp.drawLine(20, 120, 250, 120)

		pen.setStyle(Qt.DotLine)
		qp.setPen(pen)
		# DotLine
		qp.drawLine(20, 160, 250, 160)

		pen.setStyle(Qt.DashDotDotLine)
		qp.setPen(pen)
		# DashDotDotLine
		qp.drawLine(20, 200, 250, 200)

		pen.setStyle(Qt.CustomDashLine)
		# Our pattern is 1px dash, 4px space, 5px dash, 4px space etc.
		pen.setDashPattern([1, 4, 5, 4])
		qp.setPen(pen)
		# CustomDashLine
		qp.drawLine(20, 240, 250, 240)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())
