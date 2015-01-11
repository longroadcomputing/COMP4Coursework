from added_record_dialog import *
from date_widget import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys
import pdb
import re

class NewPatTestWidget(QWidget):
	"""docstring for NewPatTestWidget"""
	def __init__(self):
		super().__init__()

		self.date_label = QLabel("Please select a date:")
		self.date_widget = DateWidget()
		self.buttons_widget = QWidget()

		self.cancel_button = QPushButton("Cancel")
		self.enter_button = QPushButton("Enter")

		self.buttons_layout = QHBoxLayout()
		self.buttons_layout.addWidget(self.cancel_button)
		self.buttons_layout.addWidget(self.enter_button)

		self.buttons_widget.setLayout(self.buttons_layout)

		self.pat_test_layout = QVBoxLayout()
		self.pat_test_layout.addWidget(self.date_label)
		self.pat_test_layout.addWidget(self.date_widget)
		self.pat_test_layout.addWidget(self.buttons_widget)

	def disable_widget(self):
		self.date_label.setEnabled(False)
		self.date_widget.setEnabled(False)
		self.buttons_widget.setEnabled(False)

	def enable_widget(self):
		self.date_label.setEnabled(True)
		self.date_widget.setEnabled(True)
		self.buttons_widget.setEnabled(True)

