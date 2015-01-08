from PyQt4.QtGui import *
from PyQt4.QtCore import *

class PlasterersMenuWidget(QWidget):
    """ This class creates a widget that displays the menu for the plasterers section
    of the application """


    def __init__(self):

        super().__init__()

        self.layout = self.createPlasterersMenuLayout()
        self.setLayout(self.layout)

        

    def createPlasterersMenuLayout(self):

        self.setStyleSheet("""QPushButton[buttonClass=home] {
                           font-size: 16px; background-color: rgba(188, 188, 188, 50);
                           border: 1px solid rgba(188, 188, 188, 250);
                           height:100px;
                           border-radius:5px;}""")

        self.addPlastererPushButton = QPushButton("Add Plasterer")
        self.addPlastererPushButton.setProperty("buttonClass","home")
        self.addPlastererPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        
        self.managePlasterersPushButton = QPushButton("Manage Plasterers")
        self.managePlasterersPushButton.setProperty("buttonClass","home")
        self.managePlasterersPushButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.backButton = QPushButton("Back")

        self.mainLayout = QHBoxLayout()

        self.mainLayout.addWidget(self.addPlastererPushButton)
        self.mainLayout.addWidget(self.managePlasterersPushButton)

        self.tempWidget = QWidget()
        self.tempWidget.setLayout(self.mainLayout)

        
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.addWidget(self.tempWidget)
        self.verticalLayout.addWidget(self.backButton)

        

        return self.verticalLayout
