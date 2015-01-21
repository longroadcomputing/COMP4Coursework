from regular_expressions import *

import sqlite3
import re

def get_customer_first_name():
    valid = False
    while not valid:
        Firstname = input("Please enter the customers first name: ")
        if len(Firstname) > 0:
            valid = True
        else:
            print()
            print("Please enter a name")
            print()
            valid = False
    return Firstname

def get_customer_last_name():
    valid = False
    while not valid:
        Lastname = input("Please enter the customers last name: ")
        if len(Lastname) > 0:
            valid = True
        else:
            print()
            print("Please enter a name")
            print()
            valid = False
    return Lastname

def get_customer_company():
    valid = False
    while not valid:
        company = input("Please enter the company name: ")
        if len(company) >= 0:
            valid = True
    return company

def get_customer_address():
    valid = False
    while not valid:
        address = input("Please enter the customers street address name: ")
        if len(address) > 0:
            valid = True
        else:
            print()
            print("Please enter a street address name")
            print()
            valid = False
    return address

def get_customer_town():
    valid = False
    while not valid:
        town = input("Please enter the customers town name: ")
        if len(town) > 0:
            valid = True
        else:
            print()
            print("Please enter a town name")
            print()
            valid = False
    return town

def get_customer_post_code():
    valid = False
    while not valid:
        post_code = input("Please enter the customers post code: ")
        if len(post_code) > 0:
            valid = True
        else:
            print()
            print("Please enter a post code")
            print()
            valid = False
    return post_code

def get_customer_mobile():
    valid = False
    while not valid:
        try:
            mobile = input("Please enter the customers mobile number: ")
            if len(mobile) != 11:
                valid = False
            else:
                valid = True
        except ValueError:
            print()
            print("Please enter a house number")
            print()
    return mobile

def get_customer_landline():
    valid = False
    while not valid:
        try:
            landline = input("Please enter the customers landline number: ")
            if len(landline) != 11:
                valid = False
            else:
                valid = True
        except ValueError:
            print()
            print("Please enter a house number")
            print()
    return landline

def get_customer_email():
    valid = False
    while not valid:
        email = input("Please enter the customers email: ")
        valid_email = re.match("^[a-zA-Z0-9._%-+]+@[a-zA-Z0-9._%-]+.[a-z]{2,3}(\.[a-z]{2,3})$", email)
        if len(email) > 0 and valid_email:
            valid = True
        else:
            print()
            print("Please enter an email address")
            print()
            valid = False
    return email

def get_customer_details():
    Firstname = get_customer_first_name()
    Lastname = get_customer_last_name()
    company = get_customer_company()
    street = get_customer_address()
    town = get_customer_town()
    post_code = get_customer_post_code()
    mobile = get_customer_mobile()
    landline = get_customer_landline()
    email = get_customer_email()
    return Firstname, Lastname, company, street, town, post_code, mobile, landline, email

    


def insert_new_customer(db_name, Firstname, Lastname, company, street, town, post_code, mobile, landline, email):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = """insert into Customer(
                 FirstName,
                 LastName,
                 Company,
                 Address,
                 Town,
                 PostCode,
                 MobileNumber,
                 Landline,
                 Email)
                 values (?,?,?,?,?,?,?,?,?)"""
        values = (Firstname, Lastname, company, street, town, post_code, mobile, landline, email)
        cursor.execute(sql,values)
        db.commit()

if __name__ == "__main__":
    db_name = "C3_media_database.db"
    
    insert_new_cutomer(db_name, values)
