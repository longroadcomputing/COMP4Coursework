from create_new_item_layout import *

from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys


class PreviewNewItemWidget(QWidget):
	"""docstring for PreviewNewItemWidget"""
	def __init__(self):
		super().__init__()
		self.heading = QLabel("New Item Preview")
		self.heading.setAlignment(Qt.AlignCenter)
		self.heading.setStyleSheet("font:18pt; font-weight:bold")
		
		self.item_name_heading = QLabel("Item Name:")
		#self.item_name_widget = 

		self.new_item_preview_layout = QVBoxLayout()
		self.new_item_preview_layout.addWidget(self.heading)
		self.new_item_preview_layout.addWidget(self.item_name_heading)