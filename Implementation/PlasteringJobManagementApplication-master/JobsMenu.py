from PyQt4.QtGui import *
from PyQt4.QtCore import *

class JobsMenuWidget(QWidget):
    """ This class creates a widget that displays the menu for the client section
    of the application """


    def __init__(self):

        super().__init__()


        self.layout = self.createJobsMenuLayout()
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

    def createJobsMenuLayout(self):

        

        self.addJobPushButton = QPushButton("Add Job")
        self.addJobPushButton.setProperty("buttonClass","home")
        self.addJobPushButton.setCursor(QCursor(Qt.PointingHandCursor))
        
        self.manageJobsPushButton = QPushButton("Manage Jobs")
        self.manageJobsPushButton.setProperty("buttonClass","home")
        self.manageJobsPushButton.setCursor(QCursor(Qt.PointingHandCursor))


        self.backButton = QPushButton("Back")


        self.jobsMenuLayout = QHBoxLayout()

        self.jobsMenuLayout.addWidget(self.addJobPushButton)
        self.jobsMenuLayout.addWidget(self.manageJobsPushButton)
        self.jobsMenuLayout.addWidget(self.backButton)

        self.tempWidget = QWidget()
        self.tempWidget.setLayout(self.jobsMenuLayout)

        
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.addWidget(self.tempWidget)
        self.verticalLayout.addWidget(self.backButton)




        return self.verticalLayout
