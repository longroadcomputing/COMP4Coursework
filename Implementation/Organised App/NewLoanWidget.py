from PyQt4.QtGui import *
from PyQt4.QtCore import *

from date_widget import *
from selectItemDialog import *

import sys
import time

import sqlite3

class newLoanWidget(QWidget):
	"""docstring for newLoanWidget"""
	def __init__(self, parent):
		super().__init__()

		self.setProperty("addCustomerClass","True")

		self.connection = None

		self.parent = parent
		
		self.leftWidget = QWidget()

		self.leftTopWidget = QWidget()
		self.leftBottomWidget = QTabWidget()

		self.leftTopWidget.setFixedHeight(200)
		self.leftBottomWidget.setFixedHeight(200)

		self.leftLayout = QVBoxLayout()
		self.leftLayout.addWidget(self.leftTopWidget)
		self.leftLayout.addWidget(self.leftBottomWidget)

		self.leftWidget.setLayout(self.leftLayout)

		self.leftTopLayout = self.newLoanLayout()

		self.leftTopWidget.setLayout(self.leftTopLayout)

		self.rightWidget = QWidget()
		self.rightWidget.setFixedWidth(300)
		self.rightWidget.setFixedHeight(600)


		self.mainLayout = QHBoxLayout()
		self.mainLayout.addWidget(self.leftWidget)
		self.mainLayout.addWidget(self.rightWidget)

		self.setStyleSheet("QWidget[addCustomerClass=True]{padding:100px;}")

	def addConnection(self, connection):
		self.connection = connection
		return True

	def newLoanLayout(self):
		self.newLoanHeading = QLabel("New Loan")
		self.newLoanHeading.setAlignment(Qt.AlignCenter)
		self.shadow = QGraphicsDropShadowEffect()
		self.shadow.setBlurRadius(5)
		self.newLoanHeading.setGraphicsEffect(self.shadow)
		self.newLoanHeading.setStyleSheet("font-size:20px")

		self.customerLabel = QLabel("Customer:*")

		self.customerDropDown = QComboBox()

		self.customerDropDown.addItem("Please select...")
		

		j = self.customerDropDown.model().index(0,0)
		self.customerDropDown.model().setData(j, 0, Qt.UserRole-1)

		self.parent.mainMenu.newLoanButton.clicked.connect(self.populateDropDowns)

		self.LoanLengthLabel = QLabel("Loan Length:*")

		self.LoanLengthSpinBox = QSpinBox()
		self.LoanLengthSpinBox.setRange(1,7)
		self.LoanLengthSpinBox.setSuffix(" Days")

		self.spacerWidget = QWidget()

		self.ItemDropDown = QComboBox()
		self.ItemDropDown.addItem("Please select...")

		j = self.customerDropDown.model().index(0,0)
		self.customerDropDown.model().setData(j, 0, Qt.UserRole-1)

		self.loanRateLabel = QLabel("Loan Rate:*")

		self.loanRate = QLineEdit()

		grid = QGridLayout()
		grid.setSpacing(10)

		grid.addWidget(self.customerLabel,0,0)
		grid.addWidget(self.customerDropDown,0,1)

		grid.addWidget(self.LoanLengthLabel,1,0)
		grid.addWidget(self.LoanLengthSpinBox,1,1)

		self.gridWidget = QWidget()
		self.gridWidget.setLayout(grid)

		self.verticalLayout = QVBoxLayout()
		self.verticalLayout.addWidget(self.newLoanHeading)
		self.verticalLayout.addWidget(self.gridWidget)

		self.cancelButton = QPushButton("Cancel")
		self.cancelButton.setShortcut('Esc')
		self.cancelButton.setAutoDefault(False)
		self.cancelButton.setDefault(False)

		self.confirmButton = QPushButton("Confirm")
		self.confirmButton.setShortcut('Return')
		self.confirmButton.setAutoDefault(True)
		self.confirmButton.setDefault(True)

		self.buttonsLayout = QHBoxLayout()
		self.buttonsLayout.addWidget(self.cancelButton)
		self.buttonsLayout.addWidget(self.confirmButton)

		self.buttonsWidget = QWidget()
		self.buttonsWidget.setLayout(self.buttonsLayout)

		self.leftLayout.addWidget(self.buttonsWidget)


		#connections
		self.cancelButton.clicked.connect(self.parent.switchToMainMenu)

		return self.verticalLayout

	def populateDropDowns(self):
		with sqlite3.connect(self.connection.path) as db:
			cursor = db.cursor()
			sql = ("""SELECT CustomerID, Title, FirstName, LastName, Company, Street, Town, County, PostCode, Mobile, Landline, Email  FROM Customer ORDER BY FirstName ASC""")
			cursor.execute(sql)
			self.customers = cursor.fetchall()

			for customer in self.customers:
				self.customerDropDown.addItem("{0} {1} {2} ({3}): [{4} {5} {6} {7}]".format(customer[1], customer[2], customer[3], customer[4], customer[5], customer[6], customer[7], customer[8]))

	def selectItem(self):
		Date = "1"
		self.selectItemDialog = selectItemDialog(Date)
		self.selectItemDialog.exec_()