try:
	from PyQt4.QtCore import *
	from PyQt4.QtGui import *
	from PyQt4.QtSql import *
except:
	from PyQt5.QtCore import *
	from PyQt5.QtGui import *
	from PyQt5.QtSql import *


class DisplayWidget(QWidget):

	def __init__(self):
		super().__init__()
		self.stacked_layout = QStackedLayout()
		self.model = None
		self.results_table = QTableView()
		self.results_layout = QVBoxLayout()
		self.results_widget = QWidget()
		self.display_results_layout()

	def display_results_layout(self):
		self.results_layout.addWidget(self.results_table)
		self.setLayout(self.results_layout)

	def show_results(self,query):
		if not self.model or not isinstance(self.model, "QSqlQueryModel"):
			self.model = QSqlQueryModel()
		self.model.setQuery(query)
		self.results_table.setModel(self.model)
		self.results_table.show()
