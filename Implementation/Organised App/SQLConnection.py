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

		self.password = query.value(0)

		#print(password)

		return self.password

	def updatePassword(self, newPassword):
		query = QSqlQuery(self.db)

		query.prepare("""UPDATE Password SET Password = :NewPassword WHERE Password = :OldPassword""")

		query.bindValue(":OldPassword",self.password)
		query.bindValue(":NewPassword",newPassword)

		success = query.exec_()

		if success:
			return True
		else:
			self.error = query.lastError().text()
			return False

		

	def initialItemsTable(self):

		query = QSqlQuery(self.db)
		query.prepare("""SELECT Item.ItemName, Item.ItemValue, Item.LoanRate,
			Item.ItemClass, Item.FuseRating,  ItemType.ItemTypeID, Location.LocationID
			FROM Item, ItemType, Location
			WHERE Item.ItemTypeID = ItemType.ItemTypeID AND Item.LocationID = Location.LocationID
			AND 1=0""")
		query.exec_()

		return query

	def getAllItems(self):
		
		query = QSqlQuery(self.db)

		query.prepare("SELECT * FROM Item")

		query.exec_()

		return query

	def getItemData(self, ID):
		
		# QSqlQuery doesn't support indexing
		# query = QSqlQuery(self.db)

		# query.prepare("SELECT * FROM Customer WHERE CustomerID = :ID")

		# query.bindValue(":ID",ID)

		# query.exec_()

		# return query

		with sqlite3.connect(self.path) as db:

			cursor = db.cursor()
			sql = """SELECT * FROM Item WHERE ItemID = ?"""
			values = (ID,)
			cursor.execute(sql, values)
			data = cursor.fetchone()
			db.commit()

			return data


	def addItem(self, values, parent):
		self.parent = parent
		addItem = QSqlQuery(self.db)

		addItem.prepare("""INSERT INTO Item(ItemName,ItemValue,LoanRate,
		ItemClass,FuseRating,ItemTypeID,LocationID) VALUES(:ItemName,:ItemValue,
		:LoanRate,:ItemClass,:FuseRating,:ItemTypeID,:LocationID)""")

		addItem.bindValue(":ItemName",values["ItemName"])
		addItem.bindValue(":ItemValue",values["ItemValue"])
		addItem.bindValue(":LoanRate",values["LoanRate"])
		addItem.bindValue(":ItemClass",values["ItemClass"])
		addItem.bindValue(":FuseRating",values["FuseRating"])
		addItem.bindValue(":ItemTypeID",values["ItemTypeID"])
		addItem.bindValue(":LocationID",values["LocationID"])

		success = addItem.exec_()

		if success:
			return True
		else:
			self.error = addItem.lastError().text()
			return False

	def updateItem(self,values):
		updateCustomer = QSqlQuery(self.db)

		updateCustomer.prepare("""
UPDATE Customer SET ItemName = :ItemName, ItemValue = :ItemValue,
LoanRate = :LoanRate, ItemClass = :ItemClass, FuseRating =:FuseRating,
ItemTypeID = :ItemTypeID, LocationID = :LocationID
WHERE ItemID = :ItemID;
""")
		updateCustomer.bindValue(":ItemID",values["ItemID"])
		updateCustomer.bindValue(":ItemName",values["ItemName"])
		updateCustomer.bindValue(":ItemValue",values["ItemValue"])
		updateCustomer.bindValue(":LoanRate",values["LoanRate"])
		updateCustomer.bindValue(":ItemClass",values["ItemClass"])
		updateCustomer.bindValue(":FuseRating",values["FuseRating"])
		updateCustomer.bindValue(":ItemTypeID",values["ItemTypeID"])
		updateCustomer.bindValue(":LocationID",values["LocationID"])


	def getAllItemTypes(self):
		with sqlite3.connect(self.path) as db:

			cursor = db.cursor()
			sql = "SELECT ItemType FROM ItemType ORDER BY ItemType ASC"
			values = (ID,)
			cursor.execute(sql, values)
			data = cursor.fetchone()
			db.commit()

			return data

	def deleteItem(self, ID):
		
		query = QSqlQuery(self.db)

		query.prepare("DELETE FROM Item WHERE ItemID = :ID")

		query.bindValue(":ID",ID)

		self.error = query.lastError().text()

		print(self.error)

		query.exec_()

		return query

	def getItemSearchQuery(self, queryText):

		searchText = queryText

		if searchText == "":
			query = self.initialCustomerTable()

			return query
		else:

			query = QSqlQuery(self.db)

			query.prepare("""SELECT * FROM Item WHERE
	   Item.ItemName LIKE '%'||:searchString||'%' OR
	   ItemType.ItemType LIKE '%'||:searchString2||'%' OR
	   Location.Location LIKE '%'||:searchString3||'%'
		""")
		

			query.bindValue(":searchString", searchText)
			query.bindValue(":searchString2", searchText)
			query.bindValue(":searchString3", searchText)

			success = query.exec_()

			if success:
				return query
			else:
				
				error =  query.lastError()
				print(error.text())

				return query

	def getLocations(self):
		with sqlite3.connect(self.path) as db:

			cursor = db.cursor()
			sql = "SELECT Customer FROM Customer ORDER BY Customer ASC"
			values = (ID,)
			cursor.execute(sql, values)
			data = cursor.fetchone()
			db.commit()

			return data

	def initialCustomerTable(self):

		query = QSqlQuery(self.db)
		query.prepare("SELECT * FROM Customer WHERE 1=0")
		query.exec_()

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
		addCustomer = QSqlQuery(self.db)
		
		addCustomer.prepare("""INSERT INTO Customer(Title,FirstName,LastName,Company,
		Street,Town,County,PostCode,Mobile,Landline,Email) VALUES(:Title,:FirstName,:LastName,
		:Company,:Street,:Town,:County,:PostCode,:Mobile,:Landline,:Email)""")

		addCustomer.bindValue(":Title",values["Title"])
		addCustomer.bindValue(":FirstName",values["FirstName"])
		addCustomer.bindValue(":LastName",values["LastName"])
		addCustomer.bindValue(":Company",values["Company"])
		addCustomer.bindValue(":Street",values["Street"])
		addCustomer.bindValue(":Town",values["Town"])
		addCustomer.bindValue(":County",values["County"])
		addCustomer.bindValue(":PostCode",values["PostCode"])
		addCustomer.bindValue(":Mobile",values["Mobile"])
		addCustomer.bindValue(":Landline",values["Landline"])
		addCustomer.bindValue(":Email",values["Email"])

		success = addCustomer.exec_()

		if success:
			return True
		else:
			self.error = addCustomer.lastError().text()
			return False

	def updateCustomer(self,values):
		updateCustomer = QSqlQuery(self.db)

		updateCustomer.prepare("""
UPDATE Customer SET Title = :Title, FirstName = :FirstName, LastName = :LastName,
Company = :Company, Street = :Street, Town = :Town, County = :County, 
PostCode = :PostCode, Mobile = :Mobile, Landline = :Landline,
Email = :Email
WHERE CustomerID = :CustomerID;
""")
		updateCustomer.bindValue(":CustomerID",values["ID"])
		updateCustomer.bindValue(":Title",values["Title"])
		updateCustomer.bindValue(":FirstName",values["FirstName"])
		updateCustomer.bindValue(":LastName",values["LastName"])
		updateCustomer.bindValue(":Company",values["Company"])
		updateCustomer.bindValue(":Street",values["Street"])
		updateCustomer.bindValue(":Town",values["Town"])
		updateCustomer.bindValue(":County",values["County"])
		updateCustomer.bindValue(":PostCode",values["PostCode"])
		updateCustomer.bindValue(":Mobile",values["Mobile"])
		updateCustomer.bindValue(":Landline",values["Landline"])
		updateCustomer.bindValue(":Email",values["Email"])


	def deleteCustomer(self, ID):
		
		query = QSqlQuery(self.db)

		query.prepare("DELETE FROM Customer WHERE CustomerID = :ID")

		query.bindValue(":ID",ID)

		self.error = query.lastError().text()

		print(self.error)

		query.exec_()

		return query


	def getCustomerSearchQuery(self, queryText):

		searchText = queryText

		if searchText == "":
			query = self.initialCustomerTable()

			return query
		else:

			query = QSqlQuery(self.db)

			query.prepare("""SELECT * FROM Customer WHERE
	   FirstName LIKE '%'||:searchString||'%' OR
	   LastName LIKE '%'||:searchString2||'%' OR
	   Company LIKE '%'||:searchString3||'%' OR
	   Street LIKE '%'||:searchString4||'%' OR
	   Town LIKE '%'||:searchString5||'%' OR
	   County LIKE '%'||:searchString6||'%' OR
	   PostCode LIKE '%'||:searchString7||'%' OR
	   Mobile LIKE '%'||:searchString8||'%' OR
	   Landline LIKE '%'||:searchString9||'%' OR
	   Email LIKE '%'||:searchString10||'%'
		""")
		

			query.bindValue(":searchString", searchText)
			query.bindValue(":searchString2", searchText)
			query.bindValue(":searchString3", searchText)
			query.bindValue(":searchString4", searchText)
			query.bindValue(":searchString5", searchText)
			query.bindValue(":searchString6", searchText)
			query.bindValue(":searchString7", searchText)
			query.bindValue(":searchString8", searchText)
			query.bindValue(":searchString9", searchText)
			query.bindValue(":searchString10", searchText)

			success = query.exec_()

			if success:
				return query
			else:
				
				error =  query.lastError()
				print(error.text())

				return query


				
