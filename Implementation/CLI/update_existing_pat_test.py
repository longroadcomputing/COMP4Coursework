import sqlite3

def update_pat_test_data_sql(db_name, values, id):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = """update PATtest set
                 TestDate=?
                 where PATtestID=?
                 """
        data = (values, id)
        db.execute(sql, data)
        db.commit()
