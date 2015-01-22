import sqlite3

from delete_records_menu import *

def get_item_id(db_name):
    display_item_records(db_name)
    items_list = select_all_items(db_name)
    max_records = len(items_list)
    item_id = select_record(max_records)
    return item_id

def get_pat_test_id(db_name):
    display_pat_test_records(db_name)
    pat_test_list = select_all_pat_tests(db_name)
    max_records = len(pat_test_list)
    pat_test_id = select_record(max_records)
    return pat_test_id 

def get_item_class():
    valid = False
    while not valid:
        print("| Class 1 | Class 2 |")
        print()
        try:
            item_class = int(input("Please choose an item class: "))
            if item_class in (1,2):
                valid = True
            else:
                valid = False
                print("That is not a valid class")
                print()
        except ValueError:
            print("That is not a valid class")
    return item_class

def get_item_fuse_rating():
    valid = False
    while not valid:
        print("| 3A | 5A | 7A | 13A |")
        print()
        try:
            fuse_rating = int(input("Please enter the fuse rating(A): "))
            if fuse_rating in (3,5,7,13):
                valid = True
            else:
                valid = False
                print("That is not a fuse rating ")
                print()
        except ValueError:
            print("That is not a valid fuse rating")
    return fuse_rating

def get_test_used():
    valid = False
    while not valid:
        test_used = input("Please enter the test type used")
        if len(test_used) > 0:
            valid = True
        else:
            print("You must enter a test type")
            valid = False
    return test_used


def get_leakage():
    valid = False
    while not valid:
        try:
            leakage = float(input("Please enter the Insulation Test result: "))
            if leakage <= 0.75 :
                valid = True
            else:
                valid = False
                print("That is not a valid result")
                print()
        except ValueError:
            print("That is not a valid result")
    return cond_test_result

def get_result(leakage):
    valid = False
    while not valid:
        test_passed = input("Did the item pass the test?(y/n): ")
        test_passed = test_passed[0].upper()
        if test_passed == "Y":
            test_result = "Pass"
        elif test_passed == "N":
            test_result = "Fail"
    return test_result

def get_item_test_data(db_name):
    item_id = get_item_id(db_name)
    pat_test_id = get_pat_test_id(db_name)
    test_used = get_test_used()
    leakage = get_leakage()
    test_result = get_result()
    return item_id, pat_test_id, test_used, leakage, test_result

def insert_new_item_test(db_name, item_id, pat_test_id, test_used, leakage, test_result):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = """insert into ItemTest(
                 PATtestID,
                 ItemID,
                 PATtestNotes,
                 Leakage,
                 TestResult)
                 values (?,?,?,?,?)
                 """
        values = (item_id, pat_test_id, test_used, leakage, test_result)
        cursor.execute(sql,values)
        db.commit()
        
        

if __name__ == "__main__":
    values = get_item_test_data()
    insert_item_test_data(values)
