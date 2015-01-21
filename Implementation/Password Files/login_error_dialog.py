from C3_Media_DBMS import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *
	
import sys
import pdb

class LoginErrorDialog(QDialog):
	"""Error displayed when login password is incorrect"""
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Login Error")
		self.login_error_label = QLabel("Error, the password you entered is incorrect.")
		self.close_button = QPushButton("Close")

		self.login_error_layout = QGridLayout()
		self.close_layout = QHBoxLayout()
		self.close_layout.addWidget(self.close_button)

		self.close_widget = QWidget()
		self.close_widget.setLayout(self.close_layout)

		self.login_error_layout.addWidget(self.login_error_label,0,0)
		self.login_error_layout.addWidget(self.close_widget,1,1)


		self.setLayout(self.login_error_layout)

		self.close_button.clicked.connect(self.close)
		#self.returnPressed.connect(self.close)
