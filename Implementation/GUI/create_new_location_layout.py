from added_record_dialog import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys
import pdb
import re

class NewLocation(QWidget):
    """docstring for NewLocation"""
    def __init__(self):
        super().__init__()

        self.location_label = QLabel("Location")
        self.get_location_name = QLineEdit()
        self.get_location_name.setPlaceholderText("Enter Location")
        self.cancel_button = QPushButton("Cancel")
        self.confirm_button = QPushButton("Confirm")

        self.enter_location_layout = QVBoxLayout()
        self.enter_location_layout.addWidget(self.location_label)
        self.enter_location_layout.addWidget(self.get_location_name)
        self.enter_location_widget = QWidget()
        self.enter_location_widget.setLayout(self.enter_location_layout)

        self.location_buttons_layout = QHBoxLayout()
        self.location_buttons_layout.addWidget(self.cancel_button)
        self.location_buttons_layout.addWidget(self.confirm_button)

        self.location_buttons_widget = QWidget()
        self.location_buttons_widget.setLayout(self.location_buttons_layout)

        self.new_location_layout = QVBoxLayout()
        self.new_location_layout.addWidget(self.enter_location_widget)
        self.new_location_layout.addWidget(self.location_buttons_widget)

            
