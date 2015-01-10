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

    def addItem(self, values):
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
        print(add_item.lastError().text())
        if success:
            return True
        else:
            return False


    def addCustomer(self, values):
        query = QSqlQuery(self.db)
        
        query.prepare("""INSERT INTO Customer(Forename,Surname,Company,
        Street,Town,PostCode,Mobile,Landline,Email) VALUES(:Title,:Forename,:Surname,
        :Company,:Street,:Town,:County,:PostCode,:Mobile,:Landline,:Email)""")

        query.bindValue(":Title",values["Title"])
        query.bindValue(":Forename",values["Firstname"])
        query.bindValue(":Surname",values["Surname"])
        query.bindValue(":Company",values["Company"])
        query.bindValue(":Street",values["Street"])
        query.bindValue(":Town",values["Town"])
        query.bindValue(":County",values["County"])
        query.bindValue(":PostCode",values["PostCode"])
        query.bindValue(":Mobile",values["Mobile"])
        query.bindValue(":Landline",values["Landline"])
        query.bindValue(":Email",values["Email"])

        success = query.exec_()

        if success:
            return True
        else:
            return False
