import sqlite3

def delete_selected_pat_test(db_name, id):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = """delete from PATtest where PATtestID = ?
                 delete from ItemTest where Itemtest.PATtestID = ?"""
        id = (id, id)
        cursor.execute(sql,id)
        db.commit()
