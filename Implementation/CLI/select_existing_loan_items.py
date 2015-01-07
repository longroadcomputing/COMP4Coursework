import sqlite3

def select_all_loan_items(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("""select
                          LoanItem.LoanItemID,
                          LoanItem.LoanID,
                          LoanItem.Quantity,
                          Item.ItemName,
                          Item.LoanRate
                          from LoanItem, Item
                          where LoanItem.ItemID = Item.ItemID
                          """)
        loans = cursor.fetchall()
        return loans

def select_loan_item(db_name, id):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = """select
                 LoanItem.LoanItemID,
                 LoanItem.LoanID,
                 LoanItem.Quantity,
                 Item.ItemName,
                 Item.LoanRate
                 from LoanItem, Item
                 where LoanItemID=? and LoanItem.ItemID = Item.ItemID
                 """
        id = (id,)
        cursor.execute(sql, id)
        loan = cursor.fetchone()
        return loan

if __name__ == "__main__":
    loans = select_all_loans(db_name)
    print(customers)
