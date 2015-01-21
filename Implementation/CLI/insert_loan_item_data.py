import sqlite3

from display_records_menu import *
from delete_records_menu import *

def get_loan_id(db_name):
    display_loan_only_records(db_name)
    loan_list = select_all_loans(db_name)
    max_records = len(loan_list)
    id = select_record(max_records)
    return id

def get_item_id(db_name):
    display_item_records(db_name)
    items_list = select_all_items(db_name)
    max_records = len(items_list)
    id = select_record(max_records)
    return id

def get_quantity():
    valid = False
    while not valid:
        try:
            quantity = int(input("How many of this item is to be loaned out in this loan?: "))
            if quantity > 0:
                valid = True
            else:
                valid = False
                print("Please enter a valid quantity")
        except ValueError:
            print("Please enter a valid quantity")

def get_loan_item_data(db_name):
    loan_id = get_loan_id(db_name)
    item_id = get_item_id(db_name)
    quantity = get_quantity()
    return loan_id, item_id, quantity

def insert_loan_item_values(db_name, loan_id, item_id, quantity):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = """insert into Loan(
                 LoanID,
                 ItemID,
                 Quantity,
                 values (?,?,?)"""
        values = (loan_id, item_id, quantity)
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    loan_item_values = get_loan_item_data()
    insert_loan_item_values(db_name, values)
