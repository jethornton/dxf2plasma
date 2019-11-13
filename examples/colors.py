#!/usr/bin/python3

from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush
import sys

"""
A colour is an object representing a combination of Red, Green, and Blue
(RGB) intensity values. Valid RGB values are in the range from 0 to 255.
We can define a colour in various ways. The most common are RGB decimal
values or hexadecimal values. We can also use an RGBA value which stands
for Red, Green, Blue, and Alpha. Here we add some extra information
regarding transparency. Alpha value of 255 defines full opacity, 0 is
for full transparency, e.g. the colour is invisible.
"""

class Example(QWidget):
	def __init__(self):
		super().__init__()

		self.initUI()

	def initUI(self):
		self.setGeometry(300, 300, 350, 100)
		self.setWindowTitle('Colors')
		self.show()

	def paintEvent(self, e):
		qp = QPainter()
		qp.begin(self)
		self.drawRectangles(qp)
		qp.end()

	def drawRectangles(self, qp):
		col = QColor(0, 0, 0)
		# Here we define a color using a hexadecimal notation.
		col.setNamedColor('#d4d4d4')
		# Here we define a brush and draw a rectangle.
		# A brush is an elementary graphics object
		# which is used to draw the background of a shape.
		# The drawRect() method accepts four parameters.
		qp.setPen(col)

		qp.setBrush(QColor(200, 0, 0))
		# The method draws the rectangle using the current pen and brush.
		qp.drawRect(10, 15, 90, 60)

		qp.setBrush(QColor(255, 80, 0, 160))
		qp.drawRect(130, 15, 90, 60)

		qp.setBrush(QColor(25, 0, 90, 200))
		qp.drawRect(250, 15, 90, 60)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())
