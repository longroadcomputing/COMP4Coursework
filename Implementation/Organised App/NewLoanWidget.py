from PyQt4.QtGui import *
from PyQt4.QtCore import *

from date_widget import *
from selectItemDialog import *

import sys
import time

import sqlite3

class newLoanWidget(QWidget):
        """docstring for newLoanWidget"""
        def __init__(self, parent):
                super().__init__()

                self.setProperty("addCustomerClass","True")

                self.connection = None

                self.parent = parent

                self.model = QSqlTableModel()
                
                self.leftWidget = QWidget()
                self.leftWidget.setFixedWidth(300)

                self.leftTopWidget = QWidget()
                self.leftBottomWidget = QTabWidget()

                #self.leftTopWidget.setFixedHeight(200)
                #self.leftBottomWidget.setFixedHeight(200)

                self.leftLayout = QVBoxLayout()
                self.leftLayout.addWidget(self.leftTopWidget)
                self.leftLayout.addWidget(self.leftBottomWidget)

                self.leftWidget.setLayout(self.leftLayout)

                self.leftTopLayout = self.newLoanLayout()
                self.leftTopWidget.setLayout(self.leftTopLayout)

                self.leftBottomLayout = self.loanItemTableView()

                self.rightWidget = QWidget()
                self.rightWidget.setFixedWidth(300)
                self.rightWidget.setFixedHeight(600)


                self.mainLayout = QHBoxLayout()
                self.mainLayout.addWidget(self.leftWidget)
                self.mainLayout.addWidget(self.rightWidget)

                self.setStyleSheet("QWidget[addCustomerClass=True]{padding:100px;}")

        def addConnection(self, connection):
                self.connection = connection
                return True

        def newLoanLayout(self):
                self.newLoanHeading = QLabel("New Loan")
                self.newLoanHeading.setAlignment(Qt.AlignCenter)
                self.shadow = QGraphicsDropShadowEffect()
                self.shadow.setBlurRadius(5)
                self.newLoanHeading.setGraphicsEffect(self.shadow)
                self.newLoanHeading.setStyleSheet("font-size:20px")

                self.date_label = QLabel("Date Started:")

                self.datePopup = DateWidget()

                self.selectionLayout = QHBoxLayout()
                self.selectionLayout.addWidget(self.date_label)
                self.selectionLayout.addWidget(self.datePopup)

                self.selectionWidget = QWidget()
                self.selectionWidget.setLayout(self.selectionLayout)

                self.customerLabel = QLabel("Customer:*")

                self.customerDropDown = QComboBox()

                self.customerDropDown.addItem("Please select...")
                

                j = self.customerDropDown.model().index(0,0)
                self.customerDropDown.model().setData(j, 0, Qt.UserRole-1)

                self.parent.mainMenu.newLoanButton.clicked.connect(self.populateDropDowns)

                self.LoanLengthLabel = QLabel("Loan Length:*")

                self.LoanLengthSpinBox = QSpinBox()
                self.LoanLengthSpinBox.setRange(1,7)
                self.LoanLengthSpinBox.setSuffix(" Days")

                self.spacerWidget = QWidget()
                self.spacerWidget.setFixedHeight(10)

                self.ItemDropDown = QComboBox()
                self.ItemDropDown.addItem("Please select...")

                j = self.customerDropDown.model().index(0,0)
                self.customerDropDown.model().setData(j, 0, Qt.UserRole-1)

                self.loanRateLabel = QLabel("Loan Rate:*")

                self.createLoanButton = QPushButton("Create Loan")
                self.createLoanButton.setAutoDefault(True)
                self.createLoanButton.setDefault(True)
                self.createLoanButton.setShortcut('Return')

                self.addItemButton = QPushButton("+")
                self.addItemButton.setFixedWidth(30)
                self.addItemButton.setFixedHeight(30)

                self.addItemButton.setEnabled(False)

                #Uncomment the lines below to add the above button to its separate layout and widget
                # self.newItemButtonLayout = QHBoxLayout()
                # self.newItemButtonLayout.addWidget(self.addItemButton)

                # self.newItemButtonWidget = QWidget()
                # self.newItemButtonWidget.setLayout(self.newItemButtonLayout)

                grid = QGridLayout()
                grid.setSpacing(10)

                grid.addWidget(self.customerLabel,0,0)
                grid.addWidget(self.customerDropDown,0,1)



                grid.addWidget(self.LoanLengthLabel,1,0)
                grid.addWidget(self.LoanLengthSpinBox,1,1)



                self.gridWidget = QWidget()
                self.gridWidget.setLayout(grid)

                self.verticalLayout = QVBoxLayout()
                self.verticalLayout.addWidget(self.newLoanHeading)
                self.verticalLayout.addWidget(self.selectionWidget)
                self.verticalLayout.addWidget(self.gridWidget)
                self.verticalLayout.addWidget(self.createLoanButton)
                self.verticalLayout.setAlignment(self.createLoanButton, Qt.AlignRight)
                self.verticalLayout.addWidget(self.addItemButton)
                self.verticalLayout.setAlignment(self.addItemButton, Qt.AlignRight)

                self.cancelButton = QPushButton("Cancel")
                self.cancelButton.setShortcut('Esc')
                self.cancelButton.setAutoDefault(False)
                self.cancelButton.setDefault(False)

                self.confirmButton = QPushButton("Confirm")
                self.confirmButton.setShortcut('Return')
                self.confirmButton.setAutoDefault(True)
                self.confirmButton.setDefault(True)
                self.confirmButton.setEnabled(False)

                self.buttonsLayout = QHBoxLayout()
                self.buttonsLayout.addWidget(self.cancelButton)
                self.buttonsLayout.addWidget(self.confirmButton)

                self.buttonsWidget = QWidget()
                self.buttonsWidget.setLayout(self.buttonsLayout)

                self.leftLayout.addWidget(self.buttonsWidget)

                #connections
                self.cancelButton.clicked.connect(self.parent.switchToMainMenu)

                self.createLoanButton.clicked.connect(self.addLoan)

                return self.verticalLayout

        def validateCustomer(self):
                if self.customerDropDown.currentText() == "Please select...":
                        return False
                else:
                        return True

        def addLoan(self):
                validCustomer = self.validateCustomer()
                if validCustomer == True:
                        self.customer = self.customerDropDown.currentText()
                        self.customer = "{0}".format(self.customer)
                        print(self.customer)
#                        for customer in self.customers:
#                               if self.customer == customer
                        
                        selectedDate = self.datePopup.cal.selectedDate()
                        day = selectedDate.day()
                        month = selectedDate.month()
                        year = selectedDate.year()
        
                        date = "{0}/{1}/{2}".format(day, month, year)

                        loanLength = self.LoanLengthSpinBox.value()
                        loanLength = self.LoanLengthSpinBox.textFromValue(loanLength)

                        print(date)
                        print(loanLength)

                        data = {
                                "Date":date,
                                "LoanLength":loanLength,}

                        print(data)
                        self.newLoan = self.connection.addLoan(data)

                
                        self.selectionWidget.setEnabled(False)
                        self.gridWidget.setEnabled(False)
                        self.createLoanButton.setEnabled(False)

                        self.addItemButton.setEnabled(True)
                        self.confirmButton.setEnabled(True)
                        self.confirmButton.setShortcut('Return')
                        self.addItemButton.clicked.connect(self.selectItem)

        def selectItem(self):
                self.newLoanItemSelectionDialog = SelectItemDialog(self)
                self.newLoanItemSelectionDialog.addConnection(self.connection)
                self.newLoanItemSelectionDialog.showAllItemsInTable()
                self.newLoanItemSelectionDialog.exec_()


        def populateDropDowns(self):
                with sqlite3.connect(self.connection.path) as db:
                        cursor = db.cursor()
                        sql = ("""SELECT CustomerID, Title, FirstName, LastName, Company, FROM Customer ORDER BY FirstName ASC""")
                        cursor.execute(sql)
                        self.customers = cursor.fetchall()

                        for customer in self.customers:
                                self.customerDropDown.addItem("{0} {1} {2} ({3})".format(customer[1], customer[2], customer[3], customer[4]))

        def loanItemTableView(self):

                self.loanItemTable = QTableView()

                self.layout = QHBoxLayout()
                self.layout.addWidget(self.loanItemTable)

                return self.layout

        def addToLoan(self, data):
                print(data)


