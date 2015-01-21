import sqlite3

def update_loann_data_sql(db_name, customer_id, start_date, loan_length, id):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = """update Loan set
                 StartDate = ?
                 LoanLength = ?
                 where LoanID = ?
                 """
        data = (customer_id, start_date, loan_length, id)
        db.execute(sql, data)
        db.commit()
