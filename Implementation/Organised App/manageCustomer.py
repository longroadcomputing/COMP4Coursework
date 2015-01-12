from PyQt4.QtCore import  *
from PyQt4.QtGui import *
from PyQt4.QtSql import *


from SQLConnection import *
from editCustomerDialog import *

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
					self.mainWidget = QWidget()
					self.mainWidget.close()
					self.mainLayout.addWidget(self.mainWidget)

				#create widgets
				self.searchCustomersGroup = QGroupBox("Search Customers:")
				self.searchField = QLineEdit()

				self.searchLayout = QHBoxLayout()
				self.searchLayout.addWidget(self.searchField)

				self.searchCustomersGroup.setLayout(self.searchLayout)

				self.manageCustomersLayout = QVBoxLayout()
				self.manageCustomersLayout.addWidget(self.searchCustomersGroup)

				self.searchWidget = QWidget()
				self.searchWidget.setLayout(self.manageCustomersLayout)

				self.tableGroup = QGroupBox("Customer")

				self.results_table = QTableView()
				#self.results_table.setFixedHeight(400)

				header = QHeaderView(Qt.Horizontal, self.results_table)
				header.setStretchLastSection(True)

				self.results_table.setSelectionBehavior(QAbstractItemView.SelectRows)

				self.showAllCustomersButton = QPushButton("Show All Customers")
				self.backButton = QPushButton("<- Back")
				self.backButton.setShortcut('Esc')
				self.backButton.setMaximumWidth(75)
				self.showAllCustomersButton.setMaximumWidth(200)

				self.viewCustomersLayout = QGridLayout()
				self.viewCustomersLayout.addWidget(self.results_table,0,0)
				self.viewCustomersLayout.addWidget(self.showAllCustomersButton,1,0)

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
				self.mainLayout.setEnabled(True)

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


								self.searchCustomersGroup.setEnabled(False)
								self.tableGroup.setEnabled(False)

								self.editCustomer(data)
			
				
		def searchDatabase(self):

				queryText = self.searchField.text()

				query = self.connection.getSearchQuery(queryText)

				#print(queryText)

				self.showResults(query)
				
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
				self.searchField.textChanged.connect(self.searchDatabase)
				self.showAllCustomersButton.clicked.connect(self.showAllCustomersInTable)
				self.parent.mainMenu.manageCustomersButton.clicked.connect(self.showAllCustomersInTable)
				self.parent.manage_customer.triggered.connect(self.showAllCustomersInTable)
				self.backButton.clicked.connect(self.parent.switchToMainMenu)
				#self.results_table.selectionModel().selectionChanged.connect(self.changeFormFields)
				



		
				
