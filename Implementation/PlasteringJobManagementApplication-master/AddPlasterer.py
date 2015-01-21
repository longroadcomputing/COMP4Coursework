from PyQt4.QtCore import  *
from PyQt4.QtGui import *
from SQLConnection import *

import re

class AddPlastererWidget(QWidget):

	""" This is the add plasterer widget """

	def __init__(self, parent):

		super().__init__()
		
		self.setProperty("addPlastererClass","True")
		
		self.connection = None

		self.parent = parent
		
		self.mainLayout = self.layout()
		
		self.setLayout(self.mainLayout)

		self.setStyleSheet("QWidget[addplastererClass=True]{padding:100px;}")

	def addConnection(self, connection):
		self.connection = connection
		return True
	
	def validateFirstName(self):

		text = self.plastererFirstName.text()
		length = len(text)

		if length > 2:
			self.plastererFirstName.setStyleSheet("background-color:#c4df9b;")
			return True
		else:
			self.plastererFirstName.setStyleSheet("background-color:#f6989d;")
			return False

	def validateSurname(self):

		text = self.plastererSurname.text()
		length = len(text)

		if length > 2:
			self.plastererSurname.setStyleSheet("background-color:#c4df9b;")
			return True
		else:
			self.plastererSurname.setStyleSheet("background-color:#f6989d;")
			return False

	def validateStreet(self):

		text = self.plastererStreet.text()
		length = len(text)

		if length > 5:
			self.plastererStreet.setStyleSheet("background-color:#c4df9b;")
			return True
		else:
			self.plastererStreet.setStyleSheet("background-color:#f6989d;")
			return False


	def validateTown(self):
		
		text = self.plastererTown.text()
		length = len(text)

		if length > 3:
			self.plastererTown.setStyleSheet("background-color:#c4df9b;")
			return True
		else:
			self.plastererTown.setStyleSheet("background-color:#f6989d;")
			return False


	def validatePostCode(self):
		
		text = self.plastererPostCode.text()

		postCodeRegEx = re.compile("[A-Z]{1,2}[0-9][0-9A-Z]?\s?[0-9][A-Z]{2}")

		match = postCodeRegEx.match(text.upper())

		if match:
			self.plastererPostCode.setStyleSheet("background-color:#c4df9b;")
			return True
		else:
			self.plastererPostCode.setStyleSheet("background-color:#f6989d;")
			return False


	def validatePhoneNumber(self):
		text = self.plastererPhoneNumber.text()
		length = len(text)

		if length >= 11:
			self.plastererPhoneNumber.setStyleSheet("background-color:#c4df9b;")
			return True
		else:
			self.plastererPhoneNumber.setStyleSheet("background-color:#f6989d;")
			return False

	def validateEmail(self):
		text = self.plastererEmail.text()

		emailRegEx = re.compile("^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$")

		match = emailRegEx.match(text)

		if match:
			self.plastererEmail.setStyleSheet("background-color:#c4df9b;")
			return True
		else:
			self.plastererEmail.setStyleSheet("background-color:#f6989d;")
			return False

	def validateDailyRate(self):
		
		text = self.plastererDailyRate.text()

		dailyRateRegEx = re.compile("[0-9]+\.[0-9]+")

		match = dailyRateRegEx.match(text.upper())

		if match:
			self.plastererDailyRate.setStyleSheet("background-color:#c4df9b;")
			return True
		else:
			self.plastererDailyRate.setStyleSheet("background-color:#f6989d;")
			return False

	def clearForm(self):
		
		self.plastererTitle.setCurrentIndex(0)
		self.plastererFirstName.clear()
		self.plastererSurname.clear()
		self.plastererStreet.clear()
		self.plastererTown.clear()
		self.plastererCounty.setCurrentIndex(0)
		self.plastererPostCode.clear()
		self.plastererPhoneNumber.clear()
		self.plastererEmail.clear()
		self.plastererDailyRate.clear()

		self.plastererFirstName.setStyleSheet("background-color:#FFF;")
		self.plastererSurname.setStyleSheet("background-color:#FFF;")
		self.plastererStreet.setStyleSheet("background-color:#FFF;")
		self.plastererTown.setStyleSheet("background-color:#FFF;")
		self.plastererPostCode.setStyleSheet("background-color:#FFF;")
		self.plastererPhoneNumber.setStyleSheet("background-color:#FFF;")
		self.plastererEmail.setStyleSheet("background-color:#FFF;")
		self.plastererDailyRate.setStyleSheet("background-color:#FFF;")

		self.errorTextContentLabel.setText("None")

	def addPlastererToDatabase(self):
		
		county = str(self.plastererCounty.currentText())
		title = str(self.plastererTitle.currentText())
		
		values = { "Title": title,
				   "FirstName": self.plastererFirstName.text(),
				  "Surname": self.plastererSurname.text(),
				  "Street": self.plastererStreet.text(),
				  "Town": self.plastererTown.text(),
				  "County": county,
				  "PostCode": self.plastererPostCode.text(),
				  "Email": self.plastererEmail.text(),
				   "PhoneNumber": self.plastererPhoneNumber.text(),
				   "DailyRate": self.plastererDailyRate.text()}

		plastererAdded = self.connection.addPlasterer(values)

		if plastererAdded:
			self.clearForm()
			self.parent.switchToPlasterersMenu()
			infoText = """ The New Plasterer has been added to the database!"""
			QMessageBox.information(self, "Plasterer Added", infoText)
			
		else:
			infoText = """ The New Plasterer was not added successfully! """
			QMessageBox.critical(self, "Plasterer Not Added", infoText)  


	def validateAddPlastererForm(self):

		self.checkFirstName = self.validateFirstName()
		self.checkSurname = self.validateSurname()
		self.checkStreet = self.validateStreet()
		self.checkTown = self.validateTown()
		self.checkPostCode = self.validatePostCode()
		self.checkPhoneNumber = self.validatePhoneNumber()
		self.checkEmail = self.validateEmail()
		self.checkDailyRate = self.validateDailyRate()

		self.errorMsg = ""

		if self.checkFirstName == False:
			self.errorMsg += "Invalid First Name, "
		if self.checkSurname == False:
			self.errorMsg += "Invalid Surname, "
		if self.checkStreet == False:
			self.errorMsg += "Invalid Street, "
		if self.checkTown == False:
			self.errorMsg += "Invalid Town, "
		if self.checkPostCode == False:
			self.errorMsg += "Invalid Post Code Format, "
		if self.checkPhoneNumber == False:
			self.errorMsg += "Invalid Phone Number Format, "
		if self.checkEmail == False:
			self.errorMsg += "Invalid Email Format, "
		if self.checkDailyRate == False:
			self.errorMsg += "Invalid Daily Rate, "
		

		self.errorTextContentLabel.setText(self.errorMsg)

		if self.errorMsg == "":
			self.addPlastererToDatabase()
			return True
		else:
			return False

	

	def layout(self):

		self.counties = ['Aberdeenshire', 'Angus', 'Argyll and Bute', 'Ayrshire', 'Ayrshire and Arran',
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

		self.plastererTitleLabel = QLabel('Title')
		self.plastererFirstNameLabel = QLabel('First Name')
		self.plastererSurnameLabel = QLabel('Surname')
		self.plastererStreetLabel = QLabel('Street')
		self.plastererTownLabel = QLabel('Town/City')
		self.plastererCountyLabel = QLabel('County')
		self.plastererPostCodeLabel = QLabel('Post Code')
		self.plastererPhoneNumberLabel = QLabel('Phone Number')
		self.plastererEmailLabel = QLabel('Email')
		self.plastererDailyRateLabel = QLabel("Daily Rate")

		self.plastererTitle = QComboBox()
		self.titles = ["Mr","Mrs","Ms","Sir"]
		self.plastererTitle.addItems(self.titles)

		self.plastererFirstName = QLineEdit()
		self.plastererSurname = QLineEdit()
		self.plastererStreet = QLineEdit()
		self.plastererTown = QLineEdit()
		self.plastererCounty = QComboBox()
		self.plastererCounty.addItems(self.counties)
		self.plastererPostCode = QLineEdit()
		self.plastererPhoneNumber = QLineEdit()
		self.plastererEmail = QLineEdit()
		self.plastererDailyRate = QLineEdit()

		self.cancelFormButton = QPushButton("Cancel")
		self.addPlastererFormButton = QPushButton("Add plasterer")

		self.errorTextLabel = QLabel("Errors:")
		self.errorTextContentLabel = QLabel("None")
		self.errorTextContentLabel.setStyleSheet("color: red;")


		self.addPlastererTitleText = QLabel("Add a Plasterer")
		self.shadow = QGraphicsDropShadowEffect()
		self.shadow.setBlurRadius(5)
		self.addPlastererTitleText.setStyleSheet("font-size:20px;")
		self.addPlastererTitleText.setGraphicsEffect(self.shadow)



		grid = QGridLayout()
		grid.setSpacing(10)
		
		grid.addWidget(self.errorTextLabel,0,0)
		grid.addWidget(self.errorTextContentLabel,0,1)
		
		grid.addWidget(self.plastererTitleLabel, 1, 0)
		grid.addWidget(self.plastererTitle, 1, 1)

		grid.addWidget(self.plastererFirstNameLabel, 2, 0)
		grid.addWidget(self.plastererFirstName, 2, 1)

		grid.addWidget(self.plastererSurnameLabel, 3, 0)
		grid.addWidget(self.plastererSurname, 3, 1)

		grid.addWidget(self.plastererStreetLabel, 4, 0)
		grid.addWidget(self.plastererStreet, 4, 1)

		grid.addWidget(self.plastererTownLabel, 5, 0)
		grid.addWidget(self.plastererTown, 5, 1)

		grid.addWidget(self.plastererCountyLabel, 6, 0)
		grid.addWidget(self.plastererCounty, 6, 1)

		grid.addWidget(self.plastererPostCodeLabel, 7, 0)
		grid.addWidget(self.plastererPostCode, 7, 1)

		grid.addWidget(self.plastererPhoneNumberLabel, 8, 0)
		grid.addWidget(self.plastererPhoneNumber, 8, 1)

		grid.addWidget(self.plastererEmailLabel, 9, 0)
		grid.addWidget(self.plastererEmail, 9, 1)

		grid.addWidget(self.plastererDailyRateLabel, 10, 0)
		grid.addWidget(self.plastererDailyRate, 10, 1)

		self.gridWidget = QWidget()
		self.gridWidget.setLayout(grid)

		self.verticalLayout = QVBoxLayout()
		self.verticalLayout.addWidget(self.addPlastererTitleText)
		self.verticalLayout.addStretch(1)
		self.verticalLayout.addWidget(self.gridWidget)

		self.hBoxL = QHBoxLayout()
		self.hBoxL.addWidget(self.cancelFormButton)
		self.hBoxL.addWidget(self.addPlastererFormButton)
		self.hButtonL = QWidget()
		self.hButtonL.setLayout(self.hBoxL)
		
		self.verticalLayout.addWidget(self.hButtonL)
		self.verticalLayout.addStretch(1)

		#connections
		self.plastererFirstName.textChanged.connect(self.validateFirstName)
		self.plastererSurname.textChanged.connect(self.validateSurname)
		self.plastererStreet.textChanged.connect(self.validateStreet)
		self.plastererTown.textChanged.connect(self.validateTown)
		self.plastererPostCode.textChanged.connect(self.validatePostCode)
		self.plastererEmail.textChanged.connect(self.validateEmail)
		self.plastererPhoneNumber.textChanged.connect(self.validatePhoneNumber)
		self.plastererDailyRate.textChanged.connect(self.validateDailyRate)
		self.addPlastererFormButton.clicked.connect(self.validateAddPlastererForm)





		return self.verticalLayout





