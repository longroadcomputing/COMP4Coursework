from incorrect_current_password_dialog import *
from password_mismatch_dialog import *
from password_changed_dialog import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
	
import sys
import pdb

class DisplayCreatedRecordDialog(QDialog):
	def __init__(self,string):
		super().__init__()
		self.setWindowTitle("Added Record")
		self.string = string

		self.added_record_label = QLabel("""The following record was added successfully:
											""")
		self.display_record_added = QLabel(self.string)
		self.close_button = QPushButton("Close")

		self.created_record_layout = QGridLayout()
		self.close_layout = QHBoxLayout()
		self.close_layout.addWidget(self.close_button)

		self.close_widget = QWidget()
		self.close_widget.setLayout(self.close_layout)

		self.created_record_layout.addWidget(self.added_record_label,0,0)
		self.created_record_layout.addWidget(self.display_record_added,1,0)
		self.created_record_layout.addWidget(self.close_widget,1,1)


		self.setLayout(self.created_record_layout)

		self.close_button.clicked.connect(self.close_window)

	def close_window(self):
		self.close()

