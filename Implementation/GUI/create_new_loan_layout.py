from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys

class NewLoanWidget(QWidget):
	"""widget to display the NewLoanWidget"""
	def __init__(self):
		super().__init__()

		self.select_customer_label = QLabel("Select Customer:")
		self.select_customer_drop_down = QComboBox()
