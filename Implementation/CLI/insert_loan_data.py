import sqlite3

from delete_records_menu import *

def get_customer_id(db_name):
    display_customer_records(db_name)
    customer_list = select_all_customers(db_name)
    max_records = len(customer_list)
    customer_id = select_record(max_records)
    return customer_id

def get_start_date():
    valid = False
    while not valid:
        start_date = input("Please enter the start date of the loan: ")
        if len(start_date) > 0 and ["/", "-"] in start_date:
            valid = True
        else:
            valid = False
            print("Please enter a valid start date")
    return start_date

def get_loan_length():
    valid = False
    while not valid:
        try:
            loan_length = int(input("Please enter the length of the loan (days): "))
            if loan_length > 7:
                valid = False
                print("Loan length cannot be longer than 7 days")
            elif loan_length >= 0:
                valid = True
            else:
                print("Please enter a valid loan length")
                valid = False
        except ValueError:
            print("Please enter an integer")
    return loan_length

def get_loan_data(db_name):
    customer_id = get_customer_id(db_name)
    start_date = get_start_date()
    loan_length = get_loan_length()
    return customer_id, start_date, loan_length
   
def insert_new_customer_loan(db_name, customer_id, start_date, loan_length):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = """insert into Loan(
                 LoanID,
                 CustomerID,
                 StartDate,
                 LoanLength,
                 values (?,?,?,?)"""
        values = (customer_id, start_date, loan_length)
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    insert_new_customer_loan(values)
