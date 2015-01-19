from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *

import sys
import time

from SQLConnection import *

class SelectItemDialog(QDialog):
	"""docstring for SelectItemDialog"""
	def __init__(self, parent):
		super().__init__()

		self.resize(357, 400)

		self.parent = parent

		self.setWindowTitle("Select Item")

		self.model = QSqlQueryModel()

		layout = self.layout()

		self.setLayout(layout)

		self.currentRow = None

		self.currentMemberId = None


	def addConnection(self, connection):
		self.connection = connection
		return True


	def layout(self):
		self.titleLabel = QLabel("Select an Item from below to add to the Loan:")

		self.ItemTableView = QTableView()
		self.ItemTableView.setMaximumHeight(600)

		self.cancelButton = QPushButton("Cancel")
		self.cancelButton.setMaximumWidth(70)
		self.cancelButton.setAutoDefault(False)
		self.cancelButton.setDefault(False)

		self.mainLayout = QVBoxLayout()
		self.mainLayout.addWidget(self.titleLabel)
		self.mainLayout.addWidget(self.ItemTableView)
		self.mainLayout.addWidget(self.cancelButton)
		self.mainLayout.setAlignment(self.cancelButton, Qt.AlignRight)

		self.cancelButton.setShortcut('Ctrl+W')
		self.cancelButton.clicked.connect(self.close)

		return self.mainLayout

	def changeFormFields(self):

				selectedIndexes = self.ItemTableView.selectionModel().selection().indexes()

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
								data = self.connection.getItemDataForLoan(ID)

								self.parent.addToLoan(data)
								self.close()

	def showAllItemsInTable(self):

			query = self.connection.getAllItemsForLoan()

			self.showResults(query)
			

	def showResults(self, query):
			
			self.model.setQuery(query)
			self.ItemTableView.setModel(self.model)
			self.ItemTableView.setSortingEnabled(True)
			self.ItemTableView.show()

			self.ItemTableView.selectionModel().selectionChanged.connect(self.changeFormFields)
			
	def connections(self):
		pass


