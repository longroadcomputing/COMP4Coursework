from PyQt4.QtCore import  *
from PyQt4.QtGui import *
from PyQt4.QtSql import *


from SQLConnection import *

import re

class ManagePlasterersWidget(QWidget):

    """ This is the add plasterer widget """

    def __init__(self, parent):

        super().__init__()
        
        self.connection = None

        self.parent = parent

        self.results_table = None

        self.display = False

        self.currentRow = None

        self.model = QSqlQueryModel()
        
        self.setStyleSheet("QWidget[addplastererClass=True]{padding:100px;}")

        self.mainLayout = self.layout()
        
        self.setLayout(self.mainLayout)

        self.currentMemberId = None

        


    def layout(self):

        self.searchPlasterersGroup = QGroupBox("Search Plasterers")

        self.showAllPlasterersPushButton = QPushButton("Show All Plasterers")

        self.showAllPlasterersPushButton.setMaximumWidth(100)

        self.searchPlasterersLayout = QHBoxLayout()

        self.searchField = QLineEdit()
        self.searchPushButton = QPushButton("Search")

        self.searchPlasterersLayout.addWidget(self.searchField)
        self.searchPlasterersLayout.addWidget(self.searchPushButton)

        self.searchPlasterersGroup.setLayout(self.searchPlasterersLayout)

        self.searchL = QVBoxLayout()
        self.searchL.addWidget(self.searchPlasterersGroup)

        self.searchWidget = QWidget()
        self.searchWidget.setLayout(self.searchL)

        
        self.tableGroup = QGroupBox("Plasterers")
        
        self.results_table = QTableView()

        header = QHeaderView(Qt.Horizontal, self.results_table)
        header.setStretchLastSection(True)

        #self.results_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        #set selection behaviour to select entire row at a time
        self.results_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        

        self.newL = QVBoxLayout()
        self.newL.addWidget(self.results_table)
        self.newL.addWidget(self.showAllPlasterersPushButton)

        self.tableGroup.setLayout(self.newL)

        self.groupL = QVBoxLayout()
        self.groupL.addWidget(self.tableGroup)

        self.groupWidget = QWidget()
        self.groupWidget.setLayout(self.groupL)

        self.editPlastererWidget = self.editPlasterer()

        self.vBoxLayout = QVBoxLayout()
        self.vBoxLayout.addWidget(self.searchWidget)
        self.vBoxLayout.addWidget(self.groupWidget)
        self.vBoxLayout.addWidget(self.editPlastererWidget)

        return self.vBoxLayout

    def editPlasterer(self):

        self.editPlastererGroupBox = QGroupBox("Edit Plasterer Info")
        self.editPlastererGroupBox.setEnabled(False)
        self.grid = QGridLayout()
        self.grid.setSpacing(10)

        self.errorTextLabel = QLabel("Errors: ")
        self.errorTextContentLabel = QLabel()

        self.firstNameEditLabel = QLabel("First Name")
        self.surnameEditLabel = QLabel("Surname")
        self.streetEditLabel = QLabel("Street")
        self.townEditLabel = QLabel("Town/City")
        self.countyEditLabel = QLabel("County")
        self.postCodeEditLabel = QLabel("Post Code")
        self.emailEditLabel = QLabel("Email")
        self.phoneNumberEditLabel = QLabel("Phone Number")

        self.firstNameEdit = QLineEdit()
        self.surnameEdit = QLineEdit()
        self.streetEdit = QLineEdit()
        self.townEdit = QLineEdit()
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



        
        self.countyEdit = QComboBox()
        self.countyEdit.addItems(self.counties)

        self.titleLabel = QLabel("Title")

        self.titleEdit = QComboBox()
        self.titles = ["Mr","Mrs","Ms","Sir"]
        self.titleEdit.addItems(self.titles)

        
        self.postCodeEdit = QLineEdit()
        self.emailEdit = QLineEdit()
        self.phoneNumberEdit = QLineEdit()

        self.savePushButton = QPushButton("Save Info")
        self.cancelPushButton = QPushButton("Cancel Edit")


        self.grid.addWidget(self.titleLabel, 0,0)
        self.grid.addWidget(self.titleEdit, 0, 1)
        
        self.grid.addWidget(self.firstNameEditLabel, 1, 0)
        self.grid.addWidget(self.firstNameEdit, 1, 1)

        self.grid.addWidget(self.surnameEditLabel, 2, 0)
        self.grid.addWidget(self.surnameEdit, 2, 1)

        self.grid.addWidget(self.streetEditLabel, 3, 0)
        self.grid.addWidget(self.streetEdit, 3, 1)

        self.grid.addWidget(self.townEditLabel, 4, 0)
        self.grid.addWidget(self.townEdit, 4, 1)

        self.grid.addWidget(self.countyEditLabel, 5, 0)
        self.grid.addWidget(self.countyEdit, 5, 1)

        self.grid.addWidget(self.postCodeEditLabel, 6, 0)
        self.grid.addWidget(self.postCodeEdit, 6, 1)

        self.grid.addWidget(self.emailEditLabel, 7, 0)
        self.grid.addWidget(self.emailEdit, 7, 1)

        self.grid.addWidget(self.phoneNumberEditLabel, 8, 0)
        self.grid.addWidget(self.phoneNumberEdit, 8, 1)

        self.grid.addWidget(self.errorTextLabel, 9,0)
        self.grid.addWidget(self.errorTextContentLabel, 9, 1)
        
        self.grid.addWidget(self.cancelPushButton, 10, 0)
        self.grid.addWidget(self.savePushButton, 10, 1)

        self.editPlastererGroupBox.setLayout(self.grid)

        self.newL = QVBoxLayout()

        self.newL.addWidget(self.editPlastererGroupBox)

        self.userInfoEdit = QWidget()
        self.userInfoEdit.setLayout(self.newL)

        

        return self.userInfoEdit

    def searchDatabase(self):

        queryText = self.searchField.text()

        query = self.connection.getSearchQuery(queryText)

        #print(queryText)

        self.showResults(query)
        
    def showAllPlasterersInTable(self):
        
        print("Showing Plasterers")

        query = self.connection.getAllPlasterers()

        self.showResults(query)

        
    def addConnection(self, connection):
        
        self.connection = connection

        self.connections()
        
        return True

    def editingPlasterer(self):
        
        self.searchPlasterersGroup.setEnabled(False)
        self.tableGroup.setEnabled(False)

        self.editPlastererGroupBox.setEnabled(True)


    def searchingPlasterers(self):
        #clear edit form
        self.firstNameEdit.clear()
        self.surnameEdit.clear()
        self.streetEdit.clear()
        self.townEdit.clear()
        self.postCodeEdit.clear()
        self.emailEdit.clear()
        self.phoneNumberEdit.clear()

        self.firstNameEdit.setStyleSheet("")
        self.surnameEdit.setStyleSheet("")
        self.streetEdit.setStyleSheet("")
        self.townEdit.setStyleSheet("")
        self.countyEdit.setStyleSheet("")
        self.postCodeEdit.setStyleSheet("")
        self.emailEdit.setStyleSheet("")
        self.phoneNumberEdit.setStyleSheet("")


        self.results_table.selectionModel().clearSelection()
        
        self.searchPlasterersGroup.setEnabled(True)
        self.tableGroup.setEnabled(True)
        
        self.editPlastererGroupBox.setEnabled(False)

        
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
                data = self.connection.getPlastererData(cliID)


                self.searchPlasterersGroup.setEnabled(False)
                self.tableGroup.setEnabled(False)
                self.editPlastererGroupBox.setEnabled(True)

                self.editPlastererPopulate(data)




                            
    def editPlastererPopulate(self, data):

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
        self.showAllPlasterersPushButton.clicked.connect(self.showAllPlasterersInTable)
        #self.results_table.selectionModel().selectionChanged.connect(self.changeFormFields)


        
        self.firstNameEdit.textChanged.connect(self.validateFirstName)
        self.surnameEdit.textChanged.connect(self.validateSurname)
        self.streetEdit.textChanged.connect(self.validateStreet)
        self.townEdit.textChanged.connect(self.validateTown)
        self.postCodeEdit.textChanged.connect(self.validatePostCode)
        self.emailEdit.textChanged.connect(self.validateEmail)
        self.phoneNumberEdit.textChanged.connect(self.validatePhoneNumber)
        self.savePushButton.clicked.connect(self.validateForm)
        self.cancelPushButton.clicked.connect(self.searchingPlasterers)


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

        plastererAdded = self.connection.updatePlasterer(values)

        if plastererAdded:

            self.searchingPlasterers()
             
            infoText = """ The plasterers information has been updated!"""
            QMessageBox.information(self, "Plasterer Info Updated!", infoText)
            
        else:
            infoText = """ The plasterer was not updated successfully! """

            QMessageBox.critical(self, "Plasterer Not Updated!", infoText)
        

    def validateForm(self):

        self.checkFirstName = self.validateFirstName()
        self.checkSurname = self.validateSurname()
        self.checkStreet = self.validateStreet()
        self.checkTown = self.validateTown()
        self.checkPostCode = self.validatePostCode()
        self.checkPhoneNumber = self.validatePhoneNumber()
        self.checkEmail = self.validateEmail()

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
        

        self.errorTextContentLabel.setText(self.errorMsg)
        

        if self.errorMsg == "":
            self.addUpdatedDataToDb()
            return True
        else:
            return False

    def validateFirstName(self):

        text = self.firstNameEdit.text()
        length = len(text)

        if length > 2:
            self.firstNameEdit.setStyleSheet("background-color:#c4df9b;")
            return True
        else:
            self.firstNameEdit.setStyleSheet("background-color:#f6989d;")
            return False

    def validateSurname(self):

        text = self.surnameEdit.text()
        length = len(text)

        if length > 2:
            self.surnameEdit.setStyleSheet("background-color:#c4df9b;")
            return True
        else:
            self.surnameEdit.setStyleSheet("background-color:#f6989d;")
            return False

    def validateStreet(self):

        text = self.streetEdit.text()
        length = len(text)

        if length > 5:
            self.streetEdit.setStyleSheet("background-color:#c4df9b;")
            return True
        else:
            self.streetEdit.setStyleSheet("background-color:#f6989d;")
            return False


    def validateTown(self):
        
        text = self.townEdit.text()
        length = len(text)

        if length > 3:
            self.townEdit.setStyleSheet("background-color:#c4df9b;")
            return True
        else:
            self.townEdit.setStyleSheet("background-color:#f6989d;")
            return False


    def validatePostCode(self):
        
        text = self.postCodeEdit.text()

        postCodeRegEx = re.compile("[A-Z]{1,2}[0-9][0-9A-Z]?\s?[0-9][A-Z]{2}")

        match = postCodeRegEx.match(text.upper())

        if match:
            self.postCodeEdit.setStyleSheet("background-color:#c4df9b;")
            return True
        else:
            self.postCodeEdit.setStyleSheet("background-color:#f6989d;")
            return False


    def validatePhoneNumber(self):
        text = self.phoneNumberEdit.text()
        length = len(text)

        if length == 11:
            self.phoneNumberEdit.setStyleSheet("background-color:#c4df9b;")
            return True
        else:
            self.phoneNumberEdit.setStyleSheet("background-color:#f6989d;")
            return False

    def validateEmail(self):
        text = self.emailEdit.text()

        emailRegEx = re.compile("^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$")

        match = emailRegEx.match(text)

        if match:
            self.emailEdit.setStyleSheet("background-color:#c4df9b;")
            return True
        else:
            self.emailEdit.setStyleSheet("background-color:#f6989d;")
            return False
        





