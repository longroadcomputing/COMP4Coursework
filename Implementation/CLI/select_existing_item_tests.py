import sqlite3

def select_all_item_tests(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("""select
                          ItemTestID, 
                          ItemTest.PATtestNotes,
                          ItemTest.Leakage,
                          ItemTest.TestResult,
                          Item.ItemName,
                          Item.ItemClass,
                          Item.FuseRating,
                          PATtest.PATtestID
                          from ItemTest, Item, PATtest
                          where ItemTest.ItemID = Item.ItemID
                          """)
        item_tests = cursor.fetchall()
        return item_tests

def select_single_item_test(db_name, id):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        id = (id,)
        cursor.execute("""select
                          ItemTestID,
                          ItemTest.PATtestNotes,
                          ItemTest.Leakage,
                          ItemTest.TestResult,
                          Item.ItemName,
                          Item.ItemClass,
                          Item.FuseRating,
                          PATtest.PATtestID
                          from ItemTest, Item, PATtest
                          where ItemTestID = ? and ItemTest.ItemID = Item.ItemID
                          """,id)
        item_test = cursor.fetchone()
        return item_test

if __name__ == "__main__":
    pat_tests = select_all_item_tests(db_name)
