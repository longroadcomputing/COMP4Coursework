from create_login_dialog import *
from login_error_dialog import *
from change_password_dialog import *
from password_reset import *


from create_main_layout import *
from create_new_item_layout import *
from create_new_customer_layout import *
from create_new_loan_layout import *
from create_pat_test_layout import *

from display_entry_error_dialog import *
from added_record_dialog import *
from radio_button_dialog_class import *
from printing import *
from SQLController import *

# from insert_records_menu import *
# from update_records_menu import *
# from display_records_menu import *
# from delete_records_menu import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys
import pdb
import re
import time

class C3MediaDBMS(QMainWindow):
    """docstring for C3MediaDBMS"""
    def __init__(self):
        super().__init__()

        self.setWindowTitle("C3 Media Database Management Systems")
        self.resize(0,500)
        self.move(536,250)
        #self.icon = QIcon(QPixmap("./icon.png"))
        #self.setWindowIcon(self.icon)

        #Connection Attribute stores the database connection
        self.connection = None
        self.access = False
        
        #stacked layout
        self.stacked_layout = QStackedLayout()

        self.widget = QWidget()

        self.widget.setLayout(self.stacked_layout)

        #Set the central widget to the stacked layout

        self.setCentralWidget(self.widget)

        #Add the Menu Bar and Main Settings Etc...
        self.settings()

        self.create_start_screen()
        self.create_logged_in_screen()
        self.create_new_item()
        self.create_new_customer()
        self.create_new_loan()
        self.create_new_pat_test()

        self.enable_actions()
        self.disable_actions()

        #add action connections
        self.connections()

    def disable_actions(self):
        #file actions
        self.open.setEnabled(True) 
        self.new.setEnabled(False)
        self.Print.setEnabled(False)
        self.change_password.setEnabled(False)
        self.logout_action.setEnabled(False)

        #edit actions
        self.cut.setEnabled(False)
        self.copy.setEnabled(False)
        self.paste.setEnabled(False)
        self.select_all.setEnabled(False)

        #item actions
        self.add_item.setEnabled(False)
        self.display_item.setEnabled(False)
        self.delete_item.setEnabled(False)

        #customer actions
        self.add_customer.setEnabled(False)
        self.display_customer.setEnabled(False)
        self.delete_customer.setEnabled(False)

        #loan actions
        self.add_loan.setEnabled(False)
        self.display_loan.setEnabled(False)
        self.delete_loan.setEnabled(False)

        #pat_test actions
        self.add_pat_test.setEnabled(False)
        self.display_pat_test.setEnabled(False)
        self.delete_pat_test.setEnabled(False)

        #help actions
        self.help.setEnabled(False)
        self.about.setEnabled(True)

        #database actions
        self.open.setEnabled(True)
        self.closeDatabase.setEnabled(False)

    def enable_actions(self):
        #file actions
        self.open.setEnabled(True) 
        self.new.setEnabled(True)
        self.Print.setEnabled(True)
        self.change_password.setEnabled(True)
        self.logout_action.setEnabled(True)

        #edit actions
        self.cut.setEnabled(True)
        self.copy.setEnabled(True)
        self.paste.setEnabled(True)
        self.select_all.setEnabled(True)

        #item actions
        self.add_item.setEnabled(True)
        self.display_item.setEnabled(True)
        self.delete_item.setEnabled(True)

        #customer actions
        self.add_customer.setEnabled(True)
        self.display_customer.setEnabled(True)
        self.delete_customer.setEnabled(True)

        #loan actions
        self.add_loan.setEnabled(True)
        self.display_loan.setEnabled(True)
        self.delete_loan.setEnabled(True)

        #pat_test actions
        self.add_pat_test.setEnabled(True)
        self.display_pat_test.setEnabled(True)
        self.delete_pat_test.setEnabled(True)

        #help actions
        self.help.setEnabled(True)
        self.about.setEnabled(True)

        #database actions
        self.open.setEnabled(False)
        self.closeDatabase.setEnabled(True)

    def settings(self):
    	#file actions
        self.open = QAction("Open Database", self)
        self.closeDatabase = QAction("Close Database", self)
        self.new = QAction("New", self)
        self.Print = QAction("Print", self)
        self.change_password = QAction("Change Password", self)
        self.logout_action = QAction("Logout", self)

        #edit actions
        self.cut = QAction("Cut", self)
        self.copy = QAction("Copy", self)
        self.paste = QAction("Paste...", self)
        self.select_all = QAction("Select All", self)

        #item actions
        self.add_item = QAction('Add Item', self)
        self.display_item = QAction('Display Item', self)
        self.delete_item = QAction('Delete Item', self)

        #customer actions
        self.add_customer = QAction('Add Customer', self)
        self.display_customer = QAction('Display Customer', self)
        self.delete_customer = QAction('Delete Customer', self)

        #loan actions
        self.add_loan = QAction('Add Loan', self)
        self.display_loan = QAction('Display Loan', self)
        self.delete_loan = QAction('Delete Loan', self)

        #pat_test actions
        self.add_pat_test = QAction('Add Pat Test', self)
        self.display_pat_test = QAction('Display Pat Test', self)
        self.delete_pat_test = QAction('Delete Pat Test', self)

        #help action
        self.help = QAction('Help', self)
        self.about = QAction('About', self)

        #menubar
        self.menubar = QMenuBar()

        #add file menu and add actions to file menu
        self.file_menu = self.menubar.addMenu("File")
        self.file_menu.addAction(self.open)
        self.file_menu.addAction(self.new)
        self.file_menu.addAction(self.Print)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.change_password)
        self.file_menu.addAction(self.logout_action)

        #file menu shortcuts
        self.open.setShortcut('Ctrl+O')
        self.new.setShortcut('Ctrl+N')
        self.Print.setShortcut('Ctrl+P')

        #add edit menu and add actions to edit menu
        self.edit_menu = self.menubar.addMenu("Edit")
        self.edit_menu.addAction(self.cut)
        self.edit_menu.addAction(self.copy)
        self.edit_menu.addAction(self.paste)
        self.edit_menu.addAction(self.select_all)

        #edit menu shortcuts
        self.cut.setShortcut('Ctrl+X')
        self.copy.setShortcut('Ctrl+C')
        self.paste.setShortcut('Ctrl+V')
        self.select_all.setShortcut('Ctrl+A')

        #item menu
        self.item_menu = self.menubar.addMenu("Item")
        self.item_menu.addAction(self.add_item)
        self.item_menu.addAction(self.display_item)
        self.item_menu.addAction(self.delete_item)

        #customer menu
        self.customer_menu = self.menubar.addMenu("Customer")
        self.customer_menu.addAction(self.add_customer)
        self.customer_menu.addAction(self.display_customer)
        self.customer_menu.addAction(self.delete_customer)

        #loan menu
        self.loan_menu = self.menubar.addMenu("Loan")
        self.loan_menu.addAction(self.add_loan)
        self.loan_menu.addAction(self.display_loan)
        self.loan_menu.addAction(self.delete_loan)

        #pat test menu
        self.pat_test_menu = self.menubar.addMenu("Pat Test")
        self.pat_test_menu.addAction(self.add_pat_test)
        self.pat_test_menu.addAction(self.display_pat_test)
        self.pat_test_menu.addAction(self.delete_pat_test)

        #help menu
        self.help_menu = self.menubar.addMenu("Help")
        self.help_menu.addAction(self.help)
        self.help_menu.addAction(self.about)

        #create menubar
        self.setMenuBar(self.menubar)

        #tool bar
        self.toolBar = QToolBar()
        self.toolBar.addSeparator()

        #item toolbar actions
        self.toolBar.addAction(self.add_item)
        self.toolBar.addAction(self.display_item)
        self.toolBar.addAction(self.delete_item)
        self.toolBar.addSeparator()

        #customer toolbar action
        self.toolBar.addAction(self.add_customer)
        self.toolBar.addAction(self.display_customer)
        self.toolBar.addAction(self.delete_customer)
        self.toolBar.addSeparator()

        #loan toolbar actions
        self.toolBar.addAction(self.add_loan)
        self.toolBar.addAction(self.display_loan)
        self.toolBar.addAction(self.delete_loan)
        self.toolBar.addSeparator()

        #pat test toolbar actions
        self.toolBar.addAction(self.add_pat_test)
        self.toolBar.addAction(self.display_pat_test)
        self.toolBar.addAction(self.delete_pat_test)
        self.toolBar.addSeparator()

        #passord and logout actions
        self.toolBar.addAction(self.change_password)
        self.toolBar.addAction(self.logout_action)
        self.toolBar.setMovable(False)

        self.addToolBar(Qt.LeftToolBarArea, self.toolBar)

        self.setMenuBar(self.menubar)

        self.statusBar = QStatusBar()

        self.setStatusBar(self.statusBar)

        self.connections()

    def connections(self):
        #file menu connections
        self.new.triggered.connect(self.create_new_record_select_table_dialog)
        self.open.triggered.connect(self.open_connection)

        #edit menu connections

        #item menu connections
        self.add_item.triggered.connect(self.switch_to_new_item_layout)

        #customer menu connections
        self.add_customer.triggered.connect(self.switch_to_new_customer_layout)

        #loan menu connections
        self.add_loan.triggered.connect(self.switch_to_new_loan_layout)

        #pat test menu connections
        self.add_pat_test.triggered.connect(self.switch_to_new_pat_test_layout)

        #help menu connections
        self.about.triggered.connect(self.showAboutMessageBox)

        #logout connection
        self.logout_action.triggered.connect(self.logout)

        #database actions
        self.closeDatabase.triggered.connect(self.close_connection)

    def open_connection(self):
        if self.connection:
            self.close_connection()

        path = QFileDialog.getOpenFileName(caption="Open Database",filter="Database file (*.db)")
        self.connection = SQLConnection(path)
        opened = self.connection.open_database()

        if opened:
            self.password = self.connection.getPassword()
            #self.database_login()
            self.stacked_layout.setCurrentIndex(1)
            self.enable_actions()
            self.statusBar.showMessage("Database opened: {0}".format(path))

            
    def close_connection(self):
        if self.connection:
            closed = self.connection.close_database()

            if closed:
                self.statusBar.showMessage("Database has been closed.")
                self.disable_actions()
                self.stacked_layout.setCurrentIndex(0)
            else:
                self.statusBar.showMessage("An error occured!")
        else:
            self.statusBar.showMessage("No Database to close.")


    def showAboutMessageBox(self):

        aboutText = """This application was built by Joel Butcher using Python3, PyQt4 and uses Sqlite3. \n It is design for use by the media department of Cambridge Community Church to enable the organisation of the equipment owned by the department """

        QMessageBox.about(self, "About", aboutText)

    def create_new_record_select_table_dialog(self):
        self.select_table_dialog_box = RadioButtonWidget("Create New Record", "Please select a table", ("Item", "Customer", "Loan", "PAT-Test"))
        self.select_table_dialog_box.exec_()
        self.select_table_dialog_box.cancel_button.clicked.connect(self.close)
        self.select_table_dialog_box.select_button.clicked.connect(self.generate_new_records_layout)

    def generate_new_records_layout(self):
        self.selected_table = self.select_table_dialog_box.selected_button()
        if self.selected_table == 1:
            if hasattr(self, 'create_new_item'):
                self.stacked_layout.setCurrentIndex(2)
                #self.clear_new_item_widgets()
            else:
                self.create_new_item()
        elif self.selected_table == 2:
            if hasattr(self, 'create_new_customer'):
                self.stacked_layout.setCurrentIndex(3)
            else:
                self.create_new_customer()
        elif self.selected_table == 3:
            pass
        elif self.selected_table == 4:
            if hasattr(self, 'create_new_pat_test'):
                self.stacked_layout.setCurrentIndex(5)
            else:
                self.create_new_pat_test()

    def create_login(self):

        self.login_dialog = LoginDialog()
        self.login_dialog.exec_()

        self.login_dialog.login_button.clicked.connect(self.database_login)
        self.login_dialog.password_entry.returnPressed.connect(self.database_login)

    def create_start_screen(self):
        self.setStyleSheet("""QPushButton[buttonClass=home] {
                           font-size: 16px; background-color: rgba(188, 188, 188, 50);
                           border: 1px solid rgba(188, 188, 188, 250);
                           height:100px;
                           width:300px;
                           border-radius:5px;}""")

        self.open_database_button = QPushButton("Open Database")
        self.open_database_button.setProperty("buttonClass","home")
        self.open_database_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.close_application_button = QPushButton("Close Application")
        self.close_application_button.setProperty("buttonClass","home")
        self.close_application_button.setCursor(QCursor(Qt.PointingHandCursor))

        self.database_layout = QHBoxLayout()

        self.database_layout.addWidget(self.open_database_button)
        self.database_layout.addWidget(self.close_application_button)
        
        self.database_widget = QWidget()

        self.database_widget.setLayout(self.database_layout)

        self.stacked_layout.addWidget(self.database_widget)

        self.open_database_button.clicked.connect(self.open_connection)
        self.close_application_button.clicked.connect(self.close)

        self.close_application_button.setShortcut('Ctrl+Q')

    def create_logged_in_screen(self):
        self.start_widget = QWidget()

        self.enable_actions()

        self.stacked_layout.addWidget(self.start_widget)

    def create_new_item(self):
        if hasattr(self, 'new_item_right_widget'):
            self.new_item_right_widget.close()
            self.new_item_right_widget = QWidget()
            self.new_item_right_widget.setFixedWidth(300)

        self.new_item_right_widget = QWidget()

        self.new_item_widget = NewItemWidget()
        self.new_item_widget.setLayout(self.new_item_widget.item_layout)

        #geometry setting for widgets
        self.new_item_right_widget.setFixedWidth(300)
        self.new_item_widget.setFixedWidth(300)

        self.new_item_widget.confirm_button.clicked.connect(self.display_preview_new_item_record)
        self.new_item_widget.cancel_button.clicked.connect(self.cancel)

        self.create_new_item_layout = QHBoxLayout()

        self.create_new_item_layout.addWidget(self.new_item_widget)
        self.create_new_item_layout.addWidget(self.new_item_right_widget)

        self.create_new_item_widget = QWidget()
        self.create_new_item_widget.setLayout(self.create_new_item_layout)

        self.stacked_layout.addWidget(self.create_new_item_widget)

    def clear_new_item_widgets(self):
        #self.new_item_widget.clear_widgets()
        if hasattr(self, 'new_item_right_widget'):
            self.new_item_right_widget.close()
            self.new_item_right_widget = QWidget()
            self.new_item_right_widget.setFixedWidth(300)
            self.create_new_item_layout.addWidget(self.new_item_right_widget)

    def display_preview_new_item_record(self):
        self.new_item_widget.disable_edit_new_item()
        self.heading = QLabel("New Item Preview")
        self.heading.setAlignment(Qt.AlignCenter)
        self.heading.setStyleSheet("font:18pt; font-weight:bold")
        
        self.item_name_heading = QLabel("Item Name:")
        self.item_name = self.new_item_widget.item_name_line_edit.text()
        self.item_name_widget = QLabel("{0}".format(self.item_name))

        self.item_value_heading = QLabel("Item Value:")
        self.item_value = self.new_item_widget.item_value_line_edit.text()
        self.item_value_widget = QLabel("{0}".format(self.item_value))

        self.item_loan_rate_heading = QLabel("Loan Rate:")
        self.item_loan_rate = self.new_item_widget.item_loan_rate_line_edit.text()
        self.item_loan_rate_widget = QLabel("{0}".format(self.item_loan_rate))

        self.item_class_heading = QLabel("Item Class:")
        self.item_class = self.new_item_widget.item_class_drop_down.currentText()
        self.item_class_widget = QLabel("{0}".format(self.item_class))

        self.fuse_rating_heading = QLabel("Fuse Rating:")
        self.fuse_rating = self.new_item_widget.fuse_rating_drop_down.currentText()
        self.fuse_rating_widget = QLabel("{0}".format(self.fuse_rating))

        self.item_type_heading = QLabel("Item Type:")
        self.item_type = self.new_item_widget.item_type_drop_down.currentText()
        self.item_type_widget = QLabel("{0}".format(self.item_type))

        self.item_location_heading = QLabel("Location:")
        self.item_location = self.new_item_widget.location_drop_down.currentText()
        self.item_location_widget = QLabel("{0}".format(self.item_location))

        self.edit_button = QPushButton("Edit")
        self.preview_confirm_button = QPushButton("Confirm")

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.addWidget(self.edit_button)
        self.buttons_layout.addWidget(self.preview_confirm_button)

        self.buttons_widget = QWidget()
        self.buttons_widget.setLayout(self.buttons_layout)

        if hasattr(self, 'new_item_right_widget'):
            self.new_item_right_widget.close()
            self.new_item_right_widget = QWidget()
            self.new_item_right_widget.setFixedWidth(300)
            self.create_new_item_layout.addWidget(self.new_item_right_widget)


        self.new_item_preview_layout = QVBoxLayout()
        self.new_item_preview_layout.addWidget(self.heading)
        self.new_item_preview_layout.addWidget(self.item_name_heading)
        self.new_item_preview_layout.addWidget(self.item_name_widget)
        self.new_item_preview_layout.addWidget(self.item_value_heading)
        self.new_item_preview_layout.addWidget(self.item_value_widget)
        self.new_item_preview_layout.addWidget(self.item_loan_rate_heading)
        self.new_item_preview_layout.addWidget(self.item_loan_rate_widget)
        self.new_item_preview_layout.addWidget(self.item_class_heading)
        self.new_item_preview_layout.addWidget(self.item_class_widget)
        self.new_item_preview_layout.addWidget(self.fuse_rating_heading)
        self.new_item_preview_layout.addWidget(self.fuse_rating_widget)
        self.new_item_preview_layout.addWidget(self.item_type_heading)
        self.new_item_preview_layout.addWidget(self.item_type_widget)
        self.new_item_preview_layout.addWidget(self.item_location_heading)
        self.new_item_preview_layout.addWidget(self.item_location_widget)

        self.new_item_preview_layout.addWidget(self.buttons_widget)

        self.new_item_right_widget.setLayout(self.new_item_preview_layout)


        self.edit_button.clicked.connect(self.edit_new_item)
        self.preview_confirm_button.clicked.connect(self.enter_new_item_to_database)

    def edit_new_item(self):
        self.new_item_widget.enable_edit_new_item()
        self.edit_button.setEnabled(False)
        self.preview_confirm_button.setEnabled(False)

    def enter_new_item_to_database(self):
        if self.item_type == "Cabling":
            item_type_id = '1'
        elif self.item_type == "Storage/Hardware":
            item_type_id = '2'
        elif self.item_type == "Lighting":
            item_type_id = '3'
        elif self.item_type == "Power":
            item_type_id = '4'
        elif self.item_type == "Audio":
            item_type_id = '5'
        elif self.item_type == "Visual":
            item_type_id = '6'
        elif self.item_type == "Miscellaneous":
            item_type_id = '7'
        elif self.item_type == "Software":
            item_type_id = '8'
        elif self.item_type == "Staging":
            item_type_id = '9'
        elif self.item_type == "Control Desks":
            item_type_id = '10'

        if self.item_location == "St. Bedes":
            location_id = '1'
        elif self.item_location == "Alpha Terrace":
            location_id = '2'
        elif self.item_location == "Cineworld":
            location_id = '3'
        elif self.item_location == "C3 Centre":
            location_id = '4'


        print(self.item_name)
        print(self.item_value)
        print(self.item_loan_rate)
        print(self.item_class)
        print(self.fuse_rating)
        print(item_type_id)
        print(location_id)

        values = {"ItemName":self.item_name,
                  "ItemValue":self.item_value,
                  "LoanRate":self.item_loan_rate,
                  "ItemClass":self.item_class,
                  "FuseRating":self.fuse_rating,
                  "ItemTypeID":item_type_id,
                  "LocationID":location_id}

        print(values["ItemName"])

        success = self.connection.addItem(values)

        print(success)

        self.stacked_layout.setCurrentIndex(1)

    def create_new_loan(self):
        self.new_loan_right_widget = QWidget()

        self.loan_widget = NewLoanWidget()
        self.loan_widget.setLayout(self.loan_widget.loan_layout)

        self.loan_layout = QHBoxLayout()
        self.blank_widget = QWidget()

        self.loan_layout.addWidget(self.loan_widget)
        self.loan_layout.addWidget(self.blank_widget)

        self.new_loan_widget = QWidget()
        self.new_loan_widget.setLayout(self.loan_layout)


        self.loan_widget.enter_button.clicked.connect(self.return_pat_test)
        self.loan_widget.cancel_button.clicked.connect(self.cancel)

        self.stacked_layout.addWidget(self.new_loan_widget)

    def preview_new_loan_widget(self):
        self.new_loan_widget.disable_actions()

        self.new_loan_heading = QLabel("New Loan Preview")
        self.new_loan_heading.setAlignment(Qt.AlignCenter)
        self.new_loan_heading.setStyleSheet("font:18pt; font-weight:bold")

        if hasattr(self, 'new_loan_right_widget'):
            self.new_loan_right_widget.close()
            self.new_loan_right_widget = QWidget()
            self.new_loan_right_widget.setFixedWidth(300)
            self.create_new_loan.addWidget(self.new_loan_right_widget)

    def create_new_pat_test(self):
        self.new_pat_test_right_widget = QWidget()

        self.pat_test_widget = NewPatTestWidget()
        self.pat_test_widget.setLayout(self.pat_test_widget.pat_test_layout)

        self.pat_test_layout = QHBoxLayout()
        self.blank_widget = QWidget()

        self.pat_test_layout.addWidget(self.pat_test_widget)
        self.pat_test_layout.addWidget(self.blank_widget)

        self.new_pat_test_widget = QWidget()
        self.new_pat_test_widget.setLayout(self.pat_test_layout)

        self.pat_test_widget.enter_button.clicked.connect(self.return_pat_test)
        self.pat_test_widget.cancel_button.clicked.connect(self.cancel)

        self.stacked_layout.addWidget(self.new_pat_test_widget)

    def preview_new_pat_test_widget(self):
        self.new_pat_test_widget.disable_actions()

        self.new_pat_test_heading = QLabel("New PAT Test Preview")
        self.new_pat_test_heading.setAlignment(Qt.AlignCenter)
        self.new_pat_test_heading.setStyleSheet("font:18pt; font-weight:bold")

        if hasattr(self, 'new_pat_test_right_widget'):
            self.new_pat_test_right_widget.close()
            self.new_pat_test_right_widget = QWidget()
            self.new_pat_test_right_widget.setFixedWidth(300)
            self.create_new_pat_test.addWidget(self.new_pat_test_right_widget)

    def return_pat_test(self):
        self.date = self.pat_test_widget.date_widget.cal.selectedDate()
        year,month,day = QDate.getDate(self.date)
        year = int(year)
        month = int(month)
        day = int(day)
        self.date = ("{0}/{1}/{2}".format(day,month,year))
        self.statusBar.showMessage(self.date)
        self.stacked_layout.setCurrentIndex(0)

    def create_new_customer(self):
        self.new_customer_right_widget = QWidget()
        self.new_customer_widget = NewCustomerWidget()
        self.new_customer_right_widget.setFixedWidth(300)
        self.new_customer_widget.setFixedWidth(300)

        self.new_customer_widget.get_forename.clear()
        self.new_customer_widget.get_surname.clear()
        self.new_customer_widget.get_company.clear()
        self.new_customer_widget.get_address.clear()
        self.new_customer_widget.get_town.clear()
        self.new_customer_widget.get_post_code.clear()
        self.new_customer_widget.get_mobile.clear()
        self.new_customer_widget.get_landline.clear()
        self.new_customer_widget.get_email.clear()
        self.new_customer_widget.setLayout(self.new_customer_widget.new_customer_layout)

        self.new_customer_widget.setFixedWidth(300)
        self.new_customer_right_widget.setFixedWidth(300)

        self.create_new_customer_layout = QHBoxLayout()

        self.create_new_customer_layout.addWidget(self.new_customer_widget)
        self.create_new_customer_layout.addWidget(self.new_customer_right_widget)

        self.new_customer_widget.confirm_button.clicked.connect(self.preview_new_customer_widget)
        self.new_customer_widget.cancel_button.clicked.connect(self.cancel)

        self.stacked_layout.addWidget(self.new_customer_widget)

    def preview_new_customer_widget(self):
        self.new_customer_widget.diable_widget()

        self.new_customer_heading = QLabel("New Customer Preview")
        self.new_customer_heading.setAlignment(Qt.AlignCenter)
        self.new_customer_heading.setStyleSheet("font:18pt; font-weight:bold")

        self.firstname_label = QLabel("FirstName")
        self.new_firstname = self.new_customer_widget.get_forename.text()
        self.firstname_widget = QLabel()

        self.lastname_label = QLabel("Lastname")
        self.new_lastname = self.new_customer_widget.get_surname.text()
        self.lastname_widget = QLabel()

        self.company_label = QLabel("Company")
        self.new_company = self.new_customer_widget.get_company.text()
        self.company_widget = QLabel()

        self.street_label = QLabel("Street")
        self.new_street = self.new_customer_widget.get_address.text()
        self.street_widget = QLabel()

        self.town_label = QLabel("Town")
        self.new_town = self.new_customer_widget.get_town.text()
        self.town_widget = QLabel()

        self.post_code_label = QLabel("Post-Code")
        self.new_post_code = self.new_customer_widget.get_post_code.text()
        self.post_code_widget = QLabel()

        self.mobile_label = QLabel("Mobile")
        self.new_mobile = self.new_customer_widget.get_mobile.text()
        self.mobile_widget = QLabel()

        self.laneline_label = QLabel("Landline")
        self.new_landline = self.new_customer_widget.get_landline.text()
        self.lanline_widget = QLabel()

        self.email_label = QLabel("Email")
        self.new_email = self.new_customer_widget.get_email.text()
        self.email_widget = QLabel()

        if hasattr(self, 'new_item_right_widget'):
            self.new_customer_right_widget.close()
            self.new_customer_right_widget = QWidget()
            self.new_customer_right_widget.setFixedWidth(300)
            self.create_new_customer.addWidget(self.new_customer_right_widget)

        self.new_customer_preview_layout = QVBoxLayout()
        self.new_customer_preview_layout.addWidget(self.new_customer_heading)

        self.new_customer_right_widget.setLayout(self.new_customer_preview_layout)



    def validate_customer(self):
        valid_customer = self.return_customer()
        if valid_customer == True:
            pass
        else:
            self.new_customer_widget.enable_widget()




    def return_customer(self):
        valid_customer = False
        self.forename = self.new_customer_widget.get_forename.text()
        valid_length = False
        if len(self.forename) == 0:
            valid_length = False
            self.error_dialog = EntryErrorDialog('a valid Forename')
            self.error_dialog.exec_()
        elif len(self.forename) > 0 :
            valid_length = True
            valid = False
            for char in self.forename:
                if char.isdigit() == True:
                    valid = False
                else:
                    valid = True
            if valid == False:
                self.error_dialog = EntryErrorDialog('only letters')
                self.error_dialog.exec_()
                valid_forename = False
            elif valid == True and valid_length == True:
                valid_forename = True
                print("Forename: {0}".format(self.forename))


        self.surname = self.new_customer_widget.get_surname.text()
        valid_length = False
        if len(self.surname) == 0:
            valid_length = False
            self.error_dialog = EntryErrorDialog('a valid Surname')
            self.error_dialog.exec_()
        elif len(self.surname) > 0 :
            valid_length = True
            valid = False
            for char in self.surname:
                if char.isdigit() == True:
                    valid = False
                else:
                    valid = True
            if valid == False:
                self.error_dialog = EntryErrorDialog('only letters')
                self.error_dialog.exec_()
                valid_surname = False
            elif valid == True and valid_length == True:
                valid_surname = True
                print("Surname: {0}".format(self.surname))


        self.company = self.new_customer_widget.get_company.text()
        valid_length = False
        if len(self.company) == 0:
            valid_length = False
            self.error_dialog = EntryErrorDialog('a valid Company')
            self.error_dialog.exec_()
        elif len(self.company) > 0 :
            valid_length = True
            valid = False
            for char in self.company:
                if char.isdigit() == True:
                    valid = False
                else:
                    valid = True
            if valid == False:
                self.error_dialog = EntryErrorDialog('only letters')
                self.error_dialog.exec_()
                valid_company = False
            elif valid == True and valid_length == True:
                valid_company = True
                print("Company: {0}".format(self.company))


        self.street = self.new_customer_widget.get_address.text()
        valid_length = False
        if len(self.street) > 0:
            valid_length = True
            valid_street = True
            print("Address: {0}".format(self.street))
        else:
            valid_length = False
            self.error_dialog = EntryErrorDialog('a valid Address')
            self.error_dialog.exec_()
                

        self.town = self.new_customer_widget.get_town.text()
        valid_length = False
        if len(self.town) == 0:
            valid_length = False
            self.error_dialog = EntryErrorDialog('a Town')
            self.error_dialog.exec_()
        elif len(self.town) > 0 :
            valid_length = True
            valid = False
            for char in self.town:
                if char.isdigit() == True:
                    valid = False
                else:
                    valid = True
            if valid == False:
                self.error_dialog = EntryErrorDialog('only letters')
                self.error_dialog.exec_()
                valid_town = False
            elif valid == True and valid_length == True:
                valid_town = True
                print("Town: {0}".format(self.town))


        self.post_code = self.new_customer_widget.get_post_code.text()
        valid_length = False
        length_regex_validation = re.match('[a-zA-Z]{1,2}[0-9]{1,2}([A-Z]|[a-z]|[A-Z][a-z])?\s[0-9][a-zA-Z][a-zA-Z]', self.post_code)
        if length_regex_validation:
            valid = True
        else:
            valid = False
        
        if valid == True:
            valid_post_code = True
            print("Post-Code: {0}".format(self.post_code))
        else:
            self.error_dialog = EntryErrorDialog('a valid Post-Code')
            self.error_dialog.exec_()
            valid_post_code = False


        self.mobile = self.new_customer_widget.get_mobile.text()
        valid_length = False
        if len(self.mobile) == 11:
            valid_length = True
            valid = False
            no_letters = re.search('^[a-z],[A-z]*$', self.mobile)
            valid_mobile = re.search('^(07\d{8,12}|447\d{7,11})$', self.mobile)
            if not no_letters and valid_mobile:
                valid = True
            else:
                valid = False
        else:
            valid_length = False
        if valid_length == True and valid == True:
            valid_mobile = True
            print("Mobile: {0}".format(self.mobile))
        else:
            self.error_dialog = EntryErrorDialog('a valid Mobile Number')
            self.error_dialog.exec_()
            valid_mobile = False


        self.landline = self.new_customer_widget.get_landline.text()
        valid_length = False
        if len(self.landline) == 11:
            valid_length = True
            valid = False
            for char in self.landline:
                no_letters = re.search('^[a-z],[A-z]*$',self.landline)
                valid_landline_number = re.search('^\s*\(?(020[78]?\)? ?[1-9][0-9]{2,3} ?[0-9]{4})$|^(0[1-8][0-9]{3}\)? ?[1-9][0-9]{2} ?[0-9]{3})\s*$', self.landline)
                if not no_letters and valid_landline_number:
                    valid = True
                else:
                    valid = False
        else:
            valid_length = False
        if valid_length == True and valid == True:
            valid_landline = True
            print("Landline: {0}".format(self.landline))
        else:
            self.error_dialog = EntryErrorDialog('a valid Landline Number')
            self.error_dialog.exec_()
            valid_landline = False


        self.email = self.new_customer_widget.get_email.text()
        valid_length = False
        if len(self.email) > 0:
            valid_length = True
            valid = False
            valid_email_type = re.match("^[a-zA-Z0-9._%-+]+@[a-zA-Z0-9._%-]+.[a-z]{2,3}(\.[a-z]{2,3})$", self.email)
            if valid_email_type:
                valid = True
            else:
                valid = False
        else:
            valid_length = False
        if valid_length == True and valid == True:
            valid_email = True
            print("Email: {0}".format(self.email))
            if valid_forename == True and valid_surname == True and valid_company == True and valid_street == True and valid_town == True and valid_post_code == True and valid_mobile == True and valid_landline == True and valid_email == True:
                valid_customer = True
                print(valid_customer)
        else:
            self.error_dialog = EntryErrorDialog('a valid Email Address')
            self.error_dialog.exec_()
            valid_email = False
        
    def database_login(self):
        while not self.access:
            self.create_login()
            user_password = self.login_dialog.password_entry.text()
            if self.password == user_password:
                self.access = True
                self.enable_actions()
                self.stacked_layout.setCurrentIndex(1)
            else:
                self.login_error_dialog = LoginErrorDialog()
                self.login_error_dialog.exec_()
                self.access = False

    def closeEvent(self, event):
        self.stacked_layout.setCurrentIndex(1)
        if self.access == False:
            self.close_connection()

    def logout(self):
        self.access = False
        self.stacked_layout.setCurrentIndex(0)
        self.close_connection()
        self.disable_actions()

    def change_password_method(self):
        change_password_dialog = ChangePasswordDialog(self.password)
        change_password_dialog.exec_()  

    def switch_to_new_item_layout(self):
        if hasattr(self, 'create_new_item'):
            self.clear_new_item_widgets()
        self.stacked_layout.setCurrentIndex(2)

    def switch_to_new_customer_layout(self):
        self.stacked_layout.setCurrentIndex(3)

    def switch_to_new_loan_layout(self):
        self.stacked_layout.setCurrentIndex(4)

    def switch_to_new_pat_test_layout(self):
        self.stacked_layout.setCurrentIndex(5)

    def cancel(self):
        self.stacked_layout.setCurrentIndex(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = C3MediaDBMS()
    window.show()
    window.raise_()
    app.exec_()

