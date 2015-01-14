from PyQt4.QtCore import  *
from PyQt4.QtGui import *
from PyQt4.QtSql import *


from SQLConnection import *
from editDialog import *

import re

class ManageCustomersWidget(QWidget):

		""" This is the manage clients widget """

		def __init__(self, parent):

				super().__init__()
				
				self.connection = None

				self.parent = parent

				self.results_table = None

				self.display = False

				self.currentRow = None

				self.model = QSqlQueryModel()
				
				self.setStyleSheet("QWidget[addplastererClass=True]{padding:100px;}")

				self.mainWidget = QWidget()
				self.mainLayout = QVBoxLayout()
				self.mainLayout.setAlignment(Qt.AlignHCenter)

				self.Layout = self.layout()

				self.mainWidget.setLayout(self.Layout)

				self.mainLayout.addWidget(self.mainWidget)

				self.setLayout(self.mainLayout)

				self.currentMemberId = None

		def addConnection(self, connection):
				self.connection = connection
				self.connections()
				return True

		def layout(self):
				if hasattr(self, 'mainWidget'):
					self.mainWidget.close()
					self.mainWidget = QWidget()

				#create widgets
				self.searchCustomersGroup = QGroupBox("Search Customers:")
				self.searchField = QLineEdit()
				self.searchButton = QPushButton("Search")

				self.searchLayout = QHBoxLayout()
				self.searchLayout.addWidget(self.searchField)
				self.searchLayout.addWidget(self.searchButton)

				self.searchCustomersGroup.setLayout(self.searchLayout)

				self.manageCustomersLayout = QVBoxLayout()
				self.manageCustomersLayout.addWidget(self.searchCustomersGroup)

				self.searchWidget = QWidget()
				self.searchWidget.setLayout(self.manageCustomersLayout)

				self.tableGroup = QGroupBox("Customer")

				self.results_table = QTableView()
				self.results_table.setMaximumHeight(600)

				header = QHeaderView(Qt.Horizontal, self.results_table)
				header.setStretchLastSection(True)

				self.results_table.setSelectionBehavior(QAbstractItemView.SelectRows)

				self.showAllCustomersButton = QPushButton("Show All Customers")
				self.backButton = QPushButton("<- Back")
				self.backButton.setShortcut('Esc')
				self.backButton.setMaximumWidth(75)
				self.showAllCustomersButton.setMaximumWidth(200)

				self.viewCustomersLayout = QVBoxLayout()
				self.viewCustomersLayout.addWidget(self.results_table)
				self.viewCustomersLayout.addWidget(self.showAllCustomersButton)

				self.tableGroup.setLayout(self.viewCustomersLayout)

				self.groupL = QVBoxLayout()
				self.groupL.addWidget(self.tableGroup)

				self.groupWidget = QWidget()
				self.groupWidget.setLayout(self.groupL)

				self.vBoxLayout = QVBoxLayout()
				self.vBoxLayout.addWidget(self.backButton)
				self.vBoxLayout.addWidget(self.searchWidget)
				self.vBoxLayout.addWidget(self.groupWidget)

				return self.vBoxLayout

		def editCustomer(self, data):
				self.editCustomerDialog = editCustomerDialog(self)
				self.editCustomerDialog.addConnection(self.connection)
				self.editCustomerDialog.clearForm()
				self.editCustomerDialog.populateEditFields(data)
				self.editCustomerDialog.exec_()

		def changeFormFields(self):

				selectedIndexes = self.results_table.selectionModel().selection().indexes()

				rows = []

				for each in selectedIndexes:

						rowNum = each.row()

						if rowNum not in rows:
								rows.append(rowNum)

				numberOfRowsSelected = len(rows)

				if numberOfRowsSelected == 1:
						if self.currentRow != rows[0]:
								self.currentRow = rows[0]
								ID = int(self.currentRow) + 1
								data = self.connection.getCustomerData(ID)

								print(data)

								self.searchCustomersGroup.setEnabled(False)
								self.tableGroup.setEnabled(False)

								self.editCustomer(data)
			
				
		def searchDatabase(self):

				queryText = self.searchField.text()

				query = self.connection.getCustomerSearchQuery(queryText)

				# if query:
				# 	self.error_message_dialog = QMessageBox()
				# 	self.error_message_dialog.setFixedWidth(200)
				# 	self.error_message_dialog.setWindowTitle("Database Error")
				# 	self.error_message_dialog.setText("Error! A record with that search parameter \n"
				# 										"cannot be found. \n"
				# 										"Would you like to search again or enter a new record?")
				# 	self.error_message_dialog.setDetailedText("Database Error:\n \n "
				# 									  "{0}".format(self.connection.error))
				# 	self.error_message_dialog.setIcon(QMessageBox.Question)
				# 	self.seach_again = self.error_message_dialog.addButton(self.parent.tr("Search Again"), QMessageBox.AcceptRole)
				# 	self.new_record = self.error_message_dialog.addButton(self.parent.tr("Enter New Record"), QMessageBox.AcceptRole)
				# 	self.error_message_dialog.setEscapeButton(self.seach_again)
				# 	self.error_message_dialog.setDefaultButton(self.new_record)
				# 	self.seach_again.clicked.connect(self.searchAgain)
				# 	self.new_record.clicked.connect(self.newRecord)
				# 	self.error_message_dialog.exec_()

				# print(queryText)

				self.showResults(query)

		def searchAgain(self):
			pass

		def newRecord(self):
			self.parent.switchToNewCustomer()

				
		def showAllCustomersInTable(self):

				query = self.connection.getAllCustomers()

				self.showResults(query)

				
		def addConnection(self, connection):
				
				self.connection = connection

				self.connections()
				
				return True

		def editingCustomer(self):
				
				self.searchCustomersGroup.setEnabled(False)
				self.tableGroup.setEnabled(False)

				self.editCustomer()


		def searchingCustomers(self):


				self.results_table.selectionModel().clearSelection()
				
				self.searchCustomersGroup.setEnabled(True)
				self.tableGroup.setEnabled(True)
				
				self.editCustomerGroupBox.setEnabled(False)

				

		def showResults(self, query):
				
				self.model.setQuery(query)
				self.results_table.setModel(self.model)
				self.results_table.setSortingEnabled(True)
				self.results_table.show()

				self.results_table.selectionModel().selectionChanged.connect(self.changeFormFields)
				
		def connections(self):
				self.searchButton.clicked.connect(self.searchDatabase)
				self.showAllCustomersButton.clicked.connect(self.showAllCustomersInTable)
				self.parent.mainMenu.manageCustomersButton.clicked.connect(self.showAllCustomersInTable)
				self.parent.manage_customer.triggered.connect(self.showAllCustomersInTable)
				self.backButton.clicked.connect(self.parent.switchToMainMenu)
				#self.results_table.selectionModel().selectionChanged.connect(self.changeFormFields)
				



		
				
