import sqlite3

from display_records_menu  import *

from select_existing_items import *
from select_existing_customers import *
from select_existing_loans import *
from select_existing_loan_items import *
from select_existing_pat_tests import *
from select_existing_item_tests import *

from delete_existing_item import *
from delete_existing_customer import *
from delete_existing_loan import *
from delete_existing_loan_item import *
from delete_existing_pat_test import *
from delete_existing_item_test import *

def display_delete_records_menu():
    print("""
Delete Records Menu
===================

1. Delete Item Record
2. Delete Customer Record
3. Delete Loan Record
4. Delete Loan Item Record
5. Delete PAT Test Record
6. Delete Item Test Record
0. Cancel
""")

    
def get_delete_records_menu_choice():
    valid = False
    while not valid:
        try:
            choice = int(input("Please select a menu option: "))
            if choice in range(0,7):
                valid = True
            else:
                print("Please enter a valid menu option")
                valid = False
        except ValueError:
            print("Please enter a valid menu option")
    return choice

def select_record(max_records):
    valid = False
    while not valid:
        try:
            record_id = int(input("Please enter the ID of the record to delete: "))
            if record_id >= 1:
                valid = True
            else:
                valid = False
                print("Please enter a valid ID")
        except ValueError:
            print("Please enter a valid ID")
    return record_id

def delete_item(db_name):
    display_item_records(db_name)
    items_list = select_all_items(db_name)
    max_records = len(items_list)
    id = select_record(max_records)
    delete_selected_item(db_name, id)

def delete_item_type(db_name):
    display_item_type_only_records(db_name)
    item_type_list = select_all_item_types(db_name)
    max_records = len(item_type_list)
    id = select_record(max_records)
    delete_selected_item_type(db_name, id)

def delete_location(db_name):
    display_location_only_records(db_name)
    locations_list = select_all_locations(db_name)
    max_records = len(item_type_list)
    id = select_record(max_records)
    delete_selected_location(db_name, id)

def delete_customer(db_name):
    display_customer_records(db_name)
    customer_list = select_all_customers(db_name)
    max_records = len(customer_list)
    id = select_record(max_records)
    delete_selected_customer(db_name, id)

def delete_loan(db_name):
    display_loan_records(db_name)
    loan_list = select_all_loans(db_name)
    max_records = len(loan_list)
    id = select_record(max_records)
    delete_selected_loan(db_name, id)

def delete_loan_item(db_name):
    display_loan_item_records(db_name)
    loan_item_list = select_all_loan_items(db_name)
    max_records = len(loan_item_list)
    id = select_record(max_records)
    delete_selected_loan_item(db_name, id)

def delete_pat_test(db_name):
    display_pat_test_records(db_name)
    pat_test_list = select_all_pat_tests(db_name)
    max_records = len(pat_test_list)
    id = select_record(max_records)
    delete_selected_pat_test(db_name, id)

def delete_item_test(db_name):
    display_item_test_records(db_name)
    item_test_list = select_all_item_tests(db_name)
    max_records = len(item_test_list)
    id = select_record(max_records)
    delete_selected_item_test(db_name, id)
    

def delete_records_main(db_name):
    finished = False
    while not finished:
        display_delete_records_menu()
        selected_option = get_delete_records_menu_choice()
        if selected_option == 1:
            delete_item(db_name)
        elif selected_option == 2:
            delete_customer(db_name)
        elif selected_option == 3:
            delete_loan(db_name)
        elif selected_option == 4:
            delete_loan_item(db_name)
        elif selected_option == 5:
            delete_pat_test(db_name)
        elif selected_option == 6:
            delete_item_test(db_name)
        elif selected_option == 0:
            finished = True
