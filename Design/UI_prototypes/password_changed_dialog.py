from main_menu_window import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *
    
import sys
import pdb

class PasswordChangedDialog(QDialog):
    """Error displayed when login password is incorrect"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password")
        self.password_changed_label = QLabel("Password changed successfully.")
        self.close_button = QPushButton("Close")

        self.password_changed_layout = QGridLayout()
        self.close_layout = QHBoxLayout()
        self.close_layout.addWidget(self.close_button)

        self.close_widget = QWidget()
        self.close_widget.setLayout(self.close_layout)

        self.password_changed_layout.addWidget(self.password_changed_label,0,0)
        self.password_changed_layout.addWidget(self.close_widget,1,1)


        self.setLayout(self.password_changed_layout)

        self.close_button.clicked.connect(self.close)
        #self.returnPressed.connect(self.close)
