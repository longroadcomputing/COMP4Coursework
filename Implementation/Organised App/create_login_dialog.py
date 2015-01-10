from PyQt4.QtCore import *
from PyQt4.QtGui import *
	
import sys
import pdb

class LoginDialog(QDialog):
	"""Error displayed when login password is incorrect"""
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Login")
		self.login_label = QLabel("Please enter the Password to access:")
		self.password_entry = QLineEdit()
		self.password_entry.setEchoMode(QLineEdit.Password)

		self.login_button = QPushButton("Login")
		self.quit_button = QPushButton("Quit")
		self.buttons_widget = QWidget()

		#create layout
		self.login_layout = QVBoxLayout()
		self.login_buttons_layout = QHBoxLayout()

		self.login_buttons_layout.addWidget(self.quit_button)
		self.login_buttons_layout.addWidget(self.login_button)

		self.buttons_widget.setLayout(self.login_buttons_layout)
		#add widgets to layout
		self.login_layout.addWidget(self.login_label)
		self.login_layout.addWidget(self.password_entry)
		self.login_layout.addWidget(self.buttons_widget)

		self.setLayout(self.login_layout)

		self.quit_button.setAutoDefault(False)
		self.login_button.setAutoDefault(True)

		self.password_entry.returnPressed.connect(self.close)
		self.login_button.clicked.connect(self.close)
		self.quit_button.clicked.connect(self.close)
		self.quit_button.setShortcut('Ctrl+W')


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

		

def login_dialog_main():
	application = QApplication(sys.argv)
	window = LoginDialog()
	window.show()
	window.raise_()
	application.exec_()
				
if __name__ == '__main__':
	login_dialog_main()
