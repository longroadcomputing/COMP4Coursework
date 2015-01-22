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

                self.results_table = None

                self.display = None

                self.currentRow = None

                self.model = QSqlQueryModel()


                self.mainLayout = QHBoxLayout()
                
                self.leftWidget = QWidget()
                self.leftWidget.setFixedWidth(300)

                self.leftTopWidget = QWidget()
                self.leftBottomWidget = QTabWidget()

                self.leftLayout = QVBoxLayout()
                self.leftLayout.addWidget(self.leftTopWidget)
                self.leftLayout.addWidget(self.leftBottomWidget)

                self.leftWidget.setLayout(self.leftLayout)

                self.leftTopLayout = self.newLoanLayout()
                self.leftTopWidget.setLayout(self.leftTopLayout)

                self.leftBottomLayout = self.loanItemTableView()

                self.rightWidget = QWidget()
                self.rightWidget.setFixedWidth(300)

                self.rightLayout = self.searchItem()
                self.rightWidget.setLayout(self.rightLayout)

                self.mainLayout.addWidget(self.leftWidget)
                self.mainLayout.addWidget(self.rightWidget)

                self.setStyleSheet("QWidget[addCustomerClass=True]{padding:100px;}")

        def addConnection(self, connection):
                self.connection = connection
                self.connections()
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

        def clearForm(self):
                self.customerDropDown.setCurrentIndex(0)
                self.LoanLengthSpinBox.setValue(1)
                date = QDate.currentDate()
                self.datePopup.setDate(date)

                self.selectionWidget.setEnabled(True)
                self.gridWidget.setEnabled(True)
                self.createLoanButton.setEnabled(True)

##                self.addItemButton.setEnabled(False)
                self.confirmButton.setEnabled(False)
                self.rightWidget.setEnabled(False)

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

                        self.rightWidget.setEnabled(True)
                        self.confirmButton.setEnabled(True)
                        self.confirmButton.setShortcut('Return')
                else:
                        messg = "Please select a customer from the list"
                        QMessageBox.warning(self, "Loan Not Created!", messg)

        def searchItem(self):
                if hasattr(self, 'rightWidget'):
                        self.rightWidget.close()
                        self.rightWidget = QWidget()

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

                self.addItemButton = QPushButton("+")
                self.addItemButton.setFixedWidth(30)
                self.addItemButton.setFixedHeight(30)

                self.addItemButton.setEnabled(False)

                self.buttonsLayout = QHBoxLayout()
                self.buttonsLayout.addWidget(self.showAllItemsButton)
                self.buttonsLayout.addWidget(self.addItemButton)
                self.buttonsLayout.setAlignment(self.addItemButton, Qt.AlignRight)

                self.buttonsWidget = QWidget()
                self.buttonsWidget.setLayout(self.buttonsLayout)

                self.viewItemsLayout = QVBoxLayout()
                self.viewItemsLayout.addWidget(self.buttonsWidget)
                self.viewItemsLayout.addWidget(self.results_table)
                
                self.tableGroup.setLayout(self.viewItemsLayout)

                self.groupL = QVBoxLayout()
                self.groupL.addWidget(self.tableGroup)

                self.groupWidget = QWidget()
                self.groupWidget.setLayout(self.groupL)

                self.vBoxLayout = QVBoxLayout()
                self.vBoxLayout.addWidget(self.searchWidget)
                self.vBoxLayout.addWidget(self.groupWidget)

                return self.vBoxLayout

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
                                self.data = self.connection.getItemDataForLoan(ID)

                                self.searchItemsGroup.setEnabled(False)
                                self.showAllItemsButton.setEnabled(False)
                                self.results_table.setEnabled(False)

                                self.addItemButton.setEnabled(True)
                                self.addItemButton.setAutoDefault(True)
                                self.addItemButton.setDefault(True)
                                self.addItemButton.setShortcut('Return')
                     
                                self.addItemButton.clicked.connect(self.addLoanItem)
                                
        def searchDatabase(self):
                queryText = self.searchField.text()

                query = self.connection.getItemSearchQuery(queryText)

                self.showResults(query)

        def showAllItemsInTable(self):
                self.searchField.clear()

                query = self.connection.getAllItemsForLoan()

                self.showResults(query)

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
                self.parent.mainMenu.newLoanButton.clicked.connect(self.showAllItemsInTable)
                self.parent.add_loan.triggered.connect(self.showAllItemsInTable)

        def populateDropDowns(self):

                self.dropDownModel = QSqlRelationalTableModel(self)
                self.dropDownModel.setTable("Loan")
                self.dropDownModel.setRelation(1,
                                               QSqlRelation("Customer","CustomerID","FistName"))
                self.dropDownModel.setSort(2, Qt.AscendingOrder)
                self.dropDownModel.select()

                self.mapper = QDataWidgetMapper(self)
                self.mapper.setSubmitPolicy(QDataWidgetMapper.ManualSubmit)
                self.mapper.setModel(self.dropDownModel)
                self.mapper.setItemDelegate(QSqlRelationalDelegate(self))
                self.mapper.addMapping(self.datePopup, 2)
                self.mapper.addMapping(self.LoanLengthSpinBox, 3)

                relationModel = self.dropDownModel.relationModel(1)
                self.customerDropDown.setModel(relationModel)
                self.customerDropDown.setModelColumn(
                        relationModel.fieldIndex("FirstName"))
                self.mapper.addMapping(self.customerDropDown, 1)
                self.mapper.toFirst()

                
                
        def loanItemTableView(self):

                self.loanItemTable = QTableView()

                self.layout = QHBoxLayout()
                self.layout.addWidget(self.loanItemTable)

                return self.layout

        def addLoanItem(self):
                pass
