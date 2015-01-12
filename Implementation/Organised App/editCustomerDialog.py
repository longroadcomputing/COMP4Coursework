from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys

class editCustomerDialog(QDialog):
	"""docstring for editCustomerDialog"""
	def __init__(self, parent):
		super().__init__()
		
		self.parent = parent

		self.connection = None

	def layout(self):
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

		self.addcustomerTitleText.setAlignment(Qt.AlignCenter)
		self.addcustomerTitleText.setFixedHeight(30)
		self.shadow = QGraphicsDropShadowEffect()
		self.shadow.setBlurRadius(5)
		self.addcustomerTitleText.setGraphicsEffect(self.shadow)
		self.addcustomerTitleText.setStyleSheet("font-size:20px;")

		
		
		self.grid.addWidget(customerTitleLabel, 0, 0)
		self.grid.addWidget(self.customerTitle, 0, 1)

		self.grid.addWidget(customerFirstNameLabel, 1, 0)
		self.grid.addWidget(self.customerFirstName, 1, 1)

		self.grid.addWidget(customerSurnameLabel, 2, 0)
		self.grid.addWidget(self.customerSurname, 2, 1)

		self.grid.addWidget(customerCompanyLabel, 3, 0)
		self.grid.addWidget(self.customerCompany, 3, 1)		

		self.grid.addWidget(customerStreetLabel, 4, 0)
		self.grid.addWidget(self.customerStreet, 4, 1)

		self.grid.addWidget(customerTownLabel, 5, 0)
		self.grid.addWidget(self.customerTown, 5, 1)

		self.grid.addWidget(customerCountyLabel, 6, 0)
		self.grid.addWidget(self.customerCounty, 6, 1)

		self.grid.addWidget(customerPostCodeLabel, 7, 0)
		self.grid.addWidget(self.customerPostCode, 7, 1)

		self.grid.addWidget(customerMobileLabel, 8, 0)
		self.grid.addWidget(self.customerMobile, 8, 1)

		self.grid.addWidget(customerLandlineLabel, 9, 0)
		self.grid.addWidget(self.customerLandline, 9, 1)

		self.grid.addWidget(customerEmailLabel, 10, 0)
		self.grid.addWidget(self.customerEmail, 10, 1)

		self.newL = QVBoxLayout()

		self.newL.addWidget(self.editCustomerGroupBox)

		self.userInfoEdit = QWidget()
		self.userInfoEdit.setLayout(self.newL)

		

		return self.userInfoEdit