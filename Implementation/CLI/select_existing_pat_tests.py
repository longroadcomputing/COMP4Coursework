import sqlite3

def select_all_pat_tests(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("""select
                          PATtestID,
                          TestDate
                          from PATtest
                          """)
        pat_tests = cursor.fetchall()
        return pat_tests

def select_single_pat_test(db_name, id):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        id = (id,)
        cursor.execute("""select
                          PATtestID,
                          TestDate
                          from PATtest where PATtestID = ?
                          """,id)
        pat_test = cursor.fetchone(db_name)
        return pat_test

if __name__ == "__main__":
    pat_tests = select_all_pat_tests(db_name)
