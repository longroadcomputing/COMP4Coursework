from PyQt4.QtCore import  *
from PyQt4.QtGui import *
from PyQt4.QtSql import *


from SQLConnection import *

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

		self.mainLayout = QVBoxLayout()
		
		self.topWidget = QWidget()
		self.bottomWidget = QWidget()

		self.leftLayout = self.layout()

		self.topWidget.setLayout(self.leftLayout)

		self.mainLayout.addWidget(self.topWidget)
		self.mainLayout.addWidget(self.bottomWidget)

		self.setLayout(self.mainLayout)

		self.currentMemberId = None

	def addConnection(self, connection):
		self.connection = connection
		self.connections()
		return True

	def layout(self):
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

		header = QHeaderView(Qt.Horizontal, self.results_table)
		header.setStretchLastSection(True)

		self.results_table.setSelectionBehavior(QAbstractItemView.SelectRows)

		self.showAllCustomersButton = QPushButton("Show All Customers")
		self.showAllCustomersButton.setMaximumWidth(200)

		self.viewCustomersLayout = QGridLayout()
		self.viewCustomersLayout.addWidget(self.results_table,0,0)
		self.viewCustomersLayout.addWidget(self.showAllCustomersButton,1,0)

		self.tableGroup.setLayout(self.viewCustomersLayout)

		self.groupL = QVBoxLayout()
		self.groupL.addWidget(self.tableGroup)

		self.groupWidget = QWidget()
		self.groupWidget.setLayout(self.groupL)

		self.editCustomerWidget = self.editCustomer()
		self.bottomWidget.setLayout(self.editCustomerWidget)

		self.vBoxLayout = QVBoxLayout()
		self.vBoxLayout.addWidget(self.searchWidget)
		self.vBoxLayout.addWidget(self.groupWidget)

		return self.vBoxLayout

	def editCustomer(self):
		self.layout = QVBoxLayout()
		return self.layout

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

		self.editCustomerGroupBox.setEnabled(True)


	def searchingCustomers(self):
		#clear edit form
		self.firstNameEdit.clear()
		self.surnameEdit.clear()
		self.streetEdit.clear()
		self.townEdit.clear()
		self.postCodeEdit.clear()
		self.emailEdit.clear()
		self.phoneNumberEdit.clear()
		self.errorTextContentLabel.clear()

		self.firstNameEdit.setStyleSheet("")
		self.surnameEdit.setStyleSheet("")
		self.streetEdit.setStyleSheet("")
		self.townEdit.setStyleSheet("")
		self.countyEdit.setStyleSheet("")
		self.postCodeEdit.setStyleSheet("")
		self.emailEdit.setStyleSheet("")
		self.phoneNumberEdit.setStyleSheet("")


		self.results_table.selectionModel().clearSelection()
		
		self.searchCustomersGroup.setEnabled(True)
		self.tableGroup.setEnabled(True)
		
		self.editCustomerGroupBox.setEnabled(False)

		
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
				cliID = int(self.currentRow) + 1
				data = self.connection.getCustomerData(cliID)


				self.searchCustomersGroup.setEnabled(False)
				self.tableGroup.setEnabled(False)
				self.editCustomerGroupBox.setEnabled(True)

				self.editCustomerPopulate(data)




							
	def editCustomerPopulate(self, data):

		currentId = data[0]
		title = data[1]
		firstName = data[2]
		surname = data[3]
		street = data[4]
		town = data[5]
		county = data[6]
		postCode = data[7]
		email = data[8]
		phoneNumber = data[9]

		self.currentMemberId = currentId

		self.titleIndex = self.titleEdit.findText(title)
		self.titleEdit.setCurrentIndex(self.titleIndex)

		self.firstNameEdit.setText(firstName)
		self.surnameEdit.setText(surname)
		self.streetEdit.setText(street)
		self.townEdit.setText(town)

		self.countyIndex = self.countyEdit.findText(county)
		self.countyEdit.setCurrentIndex(self.countyIndex)

		self.postCodeEdit.setText(postCode)
		self.emailEdit.setText(email)
		self.phoneNumberEdit.setText(phoneNumber)

		

	def showResults(self, query):
		
		self.model.setQuery(query)
		self.results_table.setModel(self.model)
		self.results_table.setSortingEnabled(True)
		self.results_table.show()

		self.results_table.selectionModel().selectionChanged.connect(self.changeFormFields)
		
	def connections(self):
		self.searchField.textChanged.connect(self.searchDatabase)
		self.showAllCustomersButton.clicked.connect(self.showAllCustomersInTable)
		#self.results_table.selectionModel().selectionChanged.connect(self.changeFormFields)
		
		self.firstNameEdit.textChanged.connect(self.validateFirstName)
		self.surnameEdit.textChanged.connect(self.validateSurname)
		self.streetEdit.textChanged.connect(self.validateStreet)
		self.townEdit.textChanged.connect(self.validateTown)
		self.postCodeEdit.textChanged.connect(self.validatePostCode)
		self.emailEdit.textChanged.connect(self.validateEmail)
		self.phoneNumberEdit.textChanged.connect(self.validatePhoneNumber)
		self.savePushButton.clicked.connect(self.validateForm)
		self.cancelPushButton.clicked.connect(self.searchingCustomers)


	def addUpdatedDataToDb(self):
		county = str(self.countyEdit.currentText())
		title = str(self.titleEdit.currentText())

		values = {"ID" : self.currentMemberId,
					"Title": title,
				   "FirstName": self.firstNameEdit.text(),
				  "Surname": self.surnameEdit.text(),
				  "Street": self.streetEdit.text(),
				  "Town": self.townEdit.text(),
				  "County": county,
				  "PostCode": self.postCodeEdit.text(),
				  "Email": self.emailEdit.text(),
				   "PhoneNumber": self.phoneNumberEdit.text()}

		clientAdded = self.connection.updateCustomer(values)

		if clientAdded:

			self.searchingCustomers()
			 
			infoText = """ The clients information has been updated!"""
			QMessageBox.information(self, "Customer Info Updated!", infoText)
			
		else:
			infoText = """ The client was not updated successfully! """

			QMessageBox.critical(self, "Customer Not Updated!", infoText)
		

	def validateTitle(self):
		text = self.customerTitle.currentText()

		if text == "Please select...":
			return False
		else:
			return True

	def validateFirstName(self):

		text = self.customerFirstName.text()
		length = len(text)

		if length > 2:
			self.customerFirstName.setStyleSheet("background-color:#c4df9b;")
			return True
		else:
			self.customerFirstName.setStyleSheet("background-color:#f6989d;")
			return False

	def validateSurname(self):

		text = self.customerSurname.text()
		length = len(text)

		if length > 2:
			self.customerSurname.setStyleSheet("background-color:#c4df9b;")
			return True
		else:
			self.customerSurname.setStyleSheet("background-color:#f6989d;")
			return False

	def validateCompany(self):

		text = self.customerCompany.text()
		length = len(text)

		if text == '-' or text =='':
			return True

	def validateStreet(self):

		text = self.customerStreet.text()
		length = len(text)

		if length > 5:
			self.customerStreet.setStyleSheet("background-color:#c4df9b;")
			return True
		else:
			self.customerStreet.setStyleSheet("background-color:#f6989d;")
			return False


	def validateTown(self):
		
		text = self.customerTown.text()
		length = len(text)

		if length > 3:
			self.customerTown.setStyleSheet("background-color:#c4df9b;")
			return True
		else:
			self.customerTown.setStyleSheet("background-color:#f6989d;")
			return False

	def validateCounty(self):
		text = self.customerCounty.currentText()

		if text == "Please select...":
			return False
		else:
			return True


	def validatePostCode(self):
		
		text = self.customerPostCode.text()

		postCodeRegEx = re.compile("^[A-Z]{1,2}[0-9][0-9A-Z]?\s?[0-9][A-Z]{2}$")

		match = postCodeRegEx.match(text.upper())

		if match:
			self.customerPostCode.setStyleSheet("background-color:#c4df9b;")
			return True
		else:
			self.customerPostCode.setStyleSheet("background-color:#f6989d;")
			return False

	def validateMobile(self):
		text = self.customerMobile.text()
		length = len(text)

		no_letters = re.search('^[a-z],[A-z]*$', text)
		valid_mobile = re.search('^(((\+44\s?\d{4}|\(?0\d{4}\)?)\s?\d{3}\s?\d{3})|((\+44\s?\d{3}|\(?0\d{3}\)?)\s?\d{3}\s?\d{4})|((\+44\s?\d{2}|\(?0\d{2}\)?)\s?\d{4}\s?\d{4}))(\s?\#(\d{4}|\d{3}))?$', text)
		if not no_letters and valid_mobile:
			valid = True
		else:
			valid = False

		if length >= 11 and valid == True:
			self.customerMobile.setStyleSheet("background-color:#c4df9b;")
			return True
		else:
			self.customerMobile.setStyleSheet("background-color:#f6989d;")
			return False


	def validateUKLandline(self):
		text = self.customerLandline.text()
		length = len(text)

		no_letters = re.search('^[a-z],[A-z]*$', text)
		valid_landline_number = re.search('^((\(?0\d{4}\)?\s?\d{3}\s?\d{3})|(\(?0\d{3}\)?\s?\d{3}\s?\d{4})|(\(?0\d{2}\)?\s?\d{4}\s?\d{4}))(\s?\#(\d{4}|\d{3}))?$', text)
		if not no_letters and valid_landline_number:
			valid = True
		else:
			valid = False

		if length >= 11 and valid == True:
			self.customerLandline.setStyleSheet("background-color:#c4df9b;")
			return True
		else:
			self.customerLandline.setStyleSheet("background-color:#f6989d;")
			return False

	def validateEmail(self):
		text = self.customerEmail.text()

		emailRegEx = re.compile("^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$")

		match = emailRegEx.match(text)

		if match:
			self.customerEmail.setStyleSheet("background-color:#c4df9b;")
			return True
		else:
			self.customerEmail.setStyleSheet("background-color:#f6989d;")
			return False

	def validateAddcustomerForm(self):

		checkTitle = self.validateTitle()
		checkFirstName = self.validateFirstName()
		checkSurname = self.validateSurname()
		checkCompany = self.validateCompany()
		checkStreet = self.validateStreet()
		checkTown = self.validateTown()
		checkCounty = self.validateCounty()
		checkPostCode = self.validatePostCode()
		checkMobile = self.validateMobile()
		checkLandline = self.validateUKLandline()
		checkEmail = self.validateEmail()

		error_count = 0

		if checkTitle == False:
			error_count += 1
		if checkFirstName == False:
			error_count += 1
		if checkSurname == False:
			error_count += 1
		if checkCompany == False:
			error_count += 1
		if checkStreet == False:
			error_count += 1
		if checkTown == False:
			error_count += 1
		if checkCounty == False:
			error_count += 1
		if checkPostCode == False:
			error_count += 1
		if checkMobile == False:
			error_count += 1
		if checkLandline == False:
			error_count += 1
		if checkEmail == False:
			error_count += 1

		if error_count > 0:
			self.error_message_dialog = QMessageBox()
			self.error_message_dialog.setFixedWidth(200)
			self.error_message_dialog.setWindowTitle("Input Error")
			self.error_message_dialog.setText("Error! Some data entered is invalid \n"
											  "\n"
											  "Click the 'Show details' button for more information")
			self.error_message_dialog.setDetailedText("The information entered is invalid \n"
													"Steps to take: \n"
													"\n"
													"    1. Make sure that valid post-codes and numbers are \n"
													"       entered into the required fields. \n"
													"    2. The drop-down menus should NOT have \n"
													"       'Please select...' as an option for data input. \n")
			self.error_message_dialog.setIcon(QMessageBox.Warning)
			self.okay_button = self.error_message_dialog.addButton(self.tr("Okay"), QMessageBox.AcceptRole)
			self.error_message_dialog.setEscapeButton(self.okay_button)
			self.error_message_dialog.setDefaultButton(self.okay_button)
			self.okay_button.clicked.connect(self.editEntry)
			self.error_message_dialog.exec_()
		else: 
			self.addCustomerToDatabase()