import sqlite3

def update_customer_data_sql(db_name, Firstname, Lastname, company, street, town, post_code, mobile, landline, email, id):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = """update Customer set
                 Forename = ?
                 Surname = ?
                 Company = ?
                 Street = ?
                 Town = ?
                 PostCode = ?
                 MobileNumber = ?
                 Email = ?
                 Landline = ?
                 where CustomerID = ?
                 """
        data = (Firstname, Lastname, company, street, town, post_code, mobile, landline, email, id)
        db.execute(sql, data)
        db.commit()
