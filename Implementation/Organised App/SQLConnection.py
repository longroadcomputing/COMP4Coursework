from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *


import sys
import sqlite3
import pdb

class SQLConnection():

	def __init__(self,path):
		self.path = path
		self.db = None

	def open_database(self):
		if self.db:
			self.close_database()
			
		#pdb.set_trace()
		self.db = QSqlDatabase.addDatabase("QSQLITE")
		self.db.setDatabaseName(self.path )
		opened_ok = self.db.open()
		return opened_ok

	def close_database(self):

		if self.db:
			if self.db.isOpen() == True:
				self.db.close()
				#remove the database from the QSqlDatabase object - "conn" is the default
				#database name
				QSqlDatabase.removeDatabase("conn")
				closed = self.db.open()
				self.db = None
				return True
			else:
				return False
		else:
			return False

	def closeEvent(self,event):
		"""closes the database if a close event occures -
		   such as close window/quit application"""
		self.close_database()

	def getPassword(self):
		query = QSqlQuery(self.db)

		query.prepare(""" SELECT Password from Password""")
		query.exec_()

		query.next()

		password = query.value(0)

		#print(password)

		return password

	def addItem(self, values, parent):
		self.parent = parent
		add_item = QSqlQuery(self.db)

		add_item.prepare("""INSERT INTO Item(ItemName,ItemValue,LoanRate,
		ItemClass,FuseRating,ItemTypeID,LocationID) VALUES(:ItemName,:ItemValue,
		:LoanRate,:ItemClass,:FuseRating,:ItemTypeID,:LocationID)""")

		add_item.bindValue(":ItemName",values["ItemName"])
		add_item.bindValue(":ItemValue",values["ItemValue"])
		add_item.bindValue(":LoanRate",values["LoanRate"])
		add_item.bindValue(":ItemClass",values["ItemClass"])
		add_item.bindValue(":FuseRating",values["FuseRating"])
		add_item.bindValue(":ItemTypeID",values["ItemTypeID"])
		add_item.bindValue(":LocationID",values["LocationID"])

		success = add_item.exec_()

		self.error = add_item.lastError().text()

		if success:
			return True
		else:
			return False


	def getAllItemTypes(self):
		query = QSqlQuery(self.db)

		query.prepare("SELECT ItemType FROM ItemType ORDER BY ItemType ASC")

		query.exec_()

		return query

	def getLocations(self):
		query = QSqlQuery(self.db)

		query.prepare("SELECT Location FROM Location ORDER BY Location ASC")

		query.exec_()

		print(query)

		return query

	def getAllCustomers(self):
		
		query = QSqlQuery(self.db)

		query.prepare("SELECT * FROM Customer")

		query.exec_()

		return query

	def getCustomerData(self, ID):
		
		# QSqlQuery doesn't support indexing
		# query = QSqlQuery(self.db)

		# query.prepare("SELECT * FROM Customer WHERE CustomerID = :ID")

		# query.bindValue(":ID",ID)

		# query.exec_()

		# return query

		with sqlite3.connect(self.path) as db:

			cursor = db.cursor()
			sql = "SELECT * FROM Customer WHERE CustomerID = ?"
			values = (ID,)
			cursor.execute(sql, values)
			data = cursor.fetchone()
			db.commit()

			return data

	def addCustomer(self, values, parent):
		self.parent = parent
		add_item = QSqlQuery(self.db)
		
		add_item.prepare("""INSERT INTO Customer(Title,FirstName,LastName,Company,
		Street,Town,County,PostCode,Mobile,Landline,Email) VALUES(:Title,:FirstName,:LastName,
		:Company,:Street,:Town,:County,:PostCode,:Mobile,:Landline,:Email)""")

		add_item.bindValue(":Title",values["Title"])
		add_item.bindValue(":FirstName",values["FirstName"])
		add_item.bindValue(":LastName",values["LastName"])
		add_item.bindValue(":Company",values["Company"])
		add_item.bindValue(":Street",values["Street"])
		add_item.bindValue(":Town",values["Town"])
		add_item.bindValue(":County",values["County"])
		add_item.bindValue(":PostCode",values["PostCode"])
		add_item.bindValue(":Mobile",values["Mobile"])
		add_item.bindValue(":Landline",values["Landline"])
		add_item.bindValue(":Email",values["Email"])

		success = add_item.exec_()

		if success:
			self.mssg = QMessageBox()
			self.mssg.setFixedWidth(200)
			self.mssg.setWindowTitle("Customer Added")
			self.mssg.setText("Success! Record added for {0}".format(values["FirstName"]))
			self.mssg.setIcon(QMessageBox.Information)
			self.okay_button = self.mssg.addButton(self.parent.tr("Okay"), QMessageBox.AcceptRole)
			self.mssg.setEscapeButton(self.okay_button)
			self.mssg.setDefaultButton(self.okay_button)
			self.okay_button.clicked.connect(self.parent.editEntry)
			self.mssg.exec_()
			return True
		else:
			self.error_message_dialog = QMessageBox()
			self.error_message_dialog.setFixedWidth(200)
			self.error_message_dialog.setWindowTitle("Input Error")
			self.error_message_dialog.setText("Error! Failed to commit to database\n"
											  "\n"
											  "Click the 'Show details' button for more information")
			self.error_message_dialog.setDetailedText("Database Error:\n \n "
											  "{0}".format(add_item.lastError().text()))
			self.error_message_dialog.setIcon(QMessageBox.Warning)
			self.okay_button = self.error_message_dialog.addButton(self.parent.tr("Okay"), QMessageBox.AcceptRole)
			self.error_message_dialog.setEscapeButton(self.okay_button)
			self.error_message_dialog.setDefaultButton(self.okay_button)
			self.okay_button.clicked.connect(self.parent.editEntry)
			self.error_message_dialog.exec_()
			return False


	def getSearchQuery(self, queryText):

		searchText = queryText

		if searchText == "":
			query = self.initialTable()

			return query
		else:

			query = QSqlQuery(self.db)

			query.prepare("""SELECT * FROM Client WHERE
	   ClientFirstName LIKE '%'||:searchString||'%' OR
	   ClientEmail LIKE '%'||:searchString2||'%' OR
	   ClientSurname LIKE '%'||:searchString3||'%' OR
	   ClientAddrLine1 LIKE '%'||:searchString4||'%' OR
	   ClientAddrLine2 LIKE '%'||:searchString5||'%' OR
	   ClientAddrLine3 LIKE '%'||:searchString6||'%' OR
	   ClientAddrLine4 LIKE '%'||:searchString7||'%' OR
	   ClientPhoneNumber LIKE '%'||:searchString8||'%'
		""")
		

			query.bindValue(":searchString", searchText)
			query.bindValue(":searchString2", searchText)
			query.bindValue(":searchString3", searchText)
			query.bindValue(":searchString4", searchText)
			query.bindValue(":searchString5", searchText)
			query.bindValue(":searchString6", searchText)
			query.bindValue(":searchString7", searchText)
			query.bindValue(":searchString8", searchText)

			success = query.exec_()

			if success:
				return query
			else:
				
				error =  query.lastError()
				print(error.text())

				return query


				
