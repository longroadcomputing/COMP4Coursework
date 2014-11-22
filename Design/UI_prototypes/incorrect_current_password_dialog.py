from main_menu_window import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *
    
import sys
import pdb

class IncorrectCurrentPasswordDialog(QDialog):
    """Error displayed when login password is incorrect"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Error")
        self.incorrect_current_password_label = QLabel("Incorrect current password entered.")
        self.close_button = QPushButton("Close")

        self.incorrect_current_password_layout = QGridLayout()
        self.close_layout = QHBoxLayout()
        self.close_layout.addWidget(self.close_button)

        self.close_widget = QWidget()
        self.close_widget.setLayout(self.close_layout)

        self.incorrect_current_password_layout.addWidget(self.incorrect_current_password_label,0,0)
        self.incorrect_current_password_layout.addWidget(self.close_widget,1,1)


        self.setLayout(self.incorrect_current_password_layout)

        self.close_button.clicked.connect(self.close)
        #self.returnPressed.connect(self.close)
