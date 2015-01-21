import sqlite3

from display_records_menu  import *

from select_existing_items import *
from select_existing_customers import *
from select_existing_loans import *
from select_existing_loan_items import *
from select_existing_pat_tests import *
from select_existing_item_tests import *

from update_existing_item import *
from update_existing_customer import *
from update_existing_loan import *
from update_existing_loan_item import *
from update_existing_pat_test import *
from update_existing_item_test import *

from insert_item_data import *
from insert_customer_data import *
from insert_loan_data import *
from insert_loan_item_data import *
from insert_pat_test_data import *
from insert_item_test_data import *

def display_update_records_menu():
    print("""
Update Records Menu
===================

1. Update Item Record
2. Update Customer Record
3. Update Loan Record
4. Update Loan Item Record
5. Update PAT Test Record
6. Update Item Test Record
0. Exit
""")

def select_update_record_menu_option():
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
            record_id = int(input("Please enter the ID of the record to update: "))
            if record_id >= 1:
                valid = True
            else:
                valid = False
                print("Please enter a valid ID")
        except ValueError:
            print("Please enter a valid ID")
    return record_id

def update_item(db_name):
    display_item_records(db_name)
    items_list = select_all_items(db_name)
    max_records = len(items_list)
    id = select_record(max_records)
    id = id + 1
    name, value, loan_rate, item_class, fuse_rating, item_type_id, location_id = get_item_data(db_name)
    update_item_data_sql(db_name, name, value, loan_rate, item_class, fuse_rating, item_type_id, location_id, id)

def update_customer(db_name):
    display_customer_records(db_name)
    customer_list = select_all_customers(db_name)
    max_records = len(customer_list)
    id = select_record(max_records)
    id = id + 1
    Firstname, Lastname, company, street, town, post_code, mobile, landline, email = get_customer_data()
    update_customer_data_sql(db_name, Firstname, Lastname, company, street, town, post_code, mobile, landline, email, id)

def update_loan(db_name):
    display_loan_records(db_name)
    loan_list = select_all_loans(db_name)
    max_records = len(loan_list)
    id = select_record(max_records)
    id = id + 1
    customer_id, start_date, loan_length = get_loan_data(db_name)
    update_loan_data_sql(db_name, customer_id, start_date, loan_length, id)

def update_loan_item(db_name):
    display_loan_item_records(db_name)
    loan_item_list = select_all_loan_items(db_name)
    max_records = len(loan_item_list)
    id = select_record(max_records)
    id = id + 1
    loan_id, item_id, quantity = get_loan_item_data()
    update_loan_item_data_sql(db_name, loan_id, item_id, quantity, id)

def update_pat_test(db_name):
    display_pat_test_records(db_name)
    pat_test_list = select_all_pat_tests(db_name)
    max_records = len(pat_test_list)
    id = select_record(max_records)
    id = id + 1
    test_date = get_pat_test_data()
    update_pat_test_data_sql(db_name, test_date, id)

def update_item_test(db_name):
    display_item_test_records(db_name)
    item_test_list = select_all_item_tests(db_name)
    max_records = len(item_test_list)
    id = select_record(max_records)
    id = id + 1
    item_id, pat_test_id, test_used, leakage, test_result = get_item_test_data()
    update_item_test_data_sql(db_name, item_id, pat_test_id, test_used, leakage, test_result, id)
    

def update_records_main(db_name):
    finished = False
    while not finished:
        display_update_records_menu()
        selected_option = select_update_record_menu_option()
        if selected_option == 1:
            update_item(db_name)
        elif selected_option == 2:
            update_customer(db_name)
        elif selected_option == 3:
            update_loan(db_name)
        elif selected_option == 4:
            update_loan_item(db_name)
        elif selected_option == 5:
            update_pat_test(db_name)
        elif selected_option == 6:
            update_item_test(db_name)
        elif selected_option == 0:
            finished = True
