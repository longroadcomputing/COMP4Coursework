from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys
import re

class editCustomerDialog(QDialog):
		"""docstring for editCustomerDialog"""
		def __init__(self, parent):
				super().__init__()

				self.parent = parent

				self.connection = None

				self.mainLayout = self.layout()

				self.setLayout(self.mainLayout)

		def layout(self):
				self.parent.mainLayout.setEnabled(False)
				self.editCustomerGroupBox = QGroupBox("Edit Customer Info")
				self.editCustomerGroupBox.setEnabled(False)
				self.grid = QGridLayout()
				self.grid.setSpacing(10)

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
				self.verticalLayout.addWidget(smallPrint)

				self.cancelButton = QPushButton("Exit")
				self.cancelButton.setShortcut('Esc')
				self.cancelButton.setAutoDefault(False)
				self.cancelButton.setDefault(False)

				self.confirmButton = QPushButton("Update")
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

				return self.verticalLayout

		def connections(self):
			self.customerFirstName.textChanged.connect(self.validateFirstName)
			self.customerSurname.textChanged.connect(self.validateSurname)
			self.customerCompany.textChanged.connect(self.validateCompany)
			self.customerStreet.textChanged.connect(self.validateStreet)
			self.customerTown.textChanged.connect(self.validateTown)
			self.customerPostCode.textChanged.connect(self.validatePostCode)
			self.customerMobile.textChanged.connect(self.validateMobile)
			self.customerLandline.textChanged.connect(self.validateUKLandline)
			self.customerEmail.textChanged.connect(self.validateEmail)

			self.cancelButton.clicked.connect(self.close)
			self.confirmButton.clicked.connect(self.validateUpdatecustomerForm)
				

		def addConnection(self, connection):
				self.connection = connection

				self.connections()
				return True

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

				self.customerFirstName.setStyleSheet('')
				self.customerSurname.setStyleSheet('')
				self.customerCompany.setStyleSheet('')
				self.customerStreet.setStyleSheet('')
				self.customerTown.setStyleSheet('')
				self.customerPostCode.setStyleSheet('')
				self.customerMobile.setStyleSheet('')
				self.customerLandline.setStyleSheet('')
				self.customerEmail.setStyleSheet('')


		def populateEditFields(self, data):
				currentId = data[0]
				title = data[1]
				firstname = data[2]
				surname = data[3]
				company = data[4]
				street = data[5]
				town = data[6]
				county = data[7]
				postCode = data[8]
				mobile = data[9]
				landline = data[10]
				email = data[11]

				self.currentMemberId = currentId
				self.customerTitle.findText(title)
				self.customerFirstName.setText(firstname)
				self.customerSurname.setText(surname)
				self.customerCompany.setText(company)
				self.customerStreet.setText(street)
				self.customerTown.setText(town)
				self.customerCounty.findText(county)
				self.customerPostCode.setText(postCode)
				self.customerMobile.setText(mobile)
				self.customerLandline.setText(landline)
				self.customerEmail.setText(email)

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

		def validateUpdatecustomerForm(self):

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
						self.updateCustomer()

		def updateCustomer(self):
				county = str(self.countyEdit.currentText())
				title = str(self.titleEdit.currentText())

				values = {"ID" : self.currentMemberId,
										"Title": title,
								   "FirstName": self.firstNameEdit.text(),
								  "Surname": self.surnameEdit.text(),
								  "Company":self.companyEdit.text(),
								  "Street": self.streetEdit.text(),
								  "Town": self.townEdit.text(),
								  "County": county,
								  "PostCode": self.postCodeEdit.text(),
								  "Mobile": self.mobile.text(),
								  "Landline": self.landline.text(),
										"Email": emailEdit.text()}

				clientAdded = self.connection.updateCustomer(values)

				if clientAdded:

						self.searchingCustomers()
						 
						infoText = """ The clients information has been updated!"""
						QMessageBox.information(self, "Customer Info Updated!", infoText)
						
				else:
						infoText = """ The client was not updated successfully! """

						QMessageBox.critical(self, "Customer Not Updated!", infoText)

				
				
