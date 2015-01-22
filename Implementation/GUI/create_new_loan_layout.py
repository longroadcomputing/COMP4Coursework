from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys

class NewLoanWidget(QWidget):
	"""widget to display the NewLoanWidget"""
	def __init__(self):
		super().__init__()

		self.setProperty("newLoanClass", "True")

		#self.parent = parent

		self.setFixedWidth(800)

		self.leftWidget = QWidget()

		self.setLayout(self.mainLayout)

		self.setStyleSheet("QWidget[newLoanClass=True]{padding:100px;}")

