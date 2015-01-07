from added_record_dialog import *
from added_record_dialog import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys
import pdb
import re

class NewCustomerWidget(QWidget):
    """docstring for NewCustomerWidgetQWidget"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("New Customer")
        
        self.forename_label = QLabel("Forename")
        self.get_forename = QLineEdit()

        self.surname_label = QLabel("Surname")
        self.get_surname = QLineEdit()

        self.company_label = QLabel("Company")
        self.get_company = QLineEdit()

        self.address_label = QLabel("Address")
        self.get_address = QLineEdit()

        self.town_label = QLabel("Town")
        self.get_town = QLineEdit()

        self.post_code_label = QLabel("Post-Code")
        self.get_post_code = QLineEdit()

        self.mobile_label = QLabel("Mobile")
        self.get_mobile = QLineEdit()

        self.landline_label = QLabel("Landline")
        self.get_landline = QLineEdit()

        self.email_label = QLabel("Email")
        self.get_email = QLineEdit()


        self.new_customer_layout = QVBoxLayout()
        self.new_customer_layout.addWidget(self.forename_label)
        self.new_customer_layout.addWidget(self.get_forename)

        self.new_customer_layout.addWidget(self.surname_label)
        self.new_customer_layout.addWidget(self.get_surname)

        self.new_customer_layout.addWidget(self.company_label)
        self.new_customer_layout.addWidget(self.get_company)

        self.new_customer_layout.addWidget(self.address_label)
        self.new_customer_layout.addWidget(self.get_address)

        self.new_customer_layout.addWidget(self.town_label)
        self.new_customer_layout.addWidget(self.get_town)

        self.new_customer_layout.addWidget(self.post_code_label)
        self.new_customer_layout.addWidget(self.get_post_code)

        self.new_customer_layout.addWidget(self.mobile_label)
        self.new_customer_layout.addWidget(self.get_mobile)

        self.new_customer_layout.addWidget(self.landline_label)
        self.new_customer_layout.addWidget(self.get_landline)

        self.new_customer_layout.addWidget(self.email_label)
        self.new_customer_layout.addWidget(self.get_email)

        
        self.cancel_button = QPushButton("Cancel")
        self.confirm_button = QPushButton("Confirm")

        self.customer_buttons_layout = QHBoxLayout()
        self.customer_buttons_layout.addWidget(self.cancel_button)
        self.customer_buttons_layout.addWidget(self.confirm_button)

        self.customer_buttons_widget = QWidget()
        self.customer_buttons_widget.setLayout(self.customer_buttons_layout)

        self.new_customer_layout.addWidget(self.customer_buttons_widget)

def diable_widget(self):
    self.get_forename.setEnabled(False)
    self.get_surname.setEnabled(False)
    self.get_company.setEnabled(False)
    self.get_address.setEnabled(False)
    self.get_town.setEnabled(False)
    self.get_post_code.setEnabled(False)
    self.get_mobile.setEnabled(False)
    self.get_landline.setEnabled(False)
    self.get_email.setEnabled(False)
    self.cancel_button.setEnabled(False)
    self.confirm_button.setEnabled(False)


def enable_widget(self):
    self.get_forename.setEnabled(True)
    self.get_surname.setEnabled(True)
    self.get_company.setEnabled(True)
    self.get_address.setEnabled(True)
    self.get_town.setEnabled(True)
    self.get_post_code.setEnabled(True)
    self.get_mobile.setEnabled(True)
    self.get_landline.setEnabled(True)
    self.get_email.setEnabled(True)
    self.cancel_button.setEnabled(True)
    self.confirm_button.setEnabled(True)


