import sqlite3

def create_location_table(db_name, table_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        sql = """create table Location(
                 LocationID integer,
                 Location text,
                 Primary Key (LocationID))
                 """
        keep_table = True
        if len(result) == 1:
            valid = False
            while not valid:
                response = input("The table {0} already exists, do you wish to recreate it? (y/n): ".format(table_name))
                response = response.lower()[0]
                if response == "y":
                    valid = True
                    keep_table = False
                    print()
                    print("The {0} table will be recreated, all existing data will be lost".format(table_name))
                    cursor.execute("drop table if exists {0}".format(table_name))
                    db.commit()
                elif response == "n":
                    valid = True
                    print("The existing table was kept")
                else:
                    Valid = False
                    print("Please select a valid option")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()


def create_item_type_table(db_name, table_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor = cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        sql = """create table ItemType(
                 ItemTypeID integer,
                 ItemType text,
                 Primary Key(ItemTypeID))
                 """
        keep_table = True
        if len(result) == 1:
            valid = False
            while not valid:
                response = input("The table {0} already exists, do you wish to recreate it? (y/n): ".format(table_name))
                response = response.lower()[0]
                if response == "y":
                    valid = True
                    keep_table = False
                    print()
                    print("The {0} table will be recreated, all existing data will be lost".format(table_name))
                    cursor.execute("drop table if exists {0}".format(table_name))
                    db.commit()
                elif response == "n":
                    valid = True
                    print("The existing table was kept")
                else:
                    Valid = False
                    print("Please select a valid option")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()

def create_item_table(db_name, table_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor = cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        sql = """create table Item(
                 ItemID integer,
                 ItemName text,
                 ItemValue real,
                 LoanRate real,
                 ItemClass integer,
                 FuseRating integer,
                 ItemTypeID integer,
                 LocationID integer,
                 Primary Key(ItemID)
                 Foreign Key(ItemTypeID)
                            references ItemType(ItemTypeID)
                 Foreign Key(LocationID)
                            references Location(LocationID)
                 on update cascade
                 on delete set null)
                 """
        keep_table = True
        if len(result) == 1:
            valid = False
            while not valid:
                response = input("The table {0} already exists, do you wish to recreate it? (y/n): ".format(table_name))
                response = response.lower()[0]
                if response == "y":
                    valid = True
                    keep_table = False
                    print()
                    print("The {0} table will be recreated, all existing data will be lost".format(table_name))
                    cursor.execute("drop table if exists {0}".format(table_name))
                    db.commit()
                elif response == "n":
                    valid = True
                    print("The existing table was kept")
                else:
                    Valid = False
                    print("Please select a valid option")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()

def create_customer_table(db_name, table_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor = cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        sql = """create table Customer(
                 CustomerID integer,
                 FirstName text,
                 LastName text,
                 Company text,
                 Address text,
                 Town text,
                 PostCode text,
                 MobileNumber text,
                 Landline text,
                 Email text,
                 Primary Key(CustomerID))
                 """
        keep_table = True
        if len(result) == 1:
            valid = False
            while not valid:
                response = input("The table {0} already exists, do you wish to recreate it? (y/n): ".format(table_name))
                response = response.lower()[0]
                if response == "y":
                    valid = True
                    keep_table = False
                    print()
                    print("The {0} table will be recreated, all existing data will be lost".format(table_name))
                    cursor.execute("drop table if exists {0}".format(table_name))
                    db.commit()
                elif response == "n":
                    valid = True
                    print("The existing table was kept")
                else:
                    Valid = False
                    print("Please select a valid option")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()

def create_loan_table(db_name, table_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor = cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        sql = """create table Loan(
                 LoanID integer,
                 CustomerID integer,
                 StartDate integer,
                 LoanLength integer,
                 Primary Key(LoanID)
                 Foreign Key(CustomerID) references
                             Customer(CustomerID)
                 )
                 """
        keep_table = True
        if len(result) == 1:
            valid = False
            while not valid:
                response = input("The table {0} already exists, do you wish to recreate it? (y/n): ".format(table_name))
                response = response.lower()[0]
                if response == "y":
                    valid = True
                    keep_table = False
                    print()
                    print("The {0} table will be recreated, all existing data will be lost".format(table_name))
                    cursor.execute("drop table if exists {0}".format(table_name))
                    db.commit()
                elif response == "n":
                    valid = True
                    print("The existing table was kept")
                else:
                    Valid = False
                    print("Please select a valid option")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)

def create_loan_item_table(db_name, table_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor = cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        sql = """create table LoanItem(
                 LoanItemID integer,
                 LoanID integer,
                 ItemID integer,
                 Quantity integer,
                 Primary Key(LoanItemID)
                 Foreign Key(LoanID) references
                            Loan(LoanID)
                 Foreign Key(ItemID) references
                            Item(ItemID)
                 on update cascade
                 on delete set null)
                 """
        keep_table = True
        if len(result) == 1:
            valid = False
            while not valid:
                response = input("The table {0} already exists, do you wish to recreate it? (y/n): ".format(table_name))
                response = response.upper()[0]
                if response == "Y":
                    valid = True
                    keep_table = False
                    print()
                    print("The {0} table will be recreated, all existing data will be lost".format(table_name))
                    cursor.execute("drop table if exists {0}".format(table_name))
                    db.commit()
                elif response == "N":
                    valid = True
                    print("The existing table was kept")
                else:
                    Valid = False
                    print("Please select a valid option")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()

def create_pat_test_table(db_name,table_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor = cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        sql = """create table PATtest(
                 PATtestID integer,
                 TestDate text,
                 Primary Key(PATtestID))
                 """
        keep_table = True
        if len(result) == 1:
            valid = False
            while not valid:
                response = input("The table {0} already exists, do you wish to recreate it? (y/n): ".format(table_name))
                response = response.lower()[0]
                if response == "y":
                    valid = True
                    keep_table = False
                    print()
                    print("The {0} table will be recreated, all existing data will be lost".format(table_name))
                    cursor.execute("drop table if exists {0}".format(table_name))
                    db.commit()
                elif response == "n":
                    valid = True
                    print("The existing table was kept")
                else:
                    Valid = False
                    print("Please select a valid option")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()

def create_item_test_table(db_name,table_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor = cursor.execute("select name from sqlite_master where name=?",(table_name,))
        result = cursor.fetchall()
        sql = """create table ItemTest(
                 ItemTestID integer,
                 PATtestID integer,
                 ItemID integer,
                 PATtestNotes text,
                 ComponentType text,
                 ComponentResult text,
                 ComponentNotes text,
                 Leakage real,
                 TestResult integer,
                 Primary Key(ItemTestID)
                 Foreign Key(PATtestID)
                            references PATtest(PATtestID)
                 Foreign Key(ItemID)
                            references Item(ItemID)
                 on update cascade
                 on delete set null)
                 """
        keep_table = True
        if len(result) == 1:
            valid = False
            while not valid:
                response = input("The table {0} already exists, do you wish to recreate it? (y/n): ".format(table_name))
                response = response.lower()[0]
                if response == "y":
                    valid = True
                    keep_table = False
                    print()
                    print("The {0} table will be recreated, all existing data will be lost".format(table_name))
                    cursor.execute("drop table if exists {0}".format(table_name))
                    db.commit()
                elif response == "n":
                    valid = True
                    print("The existing table was kept")
                else:
                    Valid = False
                    print("Please select a valid option")
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()

def create_database_tables_main(db_name):
    create_location_table(db_name, "Location")
    create_item_type_table(db_name, "ItemType")
    create_item_table(db_name, "Item")
    create_customer_table(db_name, "Customer")
    create_loan_table(db_name, "Loan")
    create_loan_item_table(db_name, "LoanItem")
    create_pat_test_table(db_name, "PATtest")
    create_item_test_table(db_name, "ItemTest")

if __name__ == "__main__":
    db_name = "C3_media_database.db"
    create_database_tables_main(db_name)

