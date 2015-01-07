import sqlite3

def delete_selected_item(db_name, id):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = """delete from Item where ItemID = ?"""
        id = (id,)
        cursor.execute(sql,id)
        db.commit()

def delete_selected_item_types(db_name, id):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = """delete from ItemType
                 where ItemTypeID = ?"""
        id = (id,)
        cursor.execute(sql,id)
        db.commit()

def delete_selected_location(db_name, id):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = """delete from Location
                 where LocationID = ?"""
        id = (id,)
        cursor.execute(sql,id)
        db.commit()
