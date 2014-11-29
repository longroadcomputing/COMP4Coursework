from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys

class CalendarDialog(QDialog):
    """A calendar dialog window for selecting the date of loans and PAT tests"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Select Date")
        self.message = QLabel("Please select the date the loan started")
        
        self.calendar_widget = QCalendarWidget()
        self.calendar_widget.setGridVisible(True)
        self.calendar_widget.setSelectionMode(1)
        self.calendar_widget.setMinimumDate(QDate(2000, 1, 1))
        self.calendar_widget.setMaximumDate(QDate(2020, 12, 30))
        
        self.select_button = QPushButton("Select")
        self.cancel_button = QPushButton("Cancel")

        self.loan_calendar_layout = QVBoxLayout()
        self.buttons_layout = QHBoxLayout()

        self.loan_calendar_layout.addWidget(self.message)
        self.loan_calendar_layout.addWidget(self.calendar_widget)

        self.buttons_layout.addWidget(self.cancel_button)
        self.buttons_layout.addWidget(self.select_button)

        self.buttons_widget = QWidget()
        self.buttons_widget.setLayout(self.buttons_layout)
        self.loan_calendar_layout.addWidget(self.buttons_widget)

        self.setLayout(self.loan_calendar_layout)

        self.select_button.clicked.connect(self.select_date)
        self.cancel_button.clicked.connect(self.close)

        self.cancel_button.setAutoDefault(False)
        self.select_button.setAutoDefault(True)
        self.select_button.focusInEvent(QFocusEvent(8))

        self.cancel_button.setShortcut("Ctrl+W")

    def select_date(self):
        self.date = self.calendar_widget.selectedDate(activated)
        print(self.date)
        self.close()



if __name__ == "__main__":
    application = QApplication(sys.argv)
    calendar = CalendarDialog()
    calendar.show()
    calendar.raise_()
    application.exec_()
