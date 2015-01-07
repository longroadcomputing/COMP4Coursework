import sqlite3

def delete_selected_customer(db_name, id):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = """delete from Customer where CustomerID = ?"""
        id = (id,)
        cursor.execute(sql,id)
        db.commit

if __name__ == "__main__":
    delete_selected_customer(id)
