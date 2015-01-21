import sqlite3

def delete_selected_item_test(db_name, id):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = """delete from ItemTest where Itemtest.PATtestID = ?"""
        id = (id,)
        cursor.execute(sql,id)
        db.commit()
