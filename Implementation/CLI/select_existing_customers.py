import sqlite3

def select_all_customers(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("""select
                          CustomerID,
                          FirstName,
                          LastName,
                          Company,
                          Address,
                          Town,
                          PostCode,
                          MobileNumber,
                          Landline,
                          Email
                          from Customer
                          """)
        customers = cursor.fetchall()
        return customers

def select_customer(db_name, id):
    with sqlite3.connect("C3_media_database.db") as db:
        cursor = db.cursor()
        sql = """select
                 CustomerID,
                 FirstName,
                 LastName,
                 Company
                 Address,
                 Town,
                 PostCode,
                 MobileNumber,
                 Landline,
                 Email
                 from Customer where CustomerID=?
                 """
        id = (id,)
        cursor.execute(sql, id)
        customer = cursor.fetchone()
        return customer

if __name__ == "__main__":
    customers = select_all_customers(db_name)
    print(customers)
