from login_error_dialog import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *
    
import sys
import pdb


class MainMenuWindow(QMainWindow):
    """Main Menu Prototype"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Menu")
        self.main_menu_stacked_layout = QStackedLayout()
        self.main_menu_stacked_widget = QWidget()

        self.main_menu_stacked_widget.setLayout(self.main_menu_stacked_layout)

        self.create_menubar_actions()
        self.add_keyboard_shotcuts()
        
        self.create_login_layout()
        self.create_main_layout()

        self.setCentralWidget(self.main_menu_stacked_widget)

        self.main_menu_stacked_layout.setCurrentIndex(0)

    def create_menubar_actions(self):
        #create actions
        self.new = QAction("New", self)
        self.open = QAction("Open...", self)
        self.close_window = QAction("Close", self)
        self.save = QAction("Save", self)
        self.save_as = QAction("Save As", self)
        self.logout = QAction("Logout", self)
        self.change_password = QAction("Change Password", self)

        self.close_window.triggered.connect(self.close)
        
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
        self.file_menu.addAction(self.logout)
        self.file_menu.addAction(self.change_password)

    def create_login_layout(self):
        #components
        self.login_label = QLabel("Please enter the Password to access:")
        self.password_entry = QLineEdit()
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
        #self.password_entry.escapePressed.connect(self.close)
        self.login_enter_button.clicked.connect(self.login)
        self.login_quit_button.clicked.connect(self.close)

    def login(self):
        password = "c3media"
        name = self.password_entry.text()
        if name == password:
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
        self.main_menu_screen_layout.addWidget(self.change_password_button,3,0)
        self.main_menu_screen_layout.addWidget(self.logout_button,3,1)
        #create widget to hold layout
        self.main_menu_initial_widget = QWidget()
        #add layout to widget
        self.main_menu_initial_widget.setLayout(self.main_menu_screen_layout)
        #add widget to stacked layout
        self.main_menu_stacked_layout.addWidget(self.main_menu_initial_widget)
        

    def add_keyboard_shotcuts(self):
        #keyboard shortcuts
        self.new.setShortcut('Ctrl+N')
        self.open.setShortcut('Ctrl+O')
        self.close_window.setShortcut('Ctrl+W')
        self.save.setShortcut('Ctrl+S')
        self.save_as.setShortcut('Ctrl+Shift+S')

        
        
def main_menu_main():
    application = QApplication(sys.argv)
    window = MainMenuWindow()
    window.show()
    window.raise_()
    application.exec_()

if __name__ == "__main__":
    main_menu_main()
