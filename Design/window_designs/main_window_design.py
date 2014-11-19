from PyQt4.QtCore import *
from PyQt4.QtGui import *
    
import sys
import pdb


class MainWindow(QMainWindow):
    """A Simple window"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Menu")
        self.main_menu_stacked_layout = QStackedLayout()
        self.main_menu_stacked_widget = QWidget()

        self.main_menu_stacked_widget.setLayout(self.main_menu_stacked_layout)

        self.create_menubar_actions()
        self.create_main_layout()

        self.setCentralWidget(self.main_menu_stacked_widget)

        self.main_menu_stacked_layout.setCurrentIndex(0)

    def create_menubar_actions(self):
        #create actions
        self.new = QAction("New", self)
        self.open = QAction("Open...", self)
        self.save = QAction("Save", self)
        self.save_as = QAction("Save As", self)
        self.logout = QAction("Logout", self)
        self.change_password = QAction("Change Password", self)
        
        #add menu bar
        self.menu = QMenuBar()
        self.database_toolbar = QToolBar()

        #add actions to menu bar
        self.file_menu = self.menu.addMenu("File")
        self.file_menu.addAction(self.new)
        self.file_menu.addAction(self.open)
        self.file_menu.addAction(self.save)
        self.file_menu.addAction(self.save_as)
        self.file_menu.addAction(self.logout)
        self.file_menu.addAction(self.change_password)

    def create_main_layout(self):
        #components
        self.new_record_button = QPushButton("New Record")
        self.display_records_button = QPushButton("Display Table Records")
        self.edit_record_button = QPushButton("Edit Records")
        self.delete_record_button = QPushButton("Delete Record")
        self.logout_button = QPushButton("Logout")
        #create layout
        self.main_menu_screen_layout = QGridLayout()
        #add components to layout
        self.main_menu_screen_layout.addWidget(self.new_record_button,0,0)
        self.main_menu_screen_layout.addWidget(self.display_records_button,0,1)
        self.main_menu_screen_layout.addWidget(self.edit_record_button,1,0)
        self.main_menu_screen_layout.addWidget(self.delete_record_button,1,1)
        self.main_menu_screen_layout.addWidget(self.logout_button,2,1)
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
        self.save.setShortcut('Ctrl+S')
        self.save_as.setShortcut('Ctrl+Shift+S')
        
        
def main():
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()

if __name__ == "__main__":
    main()
