from PyQt4.QtGui import *
from PyQt4.QtCore import *

from date_widget import *

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
		self.leftBottomWidget = QWidget()

		self.leftTopWidget.setFixedHeight(200)
		self.leftBottomWidget.setFixedHeight(150)

		self.leftLayout = QVBoxLayout()
		self.leftLayout.addWidget(self.leftTopWidget)
		self.leftLayout.addWidget(self.leftBottomWidget)

		self.leftWidget.setLayout(self.leftLayout)

		self.leftTopLayout = self.newPatTestLayout()

		self.leftTopWidget.setLayout(self.leftTopLayout)

		self.rightWidget = QWidget()


		self.mainLayout = QHBoxLayout()
		self.mainLayout.addWidget(self.leftWidget)
		self.mainLayout.addWidget(self.rightWidget)

		self.setStyleSheet("QWidget[addCustomerClass=True]{padding:100px;}")

	def newPatTestLayout(self):
		self.newPatTestHeading = QLabel("New PAT Test Series:")
		self.newPatTestHeading.setAlignment(Qt.AlignCenter)
		self.shadow = QGraphicsDropShadowEffect()
		self.shadow.setBlurRadius(5)
		self.newPatTestHeading.setGraphicsEffect(self.shadow)
		self.newPatTestHeading.setStyleSheet("font-size:20px")

		self.date_label = QLabel("Please select a date:")
		self.selection_widget = DateWidget()

		self.addItemTestButton = QPushButton("+")
		self.addItemTestButton.setFixedWidth(30)
		self.addItemTestButton.setFixedHeight(30)

		self.selectionLayout = QHBoxLayout()
		self.selectionLayout.addWidget(self.selection_widget)
		self.selectionLayout.addWidget(self.addItemTestButton)

		self.selectionQWidget = QWidget()
		self.selectionQWidget.setLayout(self.selectionLayout)

		self.dateLayout = QVBoxLayout()
		self.dateLayout.addWidget(self.date_label)
		self.dateLayout.addWidget(self.selectionQWidget)

		self.dateWidget = QWidget()
		self.dateWidget.setLayout(self.dateLayout)

		self.verticalLayout = QVBoxLayout()
		self.verticalLayout.addWidget(self.newPatTestHeading)
		self.verticalLayout.addWidget(self.dateWidget)

		self.cancelButton = QPushButton("Cancel")
		self.confirmButton = QPushButton("Confirm")

		self.buttonsLayout = QHBoxLayout()
		self.buttonsLayout.addWidget(self.cancelButton)
		self.buttonsLayout.addWidget(self.confirmButton)


		#connections
		self.addItemTestButton.clicked.connect(self.addItemTestWidget)

		return self.verticalLayout

	def addItemTestWidget(self):
		self.tabbedLayout = QTabLayout()

		

	def previewPatTestLayout(self):
		self.leftWidget.setEnabled(False)
		
		self.heading = QLabel("Preview PAT Tests")
		self.heading.setStyleSheet("font-size:20px")