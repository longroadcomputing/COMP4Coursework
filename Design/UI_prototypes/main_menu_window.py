from login_error_dialog import *
from change_password_dialog import *
from password_reset import *
from printing import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *
    
import sys
import pdb


class MainMenuWindow(QMainWindow):
    """Main Menu Prototype"""
    def __init__(self):
        super().__init__()

        #pdb.set_trace()
        self.password = read_password()
        
        self.setWindowTitle("Main Menu")

        self.printer = QPrinter()
        self.printer.setPageSize(QPrinter.Letter)
        
        self.main_menu_stacked_layout = QStackedLayout()
        self.main_menu_stacked_widget = QWidget()

        self.main_menu_stacked_widget.setLayout(self.main_menu_stacked_layout)

        self.create_menubar_actions()
        self.disable_menubar_actions()
        self.add_keyboard_shotcuts()
        
        self.create_login_layout()
        self.enable_menubar_actions()
        self.create_main_layout()

        self.setCentralWidget(self.main_menu_stacked_widget)

        self.main_menu_stacked_layout.setCurrentIndex(0)

    def create_menubar_actions(self):
        #create actions
        self.new = QAction("New", self)
        self.open = QAction("Open", self)
        self.print = QAction("Print", self)
        self.close_window = QAction("Close Window", self)
        self.save = QAction("Save", self)
        self.save_as = QAction("Save As", self)
        self.logout = QAction("Logout", self)
        self.change_password = QAction("Change Password", self)

        self.close_window.triggered.connect(self.close)
        self.print.triggered.connect(self.printing)
        
        #add menu bar
        self.menu = QMenuBar()
        self.database_toolbar = QToolBar()

        #add actions to menu bar
        self.file_menu = self.menu.addMenu("File")
        self.file_menu.addAction(self.new)
        self.file_menu.addAction(self.open)
        self.file_menu.addAction(self.close_window)
        self.file_menu.addAction(self.save)
        self.file_menu.addAction(self.save_as)
        self.file_menu.addAction(self.print)
        self.file_menu.addAction(self.logout)
        self.file_menu.addAction(self.change_password)

    def disable_menubar_actions(self):
        self.new.setEnabled(False)
        self.open.setEnabled(False)
        self.print.setEnabled(False)
        self.close_window.setEnabled(False)
        self.save.setEnabled(False)
        self.save_as.setEnabled(False)
        self.logout.setEnabled(False)
        self.change_password.setEnabled(False)

    def enable_menubar_actions(self):
        self.new.setEnabled(True)
        self.open.setEnabled(True)
        self.print.setEnabled(True)
        self.close_window.setEnabled(True)
        self.save.setEnabled(True)
        self.save_as.setEnabled(True)
        self.logout.setEnabled(True)
        self.change_password.setEnabled(True)

    def create_login_layout(self):
        #components
        self.login_label = QLabel("Please enter the Password to access:")
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)
        self.password_entry.setPlaceholderText("Password...")
        self.login_quit_button = QPushButton("Quit")
        self.login_enter_button = QPushButton("Enter")
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
        
        #create main widget to hold layout
        self.login_main_widget = QWidget()
        #add layout to main widget
        self.login_main_widget.setLayout(self.login_layout)
        #add widget to stacked layout
        self.main_menu_stacked_layout.addWidget(self.login_main_widget)

        #connections
        self.password_entry.returnPressed.connect(self.login)
        self.login_enter_button.clicked.connect(self.login)
        self.login_quit_button.clicked.connect(self.close)

    def login(self):
        name = self.password_entry.text()
        if name == self.password:
            allow_access = True
            self.main_menu_stacked_layout.setCurrentIndex(1)
        else:
            allow_access = False
            login_error = LoginErrorDialog()
            login_error.exec_()

    def create_main_layout(self):
        #components
        self.new_record_button = QPushButton("New Record")
        self.display_records_button = QPushButton("Display Table Records")
        self.edit_record_button = QPushButton("Edit Records")
        self.delete_record_button = QPushButton("Delete Record")
        self.logout_button = QPushButton("Logout")
        self.change_password_button = QPushButton("Change Password")
        #create layout
        self.main_menu_screen_layout = QGridLayout()
        #add components to layout
        self.main_menu_screen_layout.addWidget(self.new_record_button,0,0)
        self.main_menu_screen_layout.addWidget(self.display_records_button,0,1)
        self.main_menu_screen_layout.addWidget(self.edit_record_button,1,0)
        self.main_menu_screen_layout.addWidget(self.delete_record_button,1,1)
        self.main_menu_screen_layout.addWidget(self.logout_button,3,0)
        self.main_menu_screen_layout.addWidget(self.change_password_button,3,1)
        #create widget to hold layout
        self.main_menu_initial_widget = QWidget()
        #add layout to widget
        self.main_menu_initial_widget.setLayout(self.main_menu_screen_layout)
        #add widget to stacked layout
        self.main_menu_stacked_layout.addWidget(self.main_menu_initial_widget)
        #connections
        self.change_password_button.clicked.connect(self.change_password_method)
        self.logout_button.clicked.connect(self.back_to_login_screen)

    def back_to_login_screen(self):
        self.main_menu_stacked_layout.setCurrentIndex(0)
        self.password_entry.clear()
        self.password = read_password()
        

    def add_keyboard_shotcuts(self):
        #keyboard shortcuts
        self.new.setShortcut('Ctrl+N')
        self.open.setShortcut('Ctrl+O')
        self.close_window.setShortcut('Ctrl+W')
        self.save.setShortcut('Ctrl+S')
        self.save_as.setShortcut('Ctrl+Shift+S')
        self.print.setShortcut('Ctrl+P')

    def change_password_method(self):
        change_password_dialog = ChangePasswordDialog(self.password)
        change_password_dialog.exec_()
        self.new_password = change_password_dialog.change_password()
        if self.new_password != self.password:
            self.password = self.new_password
            update_password(self.password)

    def printing(self):
        printing = Print()
        html = printing.statementHtml()
##        html += ("<h1> Hello this is a test print!</h1>"
##                 "<hr/><p style='font-family:times;color:red;'> {0} This is testing the print functionality"
##                 "of printing something in html from PyQt4.</p>").format(date)
        dialog = QPrintDialog(self.printer, self)
        if dialog.exec_():
            document = QTextDocument()
            document.setHtml(html)
            document.print_(self.printer)
        else:
            print("The print process has failed!")
        print(html)

        
def main_menu_main():
    application = QApplication(sys.argv)
    window = MainMenuWindow()
    window.show()
    window.raise_()
    application.exec_()

if __name__ == "__main__":
    main_menu_main()
