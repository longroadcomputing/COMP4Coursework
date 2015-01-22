from PyQt4.QtGui import *
from PyQt4.QtCore import *

from date_widget import *
from selectItemDialog import *

import sys
import time

class newPatTestWidget(QWidget):
	"""docstring for newPatTestWidget"""
	def __init__(self, parent):
		super().__init__()

		self.setProperty("addCustomerClass","True")

		self.connection = None

		self.parent = parent
		
		self.leftWidget = QWidget()

		self.leftTopWidget = QWidget()
		self.leftBottomWidget = QTabWidget()

		self.leftTopWidget.setFixedHeight(200)
		self.leftBottomWidget.setFixedHeight(200)

		self.leftLayout = QVBoxLayout()
		self.leftLayout.addWidget(self.leftTopWidget)
		self.leftLayout.addWidget(self.leftBottomWidget)

		self.leftWidget.setLayout(self.leftLayout)

		self.leftTopLayout = self.newPatTestLayout()

		self.leftTopWidget.setLayout(self.leftTopLayout)

		self.rightWidget = QWidget()
		self.rightWidget.setFixedWidth(300)
		self.rightWidget.setFixedHeight(600)


		self.mainLayout = QHBoxLayout()
		self.mainLayout.addWidget(self.leftWidget)
		self.mainLayout.addWidget(self.rightWidget)

		self.setStyleSheet("QWidget[addCustomerClass=True]{padding:100px;}")

	def newPatTestLayout(self):
		self.newPatTestHeading = QLabel("New PAT Test Series")
		self.newPatTestHeading.setAlignment(Qt.AlignCenter)
		self.shadow = QGraphicsDropShadowEffect()
		self.shadow.setBlurRadius(5)
		self.newPatTestHeading.setGraphicsEffect(self.shadow)
		self.newPatTestHeading.setStyleSheet("font-size:20px")

		self.date_label = QLabel("Please select a date:")

		self.datePopup = DateWidget()
		self.addItemTestButton = QPushButton("+")
		self.addItemTestButton.setFixedWidth(30)
		self.addItemTestButton.setFixedHeight(30)

		self.selectionLayout = QHBoxLayout()
		self.selectionLayout.addWidget(self.datePopup)
		self.selectionLayout.addWidget(self.addItemTestButton)

		self.selectionWidget = QWidget()
		self.selectionWidget.setLayout(self.selectionLayout)


		self.verticalLayout = QVBoxLayout()
		self.verticalLayout.addWidget(self.newPatTestHeading)
		self.verticalLayout.addWidget(self.date_label)
		self.verticalLayout.addWidget(self.selectionWidget)

		self.cancelButton = QPushButton("Cancel")
		self.cancelButton.setShortcut('Esc')
		self.cancelButton.setAutoDefault(False)
		self.cancelButton.setDefault(False)
		
		self.confirmButton = QPushButton("Confirm")
		self.confirmButton.setShortcut('Return')
		self.confirmButton.setAutoDefault(True)
		self.confirmButton.setDefault(True)

		self.buttonsLayout = QHBoxLayout()
		self.buttonsLayout.addWidget(self.cancelButton)
		self.buttonsLayout.addWidget(self.confirmButton)

		self.buttonsWidget = QWidget()
		self.buttonsWidget.setLayout(self.buttonsLayout)

		self.leftLayout.addWidget(self.buttonsWidget)


		#connections
		self.cancelButton.clicked.connect(self.parent.switchToMainMenu)
		self.addItemTestButton.clicked.connect(self.selectItem)

		return self.verticalLayout

	def selectItem(self):
		self.selectItemDialog = selectItemDialog()

		
