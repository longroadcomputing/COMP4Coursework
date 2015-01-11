from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys
import time

class newLoanWidget(QWidget):
	"""docstring for newLoanWidget"""
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

		self.leftTopLayout = self.newLoanLayout()

		self.leftTopWidget.setLayout(self.leftTopLayout)

		self.rightWidget = QWidget()


		self.mainLayout = QHBoxLayout()
		self.mainLayout.addWidget(self.leftWidget)
		self.mainLayout.addWidget(self.rightWidget)

		self.setStyleSheet("QWidget[addCustomerClass=True]{padding:100px;}")

	def newLoanLayout(self):
		self.newLoanHeading = QLabel("New PAT Loan Series:")
		self.newLoanHeading.setAlignment(Qt.AlignCenter)
		self.shadow = QGraphicsDropShadowEffect()
		self.shadow.setBlurRadius(5)
		self.newLoanHeading.setGraphicsEffect(self.shadow)
		self.newLoanHeading.setStyleSheet("font-size:20px")

		