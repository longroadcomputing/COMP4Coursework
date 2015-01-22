import sqlite3

from display_records_menu import *


def get_item_name():
    valid = False
    while not valid:
        name = input("Please enter the name of the item: ")
        if len(name) > 0:
            valid = True
        else:
            valid = False
    return name

def get_item_value():
    valid = False
    while not valid:
        try:
            value = float(input("Please enter the value of the item: £"))
            if value > 0:
                valid = True
            else:
                print("Please enter an item value")
                valid = False
        except ValueError:
            print("Please enter an integer")
    return value

def get_loan_rate():
    valid = False
    while not valid:
        try:
            loan_rate = float(input("Please enter the loan rate of the item: £"))
            if loan_rate >= 0: 
                valid = True
            else:
                print("Please enter a valid loan rate")
                valid = False
        except ValueError:
            print("Please enter a valid loan rate")
    return loan_rate

def get_item_class():
    valid = False
    while not valid:
        try:
            item_class = int(input("Please enter the item class(1 or 2): "))
            if item_class == 1 or item_class == 2:
                valid = True
            else:
                print("Please enter a valid quantity")
                valid = False
        except ValueError:
            print("Please enter an integer")
    return item_class

def get_fuse_rating():
    valid = False
    while not valid:
        print()
        print("==============================================")
        print("'0', '3', '5', '7', '10', '13', '-', 'No Fuse'")
        print("==============================================")
        print()
        fuse_rating = input("Please enter the item's fuse rating: ")
        if fuse_rating in ["0", "3", "5", "7","10","13", "-", "No Fuse", ""]:
            valid = True
        else:
            print("Please enter a valid fuse rating")
            valid = False
    return fuse_rating

def get_item_type_id(db_name):
    display_item_types_with_id(db_name)
    valid = False
    while not valid:
        try:
            print()
            item_type_id = int(input("Please enter the item type id: "))
            if item_type_id > 0:
                valid = True
            else:
                print("Please enter a valid id")
                valid = False
        except ValueError:
            print("Please enter an integer")
    return item_type_id

def get_location_id(db_name):
    display_locations_with_id(db_name)
    valid = False
    while not valid:
        try:
            print()
            location_id = int(input("Please enter the location id: "))
            if location_id > 0:
                valid = True
            else:
                print("Please enter a valid id")
                valid = False
        except ValueError:
            print("Please enter an integer")
    return location_id

def get_item_data(db_name):
    name = get_item_name()
    value = get_item_value()
    loan_rate = get_loan_rate()
    item_class = get_item_class()
    fuse_rating = get_fuse_rating()
    item_type_id = get_item_type_id(db_name)
    location_id = get_location_id(db_name)
    return name, value, loan_rate, item_class, fuse_rating, item_type_id, location_id
    

def get_item_type():
    valid = False
    while not valid:
        item_type = input("Please enter the item type: ")
        if len(item_type) > 0:
            valid = True
        else:
            valid = False
    return item_type

def get_location():
    valid = False
    while not valid:
        location = input("Please enter the location: ")
        if len(location) > 0:
            valid = True
        else:
            valid = False
    return location

def insert_new_item(db_name, name, value, loan_rate, item_class, fuse_rating, item_type_id, location_id):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = """insert into Item(
                 ItemName,
                 ItemValue,
                 LoanRate,
                 ItemClass,
                 FuseRating,
                 ItemTypeID,
                 LocationID)
                 values (?,?,?,?,?,?,?)
                 """
        values = (name, value, loan_rate, item_class, fuse_rating, item_type_id, location_id)
        cursor.execute(sql,values)
        db.commit()

def insert_new_item_type(db_name, item_type):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = "insert into ItemType(ItemType) values (?)"
        values = (item_type,)
        cursor.execute(sql,values)
        db.commit()

def insert_new_location(db_name, location):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = """insert into Location(
                 Location)
                 values (?)
                 """
        values = (location,)
        cursor.execute(sql,values)

if __name__ == "__main__":
    values = get_item_data(db_name)
    insert_new_item(values)
