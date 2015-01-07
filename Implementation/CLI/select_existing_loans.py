import sqlite3

def select_all_loans(db_name):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        cursor.execute("""select
                          Loan.LoanID,
                          Loan.StartDate,
                          Loan.LoanLength,
                          Customer.CustomerID,
                          Customer.Company
                          from Loan, Customer
                          where Loan.CustomerID = Customer.CustomerID
                          """)
        loans = cursor.fetchall()
        return loans

def select_loan(db_name, id):
    with sqlite3.connect(db_name) as db:
        cursor = db.cursor()
        sql = """select
                 Loan.LoanID,
                 Loan.StartDate,
                 Loan.LoanLength,
                 Customer.CustomerID,
                 Customer.Company
                 from Loan, Customer
                 where LoanID=?
                 """
        id = (id,)
        cursor.execute(sql, id)
        loan = cursor.fetchone()
        return loan

if __name__ == "__main__":
    loans = select_all_loans(db_name)
    print(customers)
