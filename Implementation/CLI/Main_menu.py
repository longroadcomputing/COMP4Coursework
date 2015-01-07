import sqlite3

from create_database_tables import *

from insert_records_menu import *
from update_records_menu import *
from display_records_menu import *
from delete_records_menu import *

def open_database(db_name,table_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("""select name from sqlite_master where name=?""",(table_name,))

def display_main_menu():
    print("""
MAIN MENU
=========

1. Insert Records
2. Update Records
3. Display Records
4. Delete Records
9. (Re)Create Database Tables
0. Exit
""")

def select_main_menu_option():
    valid = False
    while not valid:
        try:
            choice = int(input("Please select a option: "))
            if choice in range(0,5) or choice == 9:
                valid = True
            else:
                valid = False
                print("That is not a valid option")
                print()
        except ValueError:
            print("That is not a valid option")
    return choice
    

def main():
    db_name = "C3_media_database.db"
    open_database(db_name, "Item")
    finished = False
    while not finished:
        display_main_menu()
        selected_option = select_main_menu_option()
        if selected_option == 1:
            insert_records_main(db_name)
        elif selected_option == 2:
            update_records_main(db_name)
        elif selected_option == 3:
            display_records_main(db_name)
        elif selected_option == 4:
            delete_records_main(db_name)
        elif selected_option == 9:
            create_database_tables_main(db_name)
        elif selected_option == 0:
            finished = True

if __name__ == "__main__":
    main()
