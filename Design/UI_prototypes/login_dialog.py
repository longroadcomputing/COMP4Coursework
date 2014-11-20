from main_menu_window import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *
    
import sys
import pdb

class LoginDialog(QDialog):
    """Error displayed when login password is incorrect"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Error")
        self.login_label = QLabel("Please enter the Password to access:")
        self.password_entry = QLineEdit()
        self.password_entry.setPlaceholderText("Password...")
        self.login_quit_button = QPushButton("Quit")
        self.login_enter_button = QPushButton("Enter")
        self.login_enter_button.autoDefault()

        #create layout
        self.login_layout = QVBoxLayout()
        self.login_buttons_layout = QHBoxLayout()
        #add widgets to layout
        self.login_layout.addWidget(self.login_label)
        self.login_layout.addWidget(self.password_entry)
        
        self.login_buttons_layout.addWidget(self.login_quit_button)
        self.login_buttons_layout.addWidget(self.login_enter_button)

        self.login_buttons_widget = QWidget()
        self.login_buttons_widget.setLayout(self.login_buttons_layout)
        self.login_layout.addWidget(self.login_buttons_widget)

        self.setLayout(self.login_layout)
        
        self.login_enter_button.clicked.connect(self.close)
        self.login_quit_button.clicked.connect(self.close)

    def get_login(self):
        return self.password_entry
                
