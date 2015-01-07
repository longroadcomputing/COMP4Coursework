import sqlite3

def update_loan_item_data_sql(db_name, loan_id, item_id, quantity, id):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = """update LoanItem set
                 Quantity = ?
                 where LoanItemID = ?
                 """
        data = (loan_id, item_id, quantity, id)
        db.execute(sql, data)
        db.commit()
