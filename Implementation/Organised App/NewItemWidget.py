from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys
import re

from SQLConnection import *

class NewItemWidget(QWidget):
	""" This is the enter new item widget """
	def __init__(self, parent):

		super().__init__()

		self.setProperty("newItemClass", "True")

		self.connection = None

		self.parent = parent

		self.errors = []

		self.mainLayout = QHBoxLayout()
		self.mainLayout.setAlignment(Qt.AlignHCenter)

		self.leftWidget = QWidget()

		self.leftWidget.setFixedWidth(300)
		self.leftWidget.setFixedHeight(600)

		self.leftLayout = self.newItemLayout()


		self.leftWidget.setLayout(self.leftLayout)

		self.mainLayout.addWidget(self.leftWidget)

		self.setStyleSheet("QWidget[newItemClass=True]{padding:100px;}")

	def addConnection(self, connection):
		self.connection = connection
		return True


	def newItemLayout(self):

		#create widgets
		self.heading = QLabel("Add New Item")
		self.heading.setAlignment(Qt.AlignCenter)
		self.shadow = QGraphicsDropShadowEffect()
		self.shadow.setBlurRadius(5)
		self.heading.setGraphicsEffect(self.shadow)
		self.heading.setStyleSheet("font-size:20px")

		self.item_name_label = QLabel("Item Name:*")
		self.item_value_label = QLabel("Item Value:*")
		self.item_loan_rate_label = QLabel("Loan Rate:")

		self.item_class_label = QLabel("Item Class:*")
		self.fuse_rating_label = QLabel("Fuse Rating:*")
		self.item_type_label = QLabel("Item Type:*")
		self.location_label = QLabel("Location:*")

		self.smallPrint = QLabel("* required fields")
		self.smallPrint.setStyleSheet("font-size:11px")

		self.item_name_line_edit = QLineEdit()
		self.item_value_line_edit = QLineEdit()
		self.item_loan_rate_line_edit = QLineEdit()
		self.item_class_drop_down = QComboBox()



		#dropdown menus (combobox)'s
		#==========================#

		self.item_class_drop_down.addItem("Please select...")

		#self.item_class_drop_down.addItem(item_class)
		self.item_class_drop_down.addItem("1")
		self.item_class_drop_down.addItem("2")

		j = self.item_class_drop_down.model().index(0,0)
		self.item_class_drop_down.model().setData(j, 0, Qt.UserRole-1)




		self.fuse_rating_drop_down = QComboBox()
		self.fuse_rating_drop_down.addItem("Please select...")

		# self.fuse_rating_drop_down.addItem(fuse_rating)
		self.fuse_rating_drop_down.addItem("-")
		self.fuse_rating_drop_down.addItem("0")
		self.fuse_rating_drop_down.addItem("3")
		self.fuse_rating_drop_down.addItem("5")
		self.fuse_rating_drop_down.addItem("7")
		self.fuse_rating_drop_down.addItem("10")
		self.fuse_rating_drop_down.addItem("13")

		j = self.fuse_rating_drop_down.model().index(0,0)
		self.fuse_rating_drop_down.model().setData(j, 0, Qt.UserRole-1)




		self.item_type_drop_down = QComboBox()

		self.item_type_drop_down.addItem("Please select...")
		
		# self.item_type_drop_down.addItem(item_type)
		self.item_type_drop_down.addItem("Audio")
		self.item_type_drop_down.addItem("Cabling")
		self.item_type_drop_down.addItem("Control Desks")
		self.item_type_drop_down.addItem("Lighting")
		self.item_type_drop_down.addItem("Miscallaneous")
		self.item_type_drop_down.addItem("Power")
		self.item_type_drop_down.addItem("Software")
		self.item_type_drop_down.addItem("Staging")
		self.item_type_drop_down.addItem("Storage/Hardware")
		self.item_type_drop_down.addItem("Visual")

		j = self.item_type_drop_down.model().index(0,0)
		self.item_type_drop_down.model().setData(j, 0, Qt.UserRole-1)




		self.location_drop_down = QComboBox()

		self.location_drop_down.addItem("Please select...")

		# self.location_drop_down.addItem[location]

		self.location_drop_down.addItem("Alpha Terrace")
		self.location_drop_down.addItem("C3 Centre")
		self.location_drop_down.addItem("Cineworld")
		self.location_drop_down.addItem("St. Bedes")

		j = self.location_drop_down.model().index(0,0)
		self.location_drop_down.model().setData(j, 0, Qt.UserRole-1)


		self.cancelButton = QPushButton("Cancel")
		self.confirmButton = QPushButton("Confirm")

		grid = QGridLayout()
		grid.setSpacing(10)

		grid.addWidget(self.item_name_label,0,0)
		grid.addWidget(self.item_name_line_edit,0,1)

		grid.addWidget(self.item_value_label,1,0)
		grid.addWidget(self.item_value_line_edit,1,1)

		grid.addWidget(self.item_loan_rate_label,2,0)
		grid.addWidget(self.item_loan_rate_line_edit,2,1)

		grid.addWidget(self.item_class_label,3,0)
		grid.addWidget(self.item_class_drop_down,3,1)

		grid.addWidget(self.fuse_rating_label,4,0)
		grid.addWidget(self.fuse_rating_drop_down,4,1)

		grid.addWidget(self.item_type_label,5,0)
		grid.addWidget(self.item_type_drop_down,5,1)

		grid.addWidget(self.location_label,6,0)
		grid.addWidget(self.location_drop_down,6,1)

		self.gridWidget = QGroupBox('Add Item:')
		self.gridWidget.setLayout(grid)
		self.gridWidget.setFixedHeight(400)

		self.quantityGroup = QGroupBox("Duplicate Items:")

		self.quantityLabel = QLabel("Quantity")
		self.quantitySpinBox = QSpinBox()
		self.quantitySpinBox.setRange(1,50)
		self.quantitySpinBox.setValue(1)


		self.quantityLayout = QHBoxLayout()
		self.quantityLayout.addWidget(self.quantityLabel)
		self.quantityLayout.addWidget(self.quantitySpinBox)

		self.quantityGroup.setLayout(self.quantityLayout)


		self.verticalLayout = QVBoxLayout()
		self.verticalLayout.addWidget(self.heading)
		self.verticalLayout.addStretch(1)
		self.verticalLayout.addWidget(self.gridWidget)
		self.verticalLayout.addWidget(self.quantityGroup)
		self.verticalLayout.addWidget(self.smallPrint)

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
		self.item_name_line_edit.textChanged.connect(self.validateItemName)
		self.item_value_line_edit.textChanged.connect(self.validateItemValue)
		self.item_loan_rate_line_edit.textChanged.connect(self.validateLoanRate)

		self.confirmButton.clicked.connect(self.switchToPreviewWidget)

		self.clearForm()

		return self.verticalLayout



	def previewLayout(self):
		#create widgets
		self.heading = QLabel("Preview New Item")
		self.heading.setAlignment(Qt.AlignCenter)
		self.shadow = QGraphicsDropShadowEffect()
		self.shadow.setBlurRadius(5)
		self.heading.setGraphicsEffect(self.shadow)
		self.heading.setStyleSheet("font-size:20px")

		self.item_name_preview_label = QLabel("Item Name:")
		self.item_value_preview_label = QLabel("Item Value:")
		self.item_loan_rate_preview_label = QLabel("Loan Rate:")
		self.item_class_preview_label = QLabel("Item Class:")
		self.fuse_rating_preview_label = QLabel("Fuse Rating:")
		self.item_type_preview_label = QLabel("Item Type:")
		self.location_preview_label = QLabel("Item Location:")
		self.smallerPrint = QLabel("")

		self.item_name_preview = QLabel("{0}".format(self.item_name_line_edit.text()))
		self.item_value_preview = QLabel("{0}".format(self.item_value_line_edit.text()))
		self.item_loan_rate_preview = QLabel("{0}".format(self.item_loan_rate_line_edit.text()))

		self.item_class = self.item_class_drop_down.currentText()
		self.fuse_rating = self.fuse_rating_drop_down.currentText()
		self.item_type = self.item_type_drop_down.currentText()
		self.location = self.location_drop_down.currentText()

		if self.item_class == 'Please select...':
			self.item_class_preview = QLabel("")
		else:
			self.item_class_preview = QLabel("{0}".format(self.item_class))

		if self.fuse_rating == 'Please select...':
			self.fuse_rating_preview = QLabel("")
		else:
			self.fuse_rating_preview = QLabel("{0}".format(self.fuse_rating))

		if self.item_type == 'Please select...':
			self.item_type_preview = QLabel("")
		else:
			self.item_type_preview = QLabel("{0}".format(self.item_type))

		if self.location == 'Please select...':
			self.location_preview = QLabel("")
		else:
			self.location_preview = QLabel("{0}".format(self.location))

		grid = QGridLayout()

		grid.addWidget(self.item_name_preview_label,0,0)
		grid.addWidget(self.item_name_preview,0,1)

		grid.addWidget(self.item_value_preview_label,1,0)
		grid.addWidget(self.item_value_preview,1,1)

		grid.addWidget(self.item_loan_rate_preview_label,2,0)
		grid.addWidget(self.item_loan_rate_preview,2,1)

		grid.addWidget(self.item_class_preview_label,3,0)
		grid.addWidget(self.item_class_preview,3,1)

		grid.addWidget(self.fuse_rating_preview_label,4,0)
		grid.addWidget(self.fuse_rating_preview,4,1)

		grid.addWidget(self.item_type_preview_label,5,0)
		grid.addWidget(self.item_type_preview,5,1)

		grid.addWidget(self.location_preview_label,6,0)
		grid.addWidget(self.location_preview,6,1)

		self.gridWidget = QGroupBox('Preview:')
		self.gridWidget.setLayout(grid)
		self.gridWidget.setFixedHeight(400)

		self.previewVerticalLayout = QVBoxLayout()
		self.previewVerticalLayout.addWidget(self.heading)
		self.previewVerticalLayout.addStretch(1)
		self.previewVerticalLayout.addWidget(self.gridWidget)
		self.previewVerticalLayout.addWidget(self.smallerPrint)

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

		self.previewVerticalLayout.addWidget(self.hButtonL)
		self.previewVerticalLayout.addStretch(1)

		self.editButton.clicked.connect(self.editEntry)
		self.addButton.clicked.connect(self.validateNewItemForm)

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
			self.rightWidget.setFixedWidth(300)
			self.rightWidget.setFixedHeight(600)

		#set preview widget layout
		self.rightLayout = self.previewLayout()
		self.rightWidget.setLayout(self.rightLayout)


	def clearForm(self):
		self.item_name_line_edit.clear()
		self.item_value_line_edit.clear()
		self.item_loan_rate_line_edit.clear()
		self.item_class_drop_down.setCurrentIndex(0)
		self.fuse_rating_drop_down.setCurrentIndex(0)
		self.item_type_drop_down.setCurrentIndex(0)
		self.location_drop_down.setCurrentIndex(0)

		self.item_name_line_edit.setStyleSheet("background-color:#FFF;")
		self.item_value_line_edit.setStyleSheet("background-color:#FFF;")
		self.item_loan_rate_line_edit.setStyleSheet("background-color:#FFF;")

		self.item_name_preview = QLabel("")
		self.item_value_preview = QLabel("")
		self.item_loan_rate_preview = QLabel("")
		self.item_class_preview = QLabel("")
		self.fuse_rating_preview = QLabel("")
		self.item_type_preview = QLabel("")
		self.location_preview = QLabel("")

		if hasattr(self, 'rightWidget'):
			self.rightWidget.close()
		self.rightWidget = QWidget()
		self.rightLayout = self.previewLayout()
		self.rightWidget.setLayout(self.rightLayout)
		self.rightWidget.setFixedWidth(300)
		self.rightWidget.setFixedHeight(600)

		self.mainLayout.addWidget(self.rightWidget)

		self.rightWidget.setEnabled(False)


	def validateItemName(self):
		item_name = self.item_name_line_edit.text()
		length = len(item_name)
		if length >= 2:
			self.item_name_line_edit.setStyleSheet("background-color:#c4df9b")
			return True
		else:
			self.item_name_line_edit.setStyleSheet("background-color:#f6989d ")
			return False

	def validateItemValue(self):
		item_value = self.item_value_line_edit.text()
		length = len(item_value)
		try:
			item_value = int(item_value)
			if item_value:
				valid_item_value = True
		except ValueError:
			valid_item_value = False

		if valid_item_value == True:
			self.item_value_line_edit.setStyleSheet("background-color:#c4df9b")
			return True
		else:
			self.item_value_line_edit.setStyleSheet("background-color:#f6989d ")
			return False

	def validateLoanRate(self):
		text = self.item_loan_rate_line_edit.text()
		length = len(text)
		valid_loan_rate = False
		try:
			loan_rate = int(text)
			if loan_rate:
				valid_loan_rate = True
		except ValueError:
			valid_loan_rate = False

		if text == "" or text == '-':
			valid_loan_rate = True

		if valid_loan_rate == True or text == '':
			self.item_loan_rate_line_edit.setStyleSheet("background-color:#c4df9b")
			return True
		else:
			self.item_loan_rate_line_edit.setStyleSheet("background-color:#f6989d ")
			return False


	def validateItemValue(self):
		item_value = self.item_value_line_edit.text()
		length = len(item_value)
		if length >= 2:
			self.item_value_line_edit.setStyleSheet("background-color:#c4df9b")
			return True
		else:
			self.item_value_line_edit.setStyleSheet("background-color:#f6989d ")
			return False

	def validateDropDowns(self):
		valid_dropdowns = False
		if self.item_type_preview == "" or self.location_preview == "" or self.item_class_preview == "" or self.fuse_rating_preview == "":
			valid_dropdowns = False
		else:
			valid_dropdowns = True


	def validateNewItemForm(self):
		valid_dropdowns = self.validateDropDowns()
		valid_name = self.validateItemName()
		valid_value = self.validateItemValue()
		valid_loan_rate = self.validateLoanRate()

		if valid_dropdowns == False or valid_name == False or valid_value == False or valid_loan_rate == False:
			self.error_message_dialog = QMessageBox()
			self.error_message_dialog.setFixedWidth(200)
			self.error_message_dialog.setWindowTitle("Input Error")
			self.error_message_dialog.setText("Error! Some data entered is invalid \n"
											  "\n"
											  "Click the 'Show details' button for more information")
			self.error_message_dialog.setDetailedText("The information entered is invalid \n"
													"Steps to take: \n"
													"\n"
													"    1. Make sure that only an integer is entered \n"
													"       for the Item Value field. \n"
													"    2. The drop-down menus should NOT have \n"
													"       'Please select...' as an option for data input. \n")
			self.error_message_dialog.setIcon(QMessageBox.Warning)
			self.okay_button = self.error_message_dialog.addButton(self.tr("Okay"), QMessageBox.AcceptRole)
			self.error_message_dialog.setEscapeButton(self.okay_button)
			self.error_message_dialog.setDefaultButton(self.okay_button)
			self.okay_button.clicked.connect(self.editEntry)
			self.error_message_dialog.exec_()

		else:
			self.addNewItemToDatabase()

	def addNewItemToDatabase(self):

		if self.item_type_preview.text() == "Please select...":
			item_type_id = ''
		if self.location_preview.text() == "Please select...":
			location_id = ''

		if self.item_type_preview.text() == "Cabling":
			item_type_id = '2'
		elif self.item_type_preview.text() == "Storage/Hardware":
			item_type_id = '3'
		elif self.item_type_preview.text() == "Lighting":
			item_type_id = '4'
		elif self.item_type_preview.text() == "Power":
			item_type_id = '5'
		elif self.item_type_preview.text() == "Audio":
			item_type_id = '6'
		elif self.item_type_preview.text() == "Visual":
			item_type_id = '7'
		elif self.item_type_preview.text() == "Miscellaneous":
			item_type_id = '8'
		elif self.item_type_preview.text() == "Software":
			item_type_id = '9'
		elif self.item_type_preview.text() == "Staging":
			item_type_id = '10'
		elif self.item_type_preview.text() == "Control Desks":
			item_type_id = '11'


		if self.location_preview.text() == "St. Bedes":
			location_id = '2'
		elif self.location_preview.text() == "Alpha Terrace":
			location_id = '3'
		elif self.location_preview.text() == "Cineworld":
			location_id = '4'
		elif self.location_preview.text() == "C3 Centre":
			location_id = '5'

		if self.item_loan_rate_preview.text() == "":
			self.loan_rate_entry = "-"
		else:
			self.loan_rate_entry = self.item_loan_rate_preview.text()

		values = {"ItemName":self.item_name_preview.text(),
					  "ItemValue":self.item_value_preview.text(),
					  "LoanRate":self.loan_rate_entry,
					  "ItemClass":self.item_class_preview.text(),
					  "FuseRating":self.fuse_rating_preview.text(),
					  "ItemTypeID":item_type_id,
					  "LocationID":location_id}

		quantity = self.quantitySpinBox.value()

		for each in range(quantity):
			success = self.connection.addItem(values,self)

		if not success:
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
		else:
			self.mssg = QMessageBox()
			self.mssg.setFixedWidth(200)
			self.mssg.setWindowTitle("Customer Added")
			self.mssg.setText("Success! {0} Record(s) added for {1}".format(quantity, self.item_name_preview.text()))
			self.mssg.setIcon(QMessageBox.Information)
			self.okay_button = self.mssg.addButton(self.parent.tr("Okay"), QMessageBox.AcceptRole)
			self.mssg.setEscapeButton(self.okay_button)
			self.mssg.setDefaultButton(self.okay_button)
			self.mssg.exec_()
			self.parent.statusBar.showMessage("Item {0} unsuccessfully added to the database".format(values["ItemName"]))
			self.clearForm()
			self.parent.switchToMainMenu()









