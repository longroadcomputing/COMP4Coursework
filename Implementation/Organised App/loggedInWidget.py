from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys
import re

class loggedInWidget(QWidget):
	"""docstring for loggedInWidget"""
	def __init__(self, parent):
		super().__init__()

		self.setProperty("loggedInClass", "True")

		self.parent = parent

		self.mainLayout = self.layout()
		self.mainLayout.setAlignment(Qt.AlignHCenter)

		self.setLayout(self.mainLayout)

		self.setStyleSheet("QWidget[loggedInClass=True]{padding:100px;}")

	def layout(self):

		self.mainMenuText = QLabel("Main Menu")
		self.mainMenuText.setAlignment(Qt.AlignCenter)
		self.shadow = QGraphicsDropShadowEffect()
		self.shadow.setBlurRadius(5)
		self.mainMenuText.setGraphicsEffect(self.shadow)
		self.mainMenuText.setStyleSheet("font-size:30px;")

		self.setStyleSheet("""QPushButton[buttonClass=home] {
					   font-size: 16px; background-color: rgba(188, 188, 188, 50);
					   border: 1px solid rgba(188, 188, 188, 250);
					   width:200px;
					   height:100px:
					   border-radius:5px;}""")



		self.newItemButton = QPushButton("New Item")
		self.newItemButton.setProperty("buttonClass","home")
		self.newItemButton.setCursor(QCursor(Qt.PointingHandCursor))

		self.manageItemsButton = QPushButton("Manage Items")
		self.manageItemsButton.setProperty("buttonClass","home")
		self.manageItemsButton.setCursor(QCursor(Qt.PointingHandCursor))

		self.ItemLayout = QVBoxLayout()

		self.ItemLayout.addWidget(self.newItemButton)
		self.ItemLayout.addWidget(self.manageItemsButton)
		
		self.ItemWidget = QWidget()

		self.ItemWidget.setLayout(self.ItemLayout)






		self.newCustomerButton = QPushButton("New Customer")
		self.newCustomerButton.setProperty("buttonClass","home")
		self.newCustomerButton.setCursor(QCursor(Qt.PointingHandCursor))

		self.manageCustomersButton = QPushButton("Manage Customers")
		self.manageCustomersButton.setProperty("buttonClass","home")
		self.manageCustomersButton.setCursor(QCursor(Qt.PointingHandCursor))

		self.CustomerLayout = QVBoxLayout()

		self.CustomerLayout.addWidget(self.newCustomerButton)
		self.CustomerLayout.addWidget(self.manageCustomersButton)
		
		self.CustomerWidget = QWidget()

		self.CustomerWidget.setLayout(self.CustomerLayout)






		self.newLoanButton = QPushButton("New Loan")
		self.newLoanButton.setProperty("buttonClass","home")
		self.newLoanButton.setCursor(QCursor(Qt.PointingHandCursor))

		self.manageLoansButton = QPushButton("Manage Loans")
		self.manageLoansButton.setProperty("buttonClass","home")
		self.manageLoansButton.setCursor(QCursor(Qt.PointingHandCursor))

		self.LoanLayout = QVBoxLayout()

		self.LoanLayout.addWidget(self.newLoanButton)
		self.LoanLayout.addWidget(self.manageLoansButton)
		
		self.LoanWidget = QWidget()

		self.LoanWidget.setLayout(self.LoanLayout)






		self.newPatTestButton = QPushButton("New PatTest")
		self.newPatTestButton.setProperty("buttonClass","home")
		self.newPatTestButton.setCursor(QCursor(Qt.PointingHandCursor))

		self.managePatTestsButton = QPushButton("Manage PatTests")
		self.managePatTestsButton.setProperty("buttonClass","home")
		self.managePatTestsButton.setCursor(QCursor(Qt.PointingHandCursor))

		self.PatTestLayout = QVBoxLayout()

		self.PatTestLayout.addWidget(self.newPatTestButton)
		self.PatTestLayout.addWidget(self.managePatTestsButton)
		
		self.PatTestWidget = QWidget()

		self.PatTestWidget.setLayout(self.PatTestLayout)



		self.logoutButton = QPushButton("Logout")
		self.logoutButton.setShortcut('Esc')
		self.changePasswordButton = QPushButton("Change Password")

		self.logoutButton.setFixedWidth(200)
		self.changePasswordButton.setFixedWidth(200)


		grid = QGridLayout()
		grid.setSpacing(10)

		grid.addWidget(self.ItemWidget,0,0)
		grid.addWidget(self.CustomerWidget,0,1)
		grid.addWidget(self.LoanWidget,1,0)
		grid.addWidget(self.PatTestWidget,1,1)

		self.gridWidget = QWidget()
		self.gridWidget.setLayout(grid)

		self.verticalLayout = QVBoxLayout()
		self.verticalLayout.addWidget(self.mainMenuText)
		self.verticalLayout.addStretch(1)
		self.verticalLayout.addWidget(self.gridWidget)

		self.hBoxL = QHBoxLayout()
		self.hBoxL.addWidget(self.logoutButton)
		self.hBoxL.addWidget(self.changePasswordButton)
		self.hButtonL = QWidget()
		self.hButtonL.setLayout(self.hBoxL)
		
		self.verticalLayout.addWidget(self.hButtonL)
		self.verticalLayout.addStretch(1)

		#connections
		self.newItemButton.clicked.connect(self.parent.switchToNewItem)
		self.newCustomerButton.clicked.connect(self.parent.switchToNewCustomer)
		self.newLoanButton.clicked.connect(self.parent.switchToNewLoan)
		self.newPatTestButton.clicked.connect(self.parent.switchToNewPatTest)

		self.manageItemsButton.clicked.connect(self.parent.switchToManageItems)
		self.manageCustomersButton.clicked.connect(self.parent.switchToManageCustomers)


		return self.verticalLayout




