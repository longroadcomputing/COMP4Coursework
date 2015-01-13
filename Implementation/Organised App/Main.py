from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys
import time

from SQLConnection import *
from loggedInWidget import *

from NewItemWidget import *
from NewCustomerWidget import *
from NewLoanWidget import *
from NewPatTestWidget import *

from manageItems import *
from manageCustomer import *

from create_login_dialog import *


class MainWindow(QMainWindow):
	"""docstring for MainWindowQMainWindow"""
	def __init__(self):
		super( ).__init__()

		self.setWindowTitle("C3 Media Database Management Systems")
		self.move(200,250)
		self.centerOnScreen()

		self.icon = QIcon(QPixmap("./c3_logo_black.png"))
		self.setWindowIcon(self.icon)

		#Connection Attribute stores the database connection
		self.connection = None
		self.access = False
		
		#stacked layout
		self.stacked_layout = QStackedLayout()

		self.widget = QWidget()

		self.widget.setLayout(self.stacked_layout)
		#self.stacked_layout.setAlignment(Qt.AlignHCenter)

		#set central widget to the stacked layout
		self.setCentralWidget(self.widget)

		#add menubar, status and toolbars
		self.settings()
		self.createActionShortcuts()

		#generate widgets
		self.initialCentralWidget()
		self.loggedInWidget()
		self.CreateNewItemWidget()
		self.CreateNewCustomerWidget()
		self.CreateNewLoanWidget()
		self.CreateNewPatTestWidget()
		self.CreateManageCustomersWidget()

		#disable actions
		self.disable_actions()

		#set Qt action signals, connections and shortcuts
		self.connections()
		self.createActionShortcuts()

	def centerOnScreen(self):
		resolution = QDesktopWidget().screenGeometry()
		self.move((resolution.width() / 2) - (self.frameSize().width() / 2),
		(resolution.height() / 2) - (self.frameSize().height() / 2))


	def addDbConnectionsToWidgets(self):
		self.new_item_widget.addConnection(self.connection)
		self.new_customer_widget.addConnection(self.connection)
		#self.new_loan_widget.addConnection(self.connection)
		#self.new_pat_test_widget.addConnection(self.connection)

		self.manageCustomers.addConnection(self.connection)

	def settings(self):
		#file actions
		self.open = QAction("Open Database", self)
		self.closeDatabase = QAction("Close Database", self)
		self.new = QAction("New", self)
		self.Print = QAction("Print", self)
		self.change_password = QAction("Change Password", self)
		self.logout_action = QAction("Logout", self)
		self.close_window = QAction("Close Window", self)

		#edit actions
		self.cut = QAction("Cut", self)
		self.copy = QAction("Copy", self)
		self.paste = QAction("Paste...", self)
		self.select_all = QAction("Select All", self)


		#item actions
		self.add_item = QAction('Add Item', self)
		self.manage_item = QAction('Manage Item', self)

		#customer actions
		self.add_customer = QAction('Add Customer', self)
		self.manage_customer = QAction('Manage Customer', self)
   
		#loan actions
		self.add_loan = QAction('Add Loan', self)
		self.manage_loan = QAction('Manage Loan', self)

		#pat_test actions
		self.add_pat_test = QAction('Add Pat Test', self)
		self.manage_pat_test = QAction('Manage Pat Test', self)

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
		self.file_menu.addSeparator()
		self.file_menu.addAction(self.close_window)


		#add edit menu and add actions to edit menu
		self.edit_menu = self.menubar.addMenu("Edit")
		self.edit_menu.addAction(self.cut)
		self.edit_menu.addAction(self.copy)
		self.edit_menu.addAction(self.paste)
		self.edit_menu.addAction(self.select_all)


		#item menu
		self.item_menu = self.menubar.addMenu("Item")
		self.item_menu.addAction(self.add_item)
		self.item_menu.addAction(self.manage_item)

		#customer menu
		self.customer_menu = self.menubar.addMenu("Customer")
		self.customer_menu.addAction(self.add_customer)
		self.customer_menu.addAction(self.manage_customer)

		#loan menu
		self.loan_menu = self.menubar.addMenu("Loan")
		self.loan_menu.addAction(self.add_loan)
		self.loan_menu.addAction(self.manage_loan)

		#pat test menu
		self.pat_test_menu = self.menubar.addMenu("Pat Test")
		self.pat_test_menu.addAction(self.add_pat_test)
		self.pat_test_menu.addAction(self.manage_pat_test)

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
		self.toolBar.addAction(self.manage_item)
		self.toolBar.addSeparator()

		#customer toolbar action
		self.toolBar.addAction(self.add_customer)
		self.toolBar.addAction(self.manage_customer)
		self.toolBar.addSeparator()

		#loan toolbar actions
		self.toolBar.addAction(self.add_loan)
		self.toolBar.addAction(self.manage_loan)
		self.toolBar.addSeparator()

		#pat test toolbar actions
		self.toolBar.addAction(self.add_pat_test)
		self.toolBar.addAction(self.manage_pat_test)
		self.toolBar.addSeparator()

		#passord and logout actions
		self.toolBar.addAction(self.change_password)
		self.toolBar.addAction(self.logout_action)
		self.toolBar.setMovable(False)

		self.addToolBar(Qt.TopToolBarArea, self.toolBar)

		#OS X translusency
		self.toolBar.setStyleSheet('background: transparent')
		self.toolBar.setAttribute(Qt.WA_TranslucentBackground, True)
		self.toolBar.setAutoFillBackground(True)

		self.setMenuBar(self.menubar)

		self.statusBar = QStatusBar()

		self.setStatusBar(self.statusBar)


	def createActionShortcuts(self):
		#file menu shortcuts
		self.open.setShortcut('Ctrl+O')
		self.new.setShortcut('Ctrl+N')
		self.Print.setShortcut('Ctrl+P')
		self.logout_action.setShortcut('Ctrl+Shift+L')
		self.close_window.setShortcut('Ctrl+W')

		#edit menu shortcuts
		self.cut.setShortcut('Ctrl+X')
		self.copy.setShortcut('Ctrl+C')
		self.paste.setShortcut('Ctrl+V')
		self.select_all.setShortcut('Ctrl+A')

	def connections(self):
		#menubar connections
		self.open.triggered.connect(self.open_database)
		self.close_window.triggered.connect(self.close)

		#toolbar actions
		self.add_item.triggered.connect(self.switchToNewItem)
		self.add_customer.triggered.connect(self.switchToNewCustomer)
		self.add_loan.triggered.connect(self.switchToNewLoan)
		self.add_pat_test.triggered.connect(self.switchToNewPatTest)

		self.manage_customer.triggered.connect(self.switchToManageCustomers)

		#button connections
		self.open_database_button.clicked.connect(self.open_database)
		self.close_application_button.clicked.connect(self.close)

		self.mainMenu.logoutButton.clicked.connect(self.close_database)

		self.new_item_widget.cancelButton.clicked.connect(self.switchToMainMenu)
		self.new_customer_widget.cancelButton.clicked.connect(self.switchToMainMenu)
		# self.new_loan_widget.cancelButton.clicked.connect(self.switchToMainMenu)
		self.new_pat_test_widget.cancelButton.clicked.connect(self.switchToMainMenu)

		#login connections
		# self.login_dialog.login_button.clicked.connect(self.database_login)
		# self.login_dialog.password_entry.returnPressed.connect(self.database_login)
		self.logout_action.triggered.connect(self.close_database)

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
		self.manage_item.setEnabled(False)

		#customer actions
		self.add_customer.setEnabled(False)
		self.manage_customer.setEnabled(False)

		#loan actions
		self.add_loan.setEnabled(False)
		self.manage_loan.setEnabled(False)

		#pat_test actions
		self.add_pat_test.setEnabled(False)
		self.manage_pat_test.setEnabled(False)

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
		self.manage_item.setEnabled(True)

		#customer actions
		self.add_customer.setEnabled(True)
		self.manage_customer.setEnabled(True)

		#loan actions
		self.add_loan.setEnabled(True)
		self.manage_loan.setEnabled(True)

		#pat_test actions
		self.add_pat_test.setEnabled(True)
		self.manage_pat_test.setEnabled(True)

		#help actions
		self.help.setEnabled(True)
		self.about.setEnabled(True)

		#database actions
		self.open.setEnabled(False)
		self.closeDatabase.setEnabled(True)

		#add connection to widgets
		self.addDbConnectionsToWidgets()


	def open_database(self):
		if self.connection:
			self.close_database()

		path = QFileDialog.getOpenFileName(caption="Open Database",filter="Database file (*.db)")
		self.connection = SQLConnection(path)
		opened = self.connection.open_database()

		if opened:
			self.password = self.connection.getPassword()
			self.database_login()
			self.stacked_layout.setCurrentIndex(1)
			#self.enable_actions()
			self.statusBar.showMessage("Database opened: {0}".format(path))

	def close_database(self):
		if self.connection:
			closed = self.connection.close_database()

			if closed:
				self.statusBar.showMessage("Database has been closed.")
				#self.disable_actions()
				self.logout()
				#self.stacked_layout.setCurrentIndex(0)
			else:
				self.statusBar.showMessage("An error occured!")
		else:
			self.statusBar.showMessage("No Database to close.")


	def initialCentralWidget(self):
		self.setStyleSheet("""QPushButton[buttonClass=home] {
					   font-size: 16px; background-color: rgba(188, 188, 188, 50);
					   border: 1px solid rgba(188, 188, 188, 250);
					   height:100px;
					   width:200px;
					   border-radius:5px;}""")

		self.open_database_button = QPushButton("Open Database")
		self.open_database_button.setMaximumWidth(200)
		self.open_database_button.setProperty("buttonClass","home")
		self.open_database_button.setCursor(QCursor(Qt.PointingHandCursor))

		self.close_application_button = QPushButton("Close Application")
		self.close_application_button.setMaximumWidth(200)
		self.close_application_button.setProperty("buttonClass","home")
		self.close_application_button.setCursor(QCursor(Qt.PointingHandCursor))

		self.database_layout = QVBoxLayout()

		self.database_layout.addWidget(self.open_database_button,Qt.AlignCenter)
		self.database_layout.addWidget(self.close_application_button,Qt.AlignCenter)
		self.database_layout.setAlignment(Qt.AlignHCenter)
		
		self.database_widget = QWidget()

		self.database_widget.setLayout(self.database_layout)

		self.stacked_layout.addWidget(self.database_widget)

	def loggedInWidget(self):
		self.mainMenu = loggedInWidget(self)
		self.mainMenu.setLayout(self.mainMenu.mainLayout)
		self.stacked_layout.addWidget(self.mainMenu)

	def switchToMainMenu(self):
		self.stacked_layout.setCurrentIndex(1)

	def switchToNewItem(self):
		if hasattr(self, 'new_item_widget'):
			self.new_item_widget.clearForm()
		self.stacked_layout.setCurrentIndex(2)

	def switchToNewCustomer(self):
		if hasattr(self, 'new_customer_widget'):
			self.new_customer_widget.clearForm()
		self.stacked_layout.setCurrentIndex(3)

	def switchToNewLoan(self):
		if hasattr(self, 'new_loan_widget'):
			pass
		self.stacked_layout.setCurrentIndex(4)

	def switchToNewPatTest(self):
		self.stacked_layout.setCurrentIndex(5)

	def switchToManageCustomers(self):
		self.stacked_layout.setCurrentIndex(6)

	def CreateNewItemWidget(self):
		self.new_item_widget =  NewItemWidget(self)
		self.new_item_widget.setLayout(self.new_item_widget.mainLayout)
		self.stacked_layout.addWidget(self.new_item_widget)

	def CreateNewCustomerWidget(self):
		self.new_customer_widget = newCustomerWidget(self)
		self.new_customer_widget.setLayout(self.new_customer_widget.mainLayout)
		self.stacked_layout.addWidget(self.new_customer_widget)


	def CreateNewLoanWidget(self):
		self.new_loan_widget = newLoanWidget(self)
		self.new_loan_widget.setLayout(self.new_loan_widget.mainLayout)
		self.stacked_layout.addWidget(self.new_loan_widget)

	def CreateNewPatTestWidget(self):
		self.new_pat_test_widget = newPatTestWidget(self)
		self.new_pat_test_widget.setLayout(self.new_pat_test_widget.mainLayout)
		self.stacked_layout.addWidget(self.new_pat_test_widget)

	def CreateManageCustomersWidget(self):
		self.manageCustomers = ManageCustomersWidget(self)
		self.stacked_layout.addWidget(self.manageCustomers)

	def showAboutMessageBox(self):

		aboutText = """This application was built by Joel Butcher using Python3, PyQt4 and uses Sqlite3. \n 
						It is design for use by the media department of Cambridge Community Church \n
						to enable the organisation of the equipment owned by the department """

		QMessageBox.about(self, "About", aboutText)

	def create_login(self):
		self.login_dialog = LoginDialog(self)
		self.login_dialog.exec_()


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
			self.close_database()

	def logout(self):
		self.access = False
		self.stacked_layout.setCurrentIndex(0)
		self.close_database()
		self.disable_actions()

	def closeEvent(self, event):
		self.deleteLater()

def showSplash():
	
	splash_pix = QPixmap('splash.png')
	splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
	progressBar = QProgressBar(splash)
	progressBar.setTextVisible(True)
	progressBar.setAlignment(Qt.AlignHCenter)
	progressBar.setAlignment(Qt.AlignBottom)
	splash.setMask(splash_pix.mask())
	splash.show()
	for i in range(0,100):
		progressBar.setValue(i)
		t = time.time()
		while time.time() < t + 0.1:
			app.processEvents()
	app.processEvents()
	time.sleep(2)
	splash.finish(splash)

if __name__ == "__main__":
	app = QApplication(sys.argv)
	#showSplash()
	window = MainWindow()
	window.show()
	window.raise_()
	app.exec_()
		
