
from PyQt4.QtSql import *

import sqlite3

from NewDatabase import *

class SQLConnection:
    
    """Handles the conncetion to the SQL database"""
    
    def __init__(self,path):

        self.path = path

        self.db = None
        
    def create_database(self):
        
        db = create_db(self.path)

        if db == True:
        
            self.db = QSqlDatabase.addDatabase("QSQLITE")
            self.db.setDatabaseName(self.path)

            opened_ok = self.db.open()

            return opened_ok
        
        else:
            
            return False

    
    def create_table(self,table_name,sql):
        
        with sqlite3.connect(self.path) as db:
            cursor = db.cursor()
            cursor.execute("select name from sqlite_master where name=?",(table_name,))
            result = cursor.fetchall()
            if len(result) == 1:
                pass
            else:
                cursor.execute(sql)
                db.commit()

    def open_database(self):
        
        if self.db:
            self.close_database()

        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.path)

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

    def updateClient(self, values):

        query = QSqlQuery(self.db)

        query.prepare("""
UPDATE Client SET ClientTitle = :clientTitle, ClientFirstName = :clientFirstName, ClientSurname = :clientSurname,
ClientAddrLine1 = :clientStreet, ClientAddrLine2 = :clientTown, ClientAddrLine3 = :clientCounty,
ClientAddrLine4 = :clientPostCode, ClientEmail = :clientEmail, ClientPhoneNumber = :clientPhoneNumber
WHERE ClientID = :clientID;
""")
        query.bindValue(":clientID",values["ID"])
        query.bindValue(":clientTitle",values["Title"])
        query.bindValue(":clientFirstName",values["FirstName"])
        query.bindValue(":clientSurname",values["Surname"])
        query.bindValue(":clientStreet",values["Street"])
        query.bindValue(":clientTown",values["Town"])
        query.bindValue(":clientCounty",values["County"])
        query.bindValue(":clientPostCode",values["PostCode"])
        query.bindValue(":clientEmail",values["Email"])
        query.bindValue(":clientPhoneNumber",values["PhoneNumber"])


        success = query.exec_()

        if success:
            self.db.commit()
            return True
        else:
            return False
            
    def addClient(self, values):

        query = QSqlQuery(self.db)
        
        query.prepare(""" INSERT INTO Client(ClientTitle,ClientFirstName,ClientSurname,ClientAddrLine1,
ClientAddrLine2,ClientAddrLine3,ClientAddrLine4,ClientEmail,ClientPhoneNumber) VALUES(:clientTitle,
:clientFirstName,:clientSurname,:clientStreet,:clientTown,:clientCounty,:clientPostCode,:clientEmail,
:clientPhoneNumber)""")

        query.bindValue(":clientTitle",values["Title"])
        query.bindValue(":clientFirstName",values["FirstName"])
        query.bindValue(":clientSurname",values["Surname"])
        query.bindValue(":clientStreet",values["Street"])
        query.bindValue(":clientTown",values["Town"])
        query.bindValue(":clientCounty",values["County"])
        query.bindValue(":clientPostCode",values["PostCode"])
        query.bindValue(":clientEmail",values["Email"])
        query.bindValue(":clientPhoneNumber",values["PhoneNumber"])

        success = query.exec_()

        if success:
            return True
        else:
            return False
        
##            print("Failure!")
##            error = query.lastError()
##        
##            print(error.text())


    def addPlasterer(self, values):

        query = QSqlQuery(self.db)
        
        query.prepare(""" INSERT INTO Plasterer(PlastererTitle,PlastererFirstName,PlastererSurname,PlastererAddrLine1,
PlastererAddrLine2,PlastererAddrLine3,PlastererAddrLine4,PlastererEmail,PlastererPhoneNumber,PlastererDailyRate) VALUES(:plastererTitle,
:plastererFirstName,:plastererSurname,:plastererStreet,:plastererTown,:plastererCounty,:plastererPostCode,:plastererEmail,
:plastererPhoneNumber,:plastererDailyRate)""")

        query.bindValue(":plastererTitle",values["Title"])
        query.bindValue(":plastererFirstName",values["FirstName"])
        query.bindValue(":plastererSurname",values["Surname"])
        query.bindValue(":plastererStreet",values["Street"])
        query.bindValue(":plastererTown",values["Town"])
        query.bindValue(":plastererCounty",values["County"])
        query.bindValue(":plastererPostCode",values["PostCode"])
        query.bindValue(":plastererEmail",values["Email"])
        query.bindValue(":plastererPhoneNumber",values["PhoneNumber"])
        query.bindValue(":plastererDailyRate",values["DailyRate"])

        success = query.exec_()

        if success:
            return True
        else:
            return False

    def getAllClients(self):

        query = QSqlQuery(self.db)

        query.prepare("SELECT * FROM Client")

        query.exec_()

        return query

    def getAllPlasterers(self):

        query = QSqlQuery(self.db)

        query.prepare("SELECT * FROM Plasterer")

        query.exec_()

        return query

    
    def initialTable(self):

        query = QSqlQuery(self.db)
        query.prepare("SELECT * FROM Client WHERE 1=0")
        query.exec_()

        return query

    def initialTableP(self):

        query = QSqlQuery(self.db)
        query.prepare("SELECT * FROM Plasterer WHERE 1=0")
        query.exec_()

        return query
        
    
    def getClientData(self, clientID):
##
##        query = QSqlQuery(self.db)
##        query.prepare("SELECT * FROM Client WHERE ClientID = :clientId")
##        query.bindValue(":clientId", clientID)
##        query.exec_()

        with sqlite3.connect(self.path) as db:

            cursor = db.cursor()
            sql = "SELECT * FROM Client WHERE ClientID = ?"
            values = (clientID,)
            cursor.execute(sql, values)
            data = cursor.fetchone()
            db.commit()

            return data
            

        
        
    

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

                
    def closeEvent(self,event):
        
        self.close_database()
