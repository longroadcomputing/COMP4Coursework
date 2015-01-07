import sqlite3

def delete_selected_customer_loan(id):
    with sqlite3.connect("C3_media_database.db") as db:
        cursor = db.cursor()
        sql = """delete from Loan where LoanID = ?
                 delete from LoanItem where LoanItem.LoanID = ?"""
        id = (id, id)
        cursor.execute(sql,id)
        db.commit

if __name__ == "__main__":
    data = ("Latte",)
    delete_selected_customer_loan(id)
