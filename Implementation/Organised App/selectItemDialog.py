from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys
import time

class SelectItemDialog(QDialog):
	"""docstring for SelectItemDialog"""
	def __init__(self, Date):
		super().__init__()

		self.Date = Date

		self.setWindowTitle("Select Item")

		self.titleLabel = QLabel("Please select an Item to add to the loan for {0} ".format(self.Date))


