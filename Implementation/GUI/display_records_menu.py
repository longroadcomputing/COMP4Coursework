import sqlite3

from select_existing_items import *
from select_existing_customers import *
from select_existing_loans import *
from select_existing_loan_items import *
from select_existing_pat_tests import *
from select_existing_item_tests import *

def display_records_menu():
	print("""
Display Records Menu
====================

1. Display Item Records
2. Display Customer Records
3. Display Loan Records
4. Display PAT Test Records
5. Display Location Records (With Items)
6. Display Location Records (Without Items)
7. Display Item Type Records (With Items)
8. Display Item Type Records (Without Items)
0. Exit
""")

def get_display_records_menu_option():
	valid = False
	while not valid:
		try:
			choice = int(input("Please select a option: "))
			if choice in range(0,9):
				valid = True
			else:
				valid = False
				print("That is not a valid option")
				print()
		except ValueError:
			print("That is not a valid option")
	return choice

#==================Display ItemType Records==================#

def display_item_type_only_records(db_name):
	item_types = select_all_item_types(db_name)
	print()
	print("Item Types")
	print("=========")
	for item_type in item_types:
		print("{0:<15}".format(item_type[1]))
	print()

def display_item_types_with_id(db_name):
	item_types = select_all_item_types_for_id_selection(db_name)
	print()
	print("Item Types")
	print("=========")
	for item_type in item_types:
		print("{0}.{1:<15}".format(item_type[0], item_type[1]))
	print()

def display_item_type_records(db_name):
	item_types = select_all_item_types(db_name)
	items = select_all_items(db_name)
	print()
	print("Item Types")
	print("=========")
	for item_type in item_types:
		print("{0}:".format(item_type[1]))
		print()
		for item in items:
			if item[8] == item_type[0]:
				print("   {0:<20}{1:<8}".format(item[1],item[2]))
				print()
		print()

#==================Display Location Records==================#

def display_location_only_records(db_name):
	locations = select_all_locations(db_name)
	print()
	print("Locations")
	print("=========")
	for location in locations:
		print("{0:<15}".format(location[1]))
	print()

def display_locations_with_id(db_name):
	locations = select_all_locations_for_id_selection(db_name)
	print()
	print("Locations")
	print("=========")
	for location in locations:
		print("{0}.{1:<15}".format(location[0], location[1]))
	print()

def display_location_records(db_name):
	locations = select_all_locations(db_name)
	items = select_all_items(db_name)
	print()
	print("Locations")
	print("=========")
	for location in locations:
		print("{0}:".format(location[1]))
		print()
		for item in items:
			if item[9] == location[0]:
				print("  {0:<20}{1:<8}".format(item[1],item[2]))
				print()
		print()
		
#====================Display Item Records====================#

def display_item_records(db_name):
	items = select_all_items(db_name)
	print()
	print("{0:<5}{1:<30}{2:<11}{3:<15}{4:<10}{5:<15}{6:<20}{7:<15}".format("ID","Name","Value","Loan Rate","Class","Fuse Rating","Item Type", "Location"))
	print("=======================================================================================================================")
	print()
	for item in items:
		print("{0:<5}{1:<30}£{2:<10}£{3:<14}{4:<10}{5:<15}{6:<20}{7:<15}".format(item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7]))
		print()

#==================Display Customer Records==================#

def display_customer_records(db_name):
	customers = select_all_customers(db_name)
	print()
	print("{0:<5}{1:<15}{2:<15}{3:<15}{4:<20}{5:<15}{6:<10}{7:<15}{8:<15}{9:<25}".format("ID","Forename","Surname","Company","Address","Town","PostCode","Mobile","Landline","Email"))
	print("======================================================================================================================================================")
	print()
	for customer in customers:
		print("{0:<5}{1:<15}{2:<15}{3:<15}{4:<20}{5:<15}{6:<15}{7:<15}{8:<15}{9:25}".format(customer[0],customer[1],customer[2],customer[3],customer[4],customer[5],customer[6],customer[7],customer[8],customer[9]))
		print()

#====================Display Loan Records====================#

def display_loan_only_records(db_name):
	loans = select_all_loans(db_name)
	print()
	print("{0:<5}{1:<10}{2:<15}{3:<15}{4:<10}".format("ID", "CustomerID", "Company", "Start Date", "Length"))
	print("===================================================================================")
	for loan in loans:
		print("{0:<5}{1:<10}{2:<15}{3:<15}{4:<10}".format(loan[0], loan[3], loan[4], loan[1], loan[2]))
		print()


def display_loan_records(db_name):
	loans = select_all_loans(db_name)
	loan_items = select_all_loan_items(db_name)
	print()
	print("{0:<8}{1:<20}{2:<30}{3:<15}{4:<10}".format("LoanID", "CustomerID", "Company", "Start Date", "Length"))
	print("===================================================================================")
	for loan in loans:
		print("{0:<8}{1:<20}{2:<30}{3:<15}{4:<10}".format(loan[0], loan[3], loan[4], loan[1], loan[2]))
		print()
		print("  {0:<15}{1:<15}{2:<10}{3:<10}£{4:<10}".format("LoanItemID","Item Name", "Quantity", "Loan Rate", "Cost"))
		print("  ============================================================")
		for loan_item in loan_items:
			if loan_item[1] == loan[0]:
				loan_rate = loan_item[2]
				quantity = loan_item[1]
				loan_item_cost = loan_rate * quantity
				print("    {0:<15}{1:<15}{2:<10}{3:<10}{4:<10}".format(loan_item[0], loan_item[3], loan_item[2], loan_item[4], loan_item_cost))
				print()
				total_cost = total_cost + cost
		print("  {0:<8}{1:<20}{2:<30}{3:>15}£{4:<10}".format("", "", "", "TOTAL:", total_cost))
		print()

#==================Display LoanItem Records==================#

def display_loan_item_records(db_name):
	loan_items = select_all_loan_items(db_name)
	print("{0:<5}{1:<15}{2:<10}{3:<10}{4:<10}".format("ID","Item Name", "Quantity", "Loan Rate", "Cost"))
	print("==================================================")
	print()
	for loan_item in loan_items:
		loan_rate = loan_item[2]
		quantity = loan_item[1]
		loan_item_cost = loan_rate * quantity
		print("{0:<5}{1:<15}{2:<10}{3:<10}£{4:<10}".format(loan_item[0], loan_item[2], loan_item[1], loan_item[3], loan_item_cost))

#==================Display PAT Test Records==================#

def display_pat_test_only_records(db_name):
	pat_tests = select_all_pat_tests(db_name)
	print()
	print("PAT Tests")
	print("=========")
	print()
	for pat_test in pat_tests:
		print()
		print("{0:<10}".format(pat_test[1]))
		print()

def display_pat_test_records(db_name):
	pat_tests = select_all_pat_tests(db_name)
	item_tests = select_all_item_tests(db_name)
	print()
	print("PAT Test")
	print("========")
	print()
	for pat_test in pat_tests:
		print()
		print("{1:<10}".format(pat_test[1]))
		print()
		print("  Item Test")
		print("  =========")
		print()
		print("  {0:<5}{1:<20}{2:<15}{3:<15}{4:<15}{5:<30}".format("ID", "Item Name", "Item Class", "Fuse Rating", "Leakage", "Test Result", "Notes"))
		print("  =========================================================================================================")
		for item_test in item_tests:
			if item_test[7] == pat_test[0]:
				print()
				print("  {0:<5}{1:<20}{2:<15}{3:<15}{4:<15}{5:<30}".format(item_test[0], item_test[4], item_test[5], item_test[6], item_test[2], item_test[3], item_test[1]))

#==================Display ItemTest Records==================#

def display_item_test_records(db_name):
	item_tests = select_all_item_tests(db_name)
	print()
	print("PAT Test")
	print("========")
	print()
	print("{0:<3}{1:<20}{2:<15}{3:<15}{4:<15}{5:<30}".format("ID", "Item Name", "Item Class", "Fuse Rating", "Leakage", "Test Result", "Notes"))
	print("=========================================================================================================")
	for item_test in item_tests:
		print()
		print("{0:<3}{1:<20}{2:<15}{3:<15}{4:<15}{5:<30}".format(item_test[0], item_test[4], item_test[5], item_test[6], item_test[2], item_test[3], item_test[1]))

#============================================================#

def display_records_main(db_name):
	finished = False
	while not finished:
		print()
		display_records_menu()
		selected_option = get_display_records_menu_option()
		if selected_option == 1:
			display_item_records(db_name)
		elif selected_option == 2:
			display_customer_records(db_name)
		elif selected_option == 3:
			display_loan_records(db_name)
		elif selected_option == 4:
			display_pat_test_records(db_name)
		elif selected_option == 5:
			display_location_records(db_name)
		elif selected_option == 6:
			display_location_only_records(db_name)
		elif selected_option == 7:
			display_item_type_records(db_name)
		elif selected_option == 8:
			display_item_type_only_records(db_name)
		elif selected_option == 0:
			finished = True
