from PyQt4.QtGui import *
from PyQt4.QtCore import *

class ClientsMenuWidget(QWidget):
	""" This class creates a widget that displays the menu for the client section
	of the application """


	def __init__(self):

		super().__init__()


		self.layout = self.createClientsMenuLayout()
		self.setLayout(self.layout)
##        self.setAutoFillBackground(True)
##        p = self.palette()
##        p.setColor(self.backgroundRole(), Qt.white)
##        self.setPalette(p)
		self.setStyleSheet("QWidget{background-image: url(./clients.jpg);background-size:100%;}")

		self.setStyleSheet("""QPushButton[buttonClass=home] {
						   font-size: 16px; background-color: rgba(188, 188, 188, 50);
						   border: 1px solid rgba(188, 188, 188, 250);
						   height:100px;
						   border-radius:5px;}""")

	def createClientsMenuLayout(self):

		

		self.addClientPushButton = QPushButton("Add Client")
		self.addClientPushButton.setProperty("buttonClass","home")
		self.addClientPushButton.setCursor(QCursor(Qt.PointingHandCursor))
		
		self.manageClientsPushButton = QPushButton("Manage Clients")
		self.manageClientsPushButton.setProperty("buttonClass","home")
		self.manageClientsPushButton.setCursor(QCursor(Qt.PointingHandCursor))


		self.backButton = QPushButton("Back")


		self.clientsMenuLayout = QHBoxLayout()

		self.clientsMenuLayout.addWidget(self.addClientPushButton)
		self.clientsMenuLayout.addWidget(self.manageClientsPushButton)
		self.clientsMenuLayout.addWidget(self.backButton)

		self.tempWidget = QWidget()
		self.tempWidget.setLayout(self.clientsMenuLayout)

		
		self.verticalLayout = QVBoxLayout()
		self.verticalLayout.addWidget(self.tempWidget)
		self.verticalLayout.addWidget(self.backButton)




		return self.verticalLayout
