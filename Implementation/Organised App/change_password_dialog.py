from Main import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
	
import sys
import pdb

import re

class ChangePasswordDialog(QDialog):
	def __init__(self,parent,current_password):
		super().__init__()
		self.parent = parent
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

		self.cancel_button.setAutoDefault(False)
		self.cancel_button.setDefault(False)
		self.cancel_button.setShortcut("Ctrl+W")
		self.cancel_button.setShortcut("Esc")
		
		self.change_password_button.setAutoDefault(True)
		self.change_password_button.setDefault(True)
		self.change_password_button.setShortcut('Return')

		self.change_password_button.clicked.connect(self.validatePasswords)
		self.cancel_button.clicked.connect(self.close)


		self.confirm_new_password_lineEdit.textChanged.connect(self.validateNewPassword)

	def addConnection(self, connection):
		self.connection = connection
		return True

	def validateOldPassword(self):
		if self.current_password_lineEdit.text() == self.current_password:
			return True
		else:
			return False

	def validateNewPassword(self):
		if self.confirm_new_password_lineEdit.text() == self.new_password_lineEdit.text():
			self.confirm_new_password_lineEdit.setStyleSheet("background-color:#c4df9b")
			return True
		else:
			self.confirm_new_password_lineEdit.setStyleSheet("background-color:#f6989d")
			print(False)
		
		
	def validatePasswords(self):
		validOldPassword = self.validateOldPassword()
		newPassword = self.new_password_lineEdit.text()
		if validOldPassword == False:
			text = "Old Password is Wrong."
			QMessageBox.information(self, "Error! Password not Updated!", text)
			self.parent.statusBar.showMessage("Password not updated")
		else:
			if self.confirm_new_password_lineEdit.text() != self.new_password_lineEdit.text():
				text = "Passwords do not match."
				QMessageBox.information(self, "Error! Password not Updated!", text)
				self.parent.statusBar.showMessage("Password not updated")
				
			newPasswordRegEx = re.compile("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{6,}$")
			match = newPasswordRegEx.match(newPassword)
			if not match or self.current_password == self.new_password_lineEdit:
				self.error_message_dialog = QMessageBox()
				self.error_message_dialog.setFixedWidth(200)
				self.error_message_dialog.setWindowTitle("Input Error")
				self.error_message_dialog.setText("Error! Password Not Updated\n"
												  "\n"
												  "Click the 'Show details' button for more information")
				self.error_message_dialog.setDetailedText("Password must not be your old password and must: \n \n 1. Be at least 6 characters long.\n 2. Contain an upper and lowercase letter.\n 3. Contain at least a single digit number.\n  4. Contain at least one special character.")
				self.error_message_dialog.setIcon(QMessageBox.Warning)
				self.okay_button = self.error_message_dialog.addButton(self.parent.tr("Okay"), QMessageBox.AcceptRole)
				self.error_message_dialog.setEscapeButton(self.okay_button)
				self.error_message_dialog.setDefaultButton(self.okay_button)
				self.error_message_dialog.exec_()
				self.parent.statusBar.showMessage("Password not updated")
			else:
				self.updatePassword()

	def updatePassword(self):
		newPassword = self.new_password_lineEdit.text()
		
		updatePassword = self.connection.updatePassword(newPassword)

		if not updatePassword:
			self.error_message_dialog = QMessageBox()
			self.error_message_dialog.setFixedWidth(200)
			self.error_message_dialog.setWindowTitle("Error")
			self.error_message_dialog.setText("Error! Failed to update Password\n"
							  "\n"
							  "Click the 'Show details' button for more information")
			self.error_message_dialog.setDetailedText("Database Error:\n \n "
								  "{0}".format(self.connection.error))
			self.error_message_dialog.setIcon(QMessageBox.Warning)
			self.okay_button = self.error_message_dialog.addButton(self.parent.tr("Okay"), QMessageBox.AcceptRole)
			self.error_message_dialog.setEscapeButton(self.okay_button)
			self.error_message_dialog.setDefaultButton(self.okay_button)
			self.error_message_dialog.exec_()
			self.parent.statusBar.showMessage("Password not updated ({0})".format(self.connection.error))
		else:
			text = "You will now be logged out."
			QMessageBox.information(self, "Password Changed", text)
			self.parent.statusBar.showMessage("Password updated")
			self.close()
			self.parent.logout()
		
