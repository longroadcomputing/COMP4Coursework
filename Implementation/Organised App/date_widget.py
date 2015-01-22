from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys

class DateWidget(QDateEdit):
	"""docstring for DateWidget"""
	def __init__(self, parent=None):
		super(DateWidget, self).__init__()
		self.parent = parent

		self.setDate(QDate.currentDate())
		self.setCalendarPopup(True)
		self.setDisplayFormat('dd/MM/yyyy')
		self.cal = self.calendarWidget()
		#self.cal.SingleSelection()
		self.cal.setFirstDayOfWeek(Qt.Monday)
		self.cal.setHorizontalHeaderFormat(QCalendarWidget.SingleLetterDayNames)
		self.cal.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
		self.cal.setGridVisible(True)

