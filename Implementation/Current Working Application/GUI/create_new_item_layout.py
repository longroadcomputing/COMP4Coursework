from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys

class NewItemWidget(QWidget):
    """widget to display the NewItemWidget"""
    def __init__(self):
        super().__init__()

        #create widgets
        self.item_name_label = QLabel("Item Name:")
        self.item_name_line_edit = QLineEdit()

        self.item_value_label = QLabel("Item Value:")
        self.item_value_line_edit = QLineEdit()

        self.item_loan_rate_label = QLabel("Loan Rate:")
        self.item_loan_rate_line_edit = QLineEdit()

        self.item_class_label = QLabel("Item Class:")
        self.item_class_drop_down = QComboBox()

        self.item_class_drop_down.addItem("Please select...")
        self.item_class_drop_down.addItem("1")
        self.item_class_drop_down.addItem("2")

        j = self.item_class_drop_down.model().index(0,0)
        self.item_class_drop_down.model().setData(j, 0, Qt.UserRole-1)


        self.fuse_rating_label = QLabel("Fuse Rating:")
        self.fuse_rating_drop_down = QComboBox()

        self.fuse_rating_drop_down.addItem("Please select...")
        self.fuse_rating_drop_down.addItem("-")
        self.fuse_rating_drop_down.addItem("0")
        self.fuse_rating_drop_down.addItem("3")
        self.fuse_rating_drop_down.addItem("5")
        self.fuse_rating_drop_down.addItem("7")
        self.fuse_rating_drop_down.addItem("10")
        self.fuse_rating_drop_down.addItem("13")

        j = self.fuse_rating_drop_down.model().index(0,0)
        self.fuse_rating_drop_down.model().setData(j, 0, Qt.UserRole-1)



        self.item_type_label = QLabel("Item Type:")
        self.item_type_drop_down = QComboBox()

        self.item_type_drop_down.addItem("Please select...")
        self.item_type_drop_down.addItem("Audio")
        self.item_type_drop_down.addItem("Cabling")
        self.item_type_drop_down.addItem("Control Desks")
        self.item_type_drop_down.addItem("Lighting")
        self.item_type_drop_down.addItem("Miscallaneous")
        self.item_type_drop_down.addItem("Power")
        self.item_type_drop_down.addItem("Software")
        self.item_type_drop_down.addItem("Staging")
        self.item_type_drop_down.addItem("Storage/Hardware")
        self.item_type_drop_down.addItem("Visual")

        j = self.item_type_drop_down.model().index(0,0)
        self.item_type_drop_down.model().setData(j, 0, Qt.UserRole-1)



        self.location_label = QLabel("Location:")
        self.location_drop_down = QComboBox()

        self.location_drop_down.addItem("Please select...")
        self.location_drop_down.addItem("Alpha Terrace")
        self.location_drop_down.addItem("C3 Centre")
        self.location_drop_down.addItem("Cineworld")
        self.location_drop_down.addItem("St. Bedes")

        j = self.location_drop_down.model().index(0,0)
        self.location_drop_down.model().setData(j, 0, Qt.UserRole-1)




        #create layout and add wigets
        self.item_layout = QVBoxLayout()
        self.item_layout.addWidget(self.item_name_label)
        self.item_layout.addWidget(self.item_name_line_edit)

        self.item_layout.addWidget(self.item_value_label)
        self.item_layout.addWidget(self.item_value_line_edit)
        
        self.item_layout.addWidget(self.item_loan_rate_label)
        self.item_layout.addWidget(self.item_loan_rate_line_edit)
        
        self.item_layout.addWidget(self.item_class_label)
        self.item_layout.addWidget(self.item_class_drop_down)

        self.item_layout.addWidget(self.fuse_rating_label)
        self.item_layout.addWidget(self.fuse_rating_drop_down)

        self.item_layout.addWidget(self.item_type_label)
        self.item_layout.addWidget(self.item_type_drop_down)

        self.item_layout.addWidget(self.location_label)
        self.item_layout.addWidget(self.location_drop_down)

        self.cancel_button = QPushButton("Cancel")
        self.confirm_button = QPushButton("Enter")
        
        self.confirm_button.setShortcut("Enter")

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.addWidget(self.cancel_button)
        self.buttons_layout.addWidget(self.confirm_button)

        self.buttons_widget = QWidget()
        self.buttons_widget.setLayout(self.buttons_layout)

        self.item_layout.addWidget(self.buttons_widget)

        self.cancel_button.setAutoDefault(False)
        self.confirm_button.setAutoDefault(True)
        self.cancel_button.setDefault(False)
        self.confirm_button.setDefault(True)
    
    def enable_edit_new_item(self):
        self.item_name_line_edit.setEnabled(True)
        self.item_value_line_edit.setEnabled(True)
        self.item_loan_rate_line_edit.setEnabled(True)
        self.item_class_drop_down.setEnabled(True)
        self.fuse_rating_drop_down.setEnabled(True)
        self.item_type_drop_down.setEnabled(True)
        self.location_drop_down.setEnabled(True)
        self.cancel_button.setEnabled(True)
        self.confirm_button.setEnabled(True)

    def disable_edit_new_item(self):
        self.item_name_line_edit.setEnabled(False)
        self.item_value_line_edit.setEnabled(False)
        self.item_loan_rate_line_edit.setEnabled(False)
        self.item_class_drop_down.setEnabled(False)
        self.fuse_rating_drop_down.setEnabled(False)
        self.item_type_drop_down.setEnabled(False)
        self.location_drop_down.setEnabled(False)
        self.cancel_button.setEnabled(False)
        self.confirm_button.setEnabled(False)

    def clear_widgets(self):
        self.item_name_line_edit.clear()
        self.item_value_line_edit.clear()
        self.item_loan_rate_line_edit.clear()

        

