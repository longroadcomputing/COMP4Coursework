import sqlite3

def delete_selected_item_loan(db_name, id):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = """delete from ItemLoan where ItemLoanID = ??"""
        id = (id, id)
        cursor.execute(sql,id)
        db.commit()
