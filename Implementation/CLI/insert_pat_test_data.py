import sqlite3

def get_test_date():
    valid = False
    while not valid:
        test_date = input("Please enter the date of the PAT test(dd/mm/yyyy): ")
        if len(test_date) > 0 and ["/", "-"] in test_date:
            valid = True
        else:
            valid = False
            print("Please enter a valid test date")
    return test_date

def insert_new_pat_test(db_name, test_date):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = """insert into PATtest(
                 TestDate)
                 values (?)
                 """
        data = (test_date,)
        cursor.execute(sql,data)
        db.commit()

if __name__ == "__main__":
    insert_new_pat_test(db_name, test_date)
