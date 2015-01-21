from PyQt4.QtCore import  *
from PyQt4.QtGui import *
from PyQt4.QtSql import *


from SQLConnection import *
from editDialog import *

import re

class ManageItemsWidget(QWidget):

		""" This is the manage clients widget """

		def __init__(self, parent):

				super().__init__()
				
				self.connection = None

				self.parent = parent

				self.results_table = None

				self.display = False

				self.currentRow = None

				self.model = QSqlQueryModel()
				
				self.setStyleSheet("QWidget[updateItem=True]{padding:100px;}")

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
				self.searchItemsGroup = QGroupBox("Search Items:")
				self.searchField = QLineEdit()
				self.searchButton = QPushButton("Search")
				self.searchButton.setAutoDefault(True)
				self.searchButton.setDefault(True)

				self.searchLayout = QHBoxLayout()
				self.searchLayout.addWidget(self.searchField)
				self.searchLayout.addWidget(self.searchButton)

				self.searchItemsGroup.setLayout(self.searchLayout)

				self.manageItemsLayout = QVBoxLayout()
				self.manageItemsLayout.addWidget(self.searchItemsGroup)

				self.searchWidget = QWidget()
				self.searchWidget.setLayout(self.manageItemsLayout)

				self.tableGroup = QGroupBox("Item")

				self.results_table = QTableView()
				self.results_table.setMaximumHeight(600)

				header = QHeaderView(Qt.Horizontal, self.results_table)
				header.setStretchLastSection(True)

				self.results_table.setSelectionBehavior(QAbstractItemView.SelectRows)

				self.showAllItemsButton = QPushButton("Show All Items")
				self.showAllItemsButton.setMaximumWidth(130)
				self.backButton = QPushButton("<- Back")
				self.backButton.setShortcut('Esc')
				self.backButton.setMaximumWidth(75)
				self.newRecordButton = QPushButton("New Item")

				self.buttonsLayout = QHBoxLayout()
				self.buttonsLayout.addWidget(self.backButton)
				self.buttonsLayout.addWidget(self.newRecordButton)
				self.buttonsLayout.setAlignment(self.newRecordButton, Qt.AlignRight)

				self.buttonsWidget = QWidget()
				self.buttonsWidget.setLayout(self.buttonsLayout)

				self.viewItemsLayout = QVBoxLayout()
				self.viewItemsLayout.addWidget(self.showAllItemsButton)
				self.viewItemsLayout.addWidget(self.results_table)
				
				self.tableGroup.setLayout(self.viewItemsLayout)

				self.groupL = QVBoxLayout()
				self.groupL.addWidget(self.tableGroup)

				self.groupWidget = QWidget()
				self.groupWidget.setLayout(self.groupL)

				self.vBoxLayout = QVBoxLayout()
				self.vBoxLayout.addWidget(self.buttonsWidget)
				self.vBoxLayout.addWidget(self.searchWidget)
				self.vBoxLayout.addWidget(self.groupWidget)

				return self.vBoxLayout

		def editItem(self, data):
				self.editItemDialog = editItemDialog(self)
				self.editItemDialog.addConnection(self.connection)
				self.editItemDialog.clearForm()
				self.editItemDialog.populateEditFields(data)
				self.editItemDialog.exec_()
				self.results_table.selectionModel().clearSelection()
				self.searchItemsGroup.setEnabled(True)
				self.tableGroup.setEnabled(True)

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
								ID = int(self.currentRow) + 2
								data = self.connection.getItemData(ID)

								self.searchItemsGroup.setEnabled(False)
								self.tableGroup.setEnabled(False)

								self.editItem(data)
			
				
		def searchDatabase(self):

				queryText = self.searchField.text()

				query = self.connection.getItemSearchQuery(queryText)

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
			self.parent.switchToNewItem()

				
		def showAllItemsInTable(self):
				self.searchField.clear()

				query = self.connection.getAllItems()

				self.showResults(query)

				
		def addConnection(self, connection):
				
				self.connection = connection

				self.connections()
				
				return True

		def editingItem(self):
				
				self.searchItemsGroup.setEnabled(False)
				self.tableGroup.setEnabled(False)

				self.editItem()


		def searchingItems(self):


				self.results_table.selectionModel().clearSelection()
				
				self.searchItemsGroup.setEnabled(True)
				self.tableGroup.setEnabled(True)
				
				self.editItemGroupBox.setEnabled(False)

				

		def showResults(self, query):
				self.model.setQuery(query)
				self.results_table.setModel(self.model)
				self.results_table.setSortingEnabled(True)
				self.results_table.show()

				self.results_table.selectionModel().selectionChanged.connect(self.changeFormFields)
				
		def connections(self):
				self.searchField.returnPressed.connect(self.searchDatabase)
				self.searchButton.clicked.connect(self.searchDatabase)
				self.showAllItemsButton.clicked.connect(self.showAllItemsInTable)
				self.parent.mainMenu.manageItemsButton.clicked.connect(self.showAllItemsInTable)
				self.parent.manage_item.triggered.connect(self.showAllItemsInTable)
				self.backButton.clicked.connect(self.parent.switchToMainMenu)
				self.newRecordButton.clicked.connect(self.parent.switchToNewItem)
				#self.results_table.selectionModel().selectionChanged.connect(self.changeFormFields)
				



		
				
