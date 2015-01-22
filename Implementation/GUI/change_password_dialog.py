from incorrect_current_password_dialog import *
from password_mismatch_dialog import *
from password_changed_dialog import *
from C3_Media_DBMS import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
	
import sys
import pdb

class ChangePasswordDialog(QDialog):
	def __init__(self,current_password):
		super().__init__()
		self.setWindowTitle("Change Password")
		self.current_password = current_password

		self.current_password_lineEdit = QLineEdit()
		self.current_password_lineEdit.setEchoMode(QLineEdit.Password)
		self.current_password_lineEdit.setPlaceholderText("Current Password")

		self.new_password_lineEdit = QLineEdit()
		self.new_password_lineEdit.setEchoMode(QLineEdit.Password)
		self.new_password_lineEdit.setPlaceholderText("New Password")

		self.confirm_new_password_lineEdit = QLineEdit()
		self.confirm_new_password_lineEdit.setEchoMode(QLineEdit.Password)
		self.confirm_new_password_lineEdit.setPlaceholderText("Confirm New Pasword")
		
		self.change_password_layout = QVBoxLayout()
		self.change_password_layout.addWidget(self.current_password_lineEdit)
		self.change_password_layout.addWidget(self.new_password_lineEdit)
		self.change_password_layout.addWidget(self.confirm_new_password_lineEdit)

		self.change_password_button = QPushButton("Change Password")
		self.cancel_button = QPushButton("Cancel")
		

		self.button_Layout = QHBoxLayout()
		self.button_Layout.addWidget(self.cancel_button)
		self.button_Layout.addWidget(self.change_password_button)

		self.button_widget = QWidget()
		self.button_widget.setLayout(self.button_Layout)

		self.change_password_layout.addWidget(self.button_widget)

		self.setLayout(self.change_password_layout)

		self.change_password_button.clicked.connect(self.close)
		self.cancel_button.clicked.connect(self.close)
		self.confirm_new_password_lineEdit.returnPressed.connect(self.change_password)

		self.cancel_button.setAutoDefault(False)
		self.change_password_button.setAutoDefault(True)
		self.cancel_button.setShortcut("Ctrl+W")
		
	def change_password(self):
		if self.current_password_lineEdit.text() != self.current_password:
			incorrect_current_password_dialog = IncorrectCurrentPasswordDialog()
			incorrect_current_password_dialog.exec_()
			return self.current_password
		elif self.new_password_lineEdit.text() != self.confirm_new_password_lineEdit.text():
			password_mismatch_dialog = PasswordMismatchDialog()
			password_mismatch_dialog.exec()
			return self.current_password
		elif self.current_password_lineEdit.text() == self.current_password and self.new_password_lineEdit.text() == self.confirm_new_password_lineEdit.text():
			self.new_password = self.confirm_new_password_lineEdit.text()
			if self.new_password == self.password:
					self.password = self.new_password
					update_password(self.password) 
					password_changed_dialog = PasswordChangedDialog()
					password_changed_dialog.exec_()
