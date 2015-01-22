import sqlite3

from insert_item_data import *
from insert_customer_data import *
from insert_loan_data import *
from insert_loan_item_data import *
from insert_pat_test_data import *
from insert_item_test_data import *

def display_insert_record_menu():
    print("""
Add Record Menu
===================

1. Add New Item
2. Add New Item Type
3. Add New Location
4. Add New Customer
5. Add New Loan
6. Add New PAT test
0. Exit
""")

def select_insert_record_menu_option():
    valid = False
    while not valid:
        try:
            choice = int(input("Please select a option: "))
            if choice in range(0,7):
                valid = True
            else:
                valid = False
                print("That is not a valid option")
                print()
        except ValueError:
            print("That is not a valid option")
    return choice
    
#=====================New Item======================#

def new_item(db_name):
    name, value, loan_rate, item_class, fuse_rating, item_type_id, location_id = get_item_data(db_name)
    insert_new_item(db_name, name, value, loan_rate, item_class, fuse_rating, item_type_id, location_id)

#==================New Item Type====================#

def new_item_type(db_name):
    item_type = get_item_type()
    insert_new_item_type(db_name, item_type)

#===================New Location====================#

def new_location(db_name):
    location = get_location()
    insert_new_location(db_name, location)

#===================New Customer====================#

def new_customer(db_name):
    Firstname, Lastname, company, street, town, post_code, mobile, landline, email = get_customer_details()
    insert_new_customer(db_name, Firstname, Lastname, company, street, town, post_code, mobile, landline, email)

#=====================New Loan======================#

def new_loan(db_name):
    customer_id, start_date, loan_length = get_loan_data(db_name)
    insert_loan_data(db_name, customer_id, start_date, loan_length)

def new_loan_item(db_name):
    finished = False
    while not finished:
        insert_new_loan_item = input("Would you like to add an item to this loan? (y/n): ")
        insert_new_loan_item = insert_new_loan_item[0].upper()
        if insert_new_loan_item == "Y":
            loan_id, item_id, quantity = get_loan_item_data(db_name)
            insert_new_item_loan(db_name, loan_id, item_id, quantity)
        elif insert_new_loan_item == "N":
            finished = True

#==================New PAT Test=====================#
def new_pat_test(db_name):
    test_date = get_test_date()
    insert_new_pat_test(db_name, test_date)

def new_test_item(db_name):
    finished = False
    while not finished:
        insert_new_test_item = input("Would you like to add an item to this PAT test? (y/n): ")
        insert_new_test_item = insert_new_test_item[0].upper()
        if insert_new_test_item == "Y":
            item_id, pat_test_id, test_used, leakage, test_result = get_item_test_data(db_name)
            insert_new_item_test(db_name, item_id, pat_test_id, test_used, leakage, test_result)
        elif insert_new_test_item == "N":
            finished = True

def insert_records_main(db_name):
    finished = False
    while not finished:
        print()
        display_insert_record_menu()
        selected_option = select_insert_record_menu_option()
        if selected_option == 1:
            new_item(db_name)
        elif selected_option == 2:
            new_item_type(db_name)
        elif selected_option == 3:
            new_location(db_name)
        elif selected_option == 4:
            new_customer(db_name)
        elif selected_option == 5:
            new_loan(db_name)
            new_loan_item(db_name)
        elif selected_option == 6:
            new_pat_test(db_name)
            new_test_item(db_name)
        elif selected_option == 0:
            finished = True

if __name__ == "__main__":
    insert_data_main()
