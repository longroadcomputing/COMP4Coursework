try:
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
except:
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    
import sys
import pdb


class MainWindow(QMainWindow):
    """A Simple window"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

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

        #add database actions to menu bar
        self.database_menu = self.menu.addMenu("File")
        self.database_menu.addAction(self.new)
        self.database_menu.addAction(self.open)
        self.database_menu.addAction(self.save)
        self.database_menu.addAction(self.save_as)
        self.database_menu.addAction(self.logout)
        self.database_menu.addAction(self.change_password)

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
