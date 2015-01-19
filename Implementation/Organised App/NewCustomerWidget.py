from PyQt4.QtCore import  *
from PyQt4.QtGui import *
from SQLConnection import *

import re

class newCustomerWidget(QWidget):

	""" This is the add customer widget """

	def __init__(self, parent):

		super().__init__()
		
		self.setProperty("addCustomerClass","True")

		self.connection = None

		self.parent = parent

		self.mainLayout = QHBoxLayout()
		
		self.leftWidget = QWidget()

		self.leftWidget.setFixedWidth(300)
		self.leftWidget.setFixedHeight(600)

		self.leftLayout = self.newCustomerLayout()
		self.mainLayout.setAlignment(Qt.AlignHCenter)


		self.leftWidget.setLayout(self.leftLayout)

		self.mainLayout.addWidget(self.leftWidget)
		

		self.setStyleSheet("QWidget[addCustomerClass=True]{padding:100px;}")

	def addConnection(self, connection):
		self.connection = connection
		return True


	def newCustomerLayout(self):
		self.counties = ['Please select...','Aberdeenshire', 'Angus', 'Argyll and Bute', 'Ayrshire', 'Ayrshire and Arran',
						 'Banffshire', 'Bedfordshire', 'Berkshire','Berwickshire', 'Buckinghamshire',
						 'Caithness', 'Cambridgeshire', 'Ceredigion', 'Cheshire', 'City of Bristol', 'City of Edinburgh',
						 'City of Glasgow', 'Clwyd', 'Cornwall', 'Cumbria', 'Denbighshire', 'Derbyshire', 'Devon', 'Dorset',
						 'Dumbartonshire', 'Dumfries','Durham', 'Dyfed', 'East Lothian', 'East Sussex', 'East Yorkshire', 'Essex',
						 'Ettrick and Lauderdale', 'Fife', 'Gloucestershire','Greater London', 'Greater Manchester', 'Gwent', 'Gwynedd',
						 'Hampshire', 'Herefordshire', 'Hertfordshire', 'Highlands', 'Inverness','Isle of Skye', 'Isle of Wight', 'Kent',
						 'Lanarkshire', 'Lancashire', 'Leicestershire', 'Lincolnshire', 'Merseyside', 'Mid Glamorgan','Morayshire', 'Norfolk',
						 'North Yorkshire', 'Northamptonshire', 'Northumberland', 'Nottinghamshire', 'Orkney', 'Oxfordshire', 'Perth and Kinross',
						 'Powys', 'Renfrewshire', 'Roxburgh', 'Shetland', 'Shropshire', 'Somerset', 'South Glamorgan', 'South Yorkshire', 'Staffordshire',
						 'Stirling and Falkirk', 'Suffolk', 'Surrey', 'Sutherland', 'Tweeddale', 'Tyne and Wear', 'Warwickshire', 'West Glamorgan',
						 'West Lothian', 'West Midlands', 'West Sussex', 'West Yorkshire', 'Western Isles', 'Wiltshire', 'Worcestershire']

		customerTitleLabel = QLabel('Title:*')
		customerFirstNameLabel = QLabel('First Name:*')
		customerSurnameLabel = QLabel('Surname:*')
		customerCompanyLabel = QLabel('Company:')
		customerStreetLabel = QLabel('Street:*')
		customerTownLabel = QLabel('Town/City:*')
		customerCountyLabel = QLabel('County:*')
		customerPostCodeLabel = QLabel('Post Code:*')
		customerMobileLabel = QLabel('Mobile Number:*')
		customerLandlineLabel = QLabel('Landline Number:*')
		customerEmailLabel = QLabel('Email:*')
		smallPrint = QLabel('* required fields.')
		smallPrint.setStyleSheet("font-size:11pt")

		self.customerTitle = QComboBox()
		self.titles = ["Please select...","Mr","Mrs","Ms","Miss"]
		self.customerTitle.addItems(self.titles)

		j = self.customerTitle.model().index(0,0)
		self.customerTitle.model().setData(j, 0, Qt.UserRole-1)

		self.customerFirstName = QLineEdit()
		self.customerSurname = QLineEdit()
		self.customerStreet = QLineEdit()
		self.customerCompany = QLineEdit()
		self.customerTown = QLineEdit()

		self.customerCounty = QComboBox()
		self.customerCounty.addItems(self.counties)

		j = self.customerCounty.model().index(0,0)
		self.customerCounty.model().setData(j, 0, Qt.UserRole-1)


		self.customerPostCode = QLineEdit()
		self.customerMobile = QLineEdit()
		self.customerLandline = QLineEdit()
		self.customerEmail = QLineEdit()

		self.addcustomerTitleText = QLabel("Add New customer")
		self.addcustomerTitleText.setAlignment(Qt.AlignCenter)
		self.shadow = QGraphicsDropShadowEffect()
		self.shadow.setBlurRadius(5)
		self.addcustomerTitleText.setGraphicsEffect(self.shadow)
		self.addcustomerTitleText.setStyleSheet("font-size:20px;")



		grid = QGridLayout()
		grid.setSpacing(10)
		
		
		grid.addWidget(customerTitleLabel, 0, 0)
		grid.addWidget(self.customerTitle, 0, 1)

		grid.addWidget(customerFirstNameLabel, 1, 0)
		grid.addWidget(self.customerFirstName, 1, 1)

		grid.addWidget(customerSurnameLabel, 2, 0)
		grid.addWidget(self.customerSurname, 2, 1)

		grid.addWidget(customerCompanyLabel, 3, 0)
		grid.addWidget(self.customerCompany, 3, 1)		

		grid.addWidget(customerStreetLabel, 4, 0)
		grid.addWidget(self.customerStreet, 4, 1)

		grid.addWidget(customerTownLabel, 5, 0)
		grid.addWidget(self.customerTown, 5, 1)

		grid.addWidget(customerCountyLabel, 6, 0)
		grid.addWidget(self.customerCounty, 6, 1)

		grid.addWidget(customerPostCodeLabel, 7, 0)
		grid.addWidget(self.customerPostCode, 7, 1)

		grid.addWidget(customerMobileLabel, 8, 0)
		grid.addWidget(self.customerMobile, 8, 1)

		grid.addWidget(customerLandlineLabel, 9, 0)
		grid.addWidget(self.customerLandline, 9, 1)

		grid.addWidget(customerEmailLabel, 10, 0)
		grid.addWidget(self.customerEmail, 10, 1)

		self.gridWidget = QGroupBox("")
		self.gridWidget.setLayout(grid)
		self.gridWidget.setFixedHeight(400)

		self.verticalLayout = QVBoxLayout()
		self.verticalLayout.addWidget(self.addcustomerTitleText)
		self.verticalLayout.addStretch(1)
		self.verticalLayout.addWidget(self.gridWidget)
		#self.verticalLayout.addWidget(smallPrint)

		self.cancelButton = QPushButton("Cancel")
		self.cancelButton.setShortcut('Esc')
		self.cancelButton.setAutoDefault(False)
		self.cancelButton.setDefault(False)

		self.confirmButton = QPushButton("Confirm")
		self.confirmButton.setShortcut('Return')
		self.confirmButton.setAutoDefault(True)
		self.confirmButton.setDefault(True)

		self.hBoxL = QHBoxLayout()
		self.hBoxL.addWidget(self.cancelButton)
		self.hBoxL.addWidget(self.confirmButton)
		self.hButtonL = QWidget()
		self.hButtonL.setLayout(self.hBoxL)
		
		self.verticalLayout.addWidget(self.hButtonL)
		self.verticalLayout.addStretch(1)

		#connections
		self.customerFirstName.textChanged.connect(self.validateFirstName)
		self.customerSurname.textChanged.connect(self.validateSurname)
		self.customerCompany.textChanged.connect(self.validateCompany)
		self.customerStreet.textChanged.connect(self.validateStreet)
		self.customerTown.textChanged.connect(self.validateTown)
		self.customerPostCode.textChanged.connect(self.validatePostCode)
		self.customerEmail.textChanged.connect(self.validateEmail)
		self.customerMobile.textChanged.connect(self.validateMobile)
		self.customerLandline.textChanged.connect(self.validateUKLandline)

		self.confirmButton.clicked.connect(self.switchToPreviewWidget)

		return self.verticalLayout

	def previewNewCustomer(self):
		self.previewCustomerTitleText = QLabel("Preview New Customer")
		self.shadow = QGraphicsDropShadowEffect()
		self.shadow.setBlurRadius(5)
		self.previewCustomerTitleText.setGraphicsEffect(self.shadow)
		self.previewCustomerTitleText.setStyleSheet("font-size:20px;")

		customerTitleLabel = QLabel('Title:')
		customerFirstNameLabel = QLabel('First Name:')
		customerSurnameLabel = QLabel('Surname:')
		customerCompanyLabel = QLabel('Company:')
		customerStreetLabel = QLabel('Street:')
		customerTownLabel = QLabel('Town/City:')
		customerCountyLabel = QLabel('County:')
		customerPostCodeLabel = QLabel('Post Code:')
		customerMobileLabel = QLabel('Mobile Number:')
		customerLandlineLabel = QLabel('Landline Number:')
		customerEmailLabel = QLabel('Email:')
		self.smallerPrint = QLabel("")

		Title = self.customerTitle.currentText()
		Firstname = self.customerFirstName.text()
		Surname = self.customerSurname.text()
		Company = self.customerCompany.text()
		Street = self.customerStreet.text()
		Town = self.customerTown.text()
		County = self.customerCounty.currentText()
		PostCode = self.customerPostCode.text()
		Mobile = self.customerMobile.text()
		Landline = self.customerLandline.text()
		Email = self.customerEmail.text()


		if Title == 'Please select...':
			self.previewCustomerTitle = QLabel("")
		else:
			self.previewCustomerTitle = QLabel("{0}".format(Title))

		self.previewCustomerFirstName = QLabel('{0}'.format(Firstname))
		self.previewCustomerSurname = QLabel('{0}'.format(Surname))
		self.previewCustomerCompany = QLabel('{0}'.format(Company))
		self.previewCustomerStreet = QLabel('{0}'.format(Street))
		self.previewCustomerTown = QLabel('{0}'.format(Town))

		if County == 'Please select...':
			self.previewCustomerCounty = QLabel("")
		else:
			self.previewCustomerCounty = QLabel("{0}".format(County))

		self.previewCustomerPostCode = QLabel('{0}'.format(PostCode))
		self.previewCustomerMobile = QLabel('{0}'.format(Mobile))
		self.previewCustomerLandline = QLabel('{0}'.format(Landline))
		self.previewCustomerEmail = QLabel('{0}'.format(Email))

		grid = QGridLayout()

		grid.addWidget(customerTitleLabel, 0, 0)
		grid.addWidget(self.previewCustomerTitle, 0, 1)

		grid.addWidget(customerFirstNameLabel, 1, 0)
		grid.addWidget(self.previewCustomerFirstName, 1, 1)

		grid.addWidget(customerSurnameLabel, 2, 0)
		grid.addWidget(self.previewCustomerSurname, 2, 1)

		grid.addWidget(customerCompanyLabel, 3, 0)
		grid.addWidget(self.previewCustomerCompany, 3, 1)		

		grid.addWidget(customerStreetLabel, 4, 0)
		grid.addWidget(self.previewCustomerStreet, 4, 1)

		grid.addWidget(customerTownLabel, 5, 0)
		grid.addWidget(self.previewCustomerTown, 5, 1)

		grid.addWidget(customerCountyLabel, 6, 0)
		grid.addWidget(self.previewCustomerCounty, 6, 1)

		grid.addWidget(customerPostCodeLabel, 7, 0)
		grid.addWidget(self.previewCustomerPostCode, 7, 1)

		grid.addWidget(customerMobileLabel, 8, 0)
		grid.addWidget(self.previewCustomerMobile, 8, 1)

		grid.addWidget(customerLandlineLabel, 9, 0)
		grid.addWidget(self.previewCustomerLandline, 9, 1)

		grid.addWidget(customerEmailLabel, 10, 0)
		grid.addWidget(self.previewCustomerEmail, 10, 1)

		self.gridWidget = QGroupBox("")
		self.gridWidget.setLayout(grid)
		self.gridWidget.setFixedHeight(400)

		self.previewVerticalLayout = QVBoxLayout()
		self.previewVerticalLayout.addWidget(self.previewCustomerTitleText)
		self.previewVerticalLayout.addStretch(1)
		self.previewVerticalLayout.addWidget(self.gridWidget)

		self.editButton = QPushButton("Edit")
		self.editButton.setShortcut('Esc')
		self.editButton.setAutoDefault(False)
		self.editButton.setDefault(False)

		self.addButton = QPushButton("Add")
		self.addButton.setShortcut('Return')
		self.addButton.setAutoDefault(True)
		self.addButton.setDefault(True)

		self.hBoxL = QHBoxLayout()
		self.hBoxL.addWidget(self.editButton)
		self.hBoxL.addWidget(self.addButton)
		self.hButtonL = QWidget()
		self.hButtonL.setLayout(self.hBoxL)
		self.hButtonL.setFixedHeight(100)
		
		self.previewVerticalLayout.addWidget(self.hButtonL)
		self.previewVerticalLayout.addStretch(1)

		#connections
		self.editButton.clicked.connect(self.editEntry)
		self.addButton.clicked.connect(self.validateAddcustomerForm)

		return self.previewVerticalLayout

	def editEntry(self):
		self.rightWidget.setEnabled(False)
		self.leftWidget.setEnabled(True)

	def switchToPreviewWidget(self):
		#disable editing widget
		self.leftWidget.setEnabled(False)

		#reshresh preview widget
		if hasattr(self, 'rightWidget'):
			self.rightWidget.close()
			self.rightWidget = QWidget()
			self.mainLayout.addWidget(self.rightWidget)

		#set preview widget layout
		self.rightLayout = self.previewNewCustomer()
		self.rightWidget.setLayout(self.rightLayout)

	def clearForm(self):
		
		self.customerTitle.setCurrentIndex(0)
		self.customerFirstName.clear()
		self.customerSurname.clear()
		self.customerCompany.clear()
		self.customerStreet.clear()
		self.customerTown.clear()
		self.customerCounty.setCurrentIndex(0)
		self.customerPostCode.clear()
		self.customerMobile.clear()
		self.customerLandline.clear()
		self.customerEmail.clear()

		self.customerFirstName.setStyleSheet("background-color:#FFF;")
		self.customerSurname.setStyleSheet("background-color:#FFF;")
		self.customerCompany.setStyleSheet("background-color:#FFF;")
		self.customerStreet.setStyleSheet("background-color:#FFF;")
		self.customerTown.setStyleSheet("background-color:#FFF;")
		self.customerPostCode.setStyleSheet("background-color:#FFF;")
		self.customerMobile.setStyleSheet("background-color:#FFF;")
		self.customerLandline.setStyleSheet("background-color:#FFF;")
		self.customerEmail.setStyleSheet("background-color:#FFF;")

		if hasattr(self, 'rightWidget'):
			self.rightWidget.close()

		self.rightWidget = QWidget()
		self.rightLayout = self.previewNewCustomer()
		self.rightWidget.setLayout(self.rightLayout)
		self.rightWidget.setFixedWidth(300)
		self.rightWidget.setFixedHeight(600)

		self.mainLayout.addWidget(self.rightWidget)

		self.rightWidget.setEnabled(False)

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
		

	def addCustomerToDatabase(self):

		county = str(self.customerCounty.currentText())
		title = str(self.customerTitle.currentText())

		if self.customerCompany.text() == "":
			self.customerCompany == "-"
		else:
			self.customerCompany == self.customerCompany.text()

		values = { "Title": title,
				   "FirstName": self.customerFirstName.text(),
				  "LastName": self.customerSurname.text(),
				  "Company": self.customerCompany,
				  "Street": self.customerStreet.text(),
				  "Town": self.customerTown.text(),
				  "County": county,
				  "PostCode": self.customerPostCode.text(),
				  "Mobile": self.customerMobile.text(),
				  "Landline": self.customerLandline.text(),
				  "Email": self.customerEmail.text()}

		customerAdded = self.connection.addCustomer(values, self)

		if not customerAdded:
			self.error_message_dialog = QMessageBox()
			self.error_message_dialog.setFixedWidth(200)
			self.error_message_dialog.setWindowTitle("Input Error")
			self.error_message_dialog.setText("Error! Failed to commit to database\n"
											  "\n"
											  "Click the 'Show details' button for more information")
			self.error_message_dialog.setDetailedText("Database Error:\n \n "
											  "{0}".format(self.connection.error))
			self.error_message_dialog.setIcon(QMessageBox.Warning)
			self.okay_button = self.error_message_dialog.addButton(self.parent.tr("Okay"), QMessageBox.AcceptRole)
			self.error_message_dialog.setEscapeButton(self.okay_button)
			self.error_message_dialog.setDefaultButton(self.okay_button)
			self.okay_button.clicked.connect(self.editEntry)
			self.error_message_dialog.exec_()
			self.parent.statusBar.showMessage("Customer {0} {1} unsuccessfully added to the database".format(values["FirstName"],values["LastName"]))
			self.parent.switchToMainMenu()
		else:
			self.mssg = QMessageBox()
			self.mssg.setFixedWidth(200)
			self.mssg.setWindowTitle("Customer Added")
			self.mssg.setText("Success! Record added for {0} {1}".format(self.customerFirstName.text(), self.customerSurname.text()))
			self.mssg.setIcon(QMessageBox.Information)
			self.okay_button = self.mssg.addButton(self.parent.tr("Okay"), QMessageBox.AcceptRole)
			self.mssg.setEscapeButton(self.okay_button)
			self.mssg.setDefaultButton(self.okay_button)
			self.mssg.exec_()
			self.parent.statusBar.showMessage("Customer {0} {1} successfully added to the database".format(values["FirstName"],values["LastName"]))
			self.clearForm()
			self.parent.switchToMainMenu()
			self.editEntry()


