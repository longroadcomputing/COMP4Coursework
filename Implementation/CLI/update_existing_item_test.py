import sqlite3

def update_item_data_sql(db_name, item_id, pat_test_id, test_used, leakage, test_result, id):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = """update Item set
                 ItemName = ?,
                 ItemValue = ?,
                 LoanRate = ?,
                 ItemClass = ?,
                 FuseRating = ?,
                 ItemTypeID = ?,
                 LocationID = ?
                 where ItemID = ?
                 """
        data = (item_id, pat_test_id, test_used, leakage, test_result, id)
        db.execute(sql, data)
        db.commit()
