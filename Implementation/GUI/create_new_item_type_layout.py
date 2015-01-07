from added_record_dialog import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys
import pdb
import re


class NewItemType(QWidget):
	"""docstring for NewItemTypeQWidget"""
	def __init__(self):
		super().__init__()
		
		self.item_type_label = QLabel("Item Type")
		self.get_item_type = QLineEdit()
		self.get_item_type.setPlaceholderText("Enter Item Type")
		self.cancel_button = QPushButton("Cancel")
		self.confirm_button = QPushButton("Confirm")

		self.enter_item_type_layout = QVBoxLayout()
		self.enter_item_type_layout.addWidget(self.item_type_label)
		self.enter_item_type_layout.addWidget(self.get_item_type)
		self.enter_item_type_widget = QWidget()
		self.enter_item_type_widget.setLayout(self.enter_item_type_layout)

		self.item_type_buttons_layout = QHBoxLayout()
		self.item_type_buttons_layout.addWidget(self.cancel_button)
		self.item_type_buttons_layout.addWidget(self.confirm_button)

		self.item_type_buttons_widget = QWidget()
		self.item_type_buttons_widget.setLayout(self.item_type_buttons_layout)

		self.new_item_type_layout = QVBoxLayout()
		self.new_item_type_layout.addWidget(self.enter_item_type_widget)
		self.new_item_type_layout.addWidget(self.item_type_buttons_widget)

