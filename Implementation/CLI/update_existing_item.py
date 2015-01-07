import sqlite3

def update_item_data_sql(db_name, name, value, loan_rate, item_class, fuse_rating, item_type_id, location_id, id):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = """update Item set
                 ItemName = ?
                 ItemValue = ?
                 LoanRate = ?
                 ItemClass = ?
                 FuseRating = ?
                 ItemTypeID = ?
                 Location = ?
                 where ItemID = ?
                 """
        data = (name, value, loan_rate, item_class, fuse_rating, item_type_id, location_id, id)
        db.execute(sql, data)
        db.commit()
