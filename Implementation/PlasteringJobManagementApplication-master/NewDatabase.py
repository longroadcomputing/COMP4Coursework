import sqlite3
def create_table(db_name,table_name,sql):
		
		with sqlite3.connect(db_name) as db:
			cursor = db.cursor()
			cursor.execute("select name from sqlite_master where name=?",(table_name,))
			result = cursor.fetchall()
			if len(result) == 1:
				pass
			else:
				cursor.execute(sql)
				db.commit()

def referential_integrity(db_name):
	with sqlite3.connect(db_name) as db:
		cursor = db.cursor()
		cursor.execute("PRAGMA foreign_keys = ON")
		db.commit()

def create_client_table(db_name):
	
	sql = """CREATE TABLE Client(
	ClientID integer,
	ClientTitle text,
	ClientFirstName real,
	ClientSurname text,
	ClientAddrLine1 text,
	ClientAddrLine2 text,
	ClientAddrLine3 text,
	ClientAddrLine4 text,
	ClientEmail text,
	ClientPhoneNumber text,
	Primary Key(ClientID));"""

	create_table(db_name,"Client",sql)
		

def create_plasterer_table(db_name):

	sql = """CREATE TABLE Plasterer(
	PlastererID integer,
	PlastererTitle text,
	PlastererFirstName real,
	PlastererSurname text,
	PlastererAddrLine1 text,
	PlastererAddrLine2 text,
	PlastererAddrLine3 text,
	PlastererAddrLine4 text,
	PlastererEmail text,
	PlastererPhoneNumber text,
	PlastererDailyRate real,
	Primary Key(PlastererID));"""

	create_table(db_name,"Plasterer",sql)



def create_material_table(db_name):

	sql = """CREATE TABLE Material(
	MaterialID integer,
	MaterialName text,
	MaterialPrice real,
	Primary Key(MaterialID));"""

	create_table(db_name,"Material",sql)


def create_job_table(db_name):

	sql = """CREATE TABLE Job(
	JobID integer,
	ClientID integer,
	PlastererID integer,
	InvoiceID integer,
	JobDescription text,
	JobAddrLine1 text,
	JobAddrLine2 text,
	JobAddrLine3 text,
	JobAddrLine4 text,
	JobDaysWorked integer,
	JobComplete text,
	Primary Key(JobID),
	Foreign Key (ClientID) references Job(JobID),
	Foreign Key (PlastererID) references Plasterer(PlastererID),
	Foreign Key (InvoiceID) references Invoice(InvoiceID));"""

	create_table(db_name,"Job",sql)


def create_invoice_table(db_name):

	sql = """CREATE TABLE Invoice(
	InvoiceID integer,
	JobID integer,
	InvoiceAmountPreTax real,
	InvoiceAmountAfterTax real,
	InvoiceReceived integer,
	InvoiceDate text,
	InvoiceText text,
	InvoicePaid integer,
	Primary Key(InvoiceID),
	Foreign Key (JobID) references Job(JobID));"""

	create_table(db_name,"Invoice",sql)

				
def create_appointment_table(db_name):


	sql = """CREATE TABLE Appointment(
	AppointmentID integer,
	JobID text,
	AppointmentDate text,
	AppointmentTime text,
	Primary Key(AppointmentID),
	Foreign Key(JobID) references Job(JobID));"""


	create_table(db_name,"Appointment",sql)






def create_jobMaterials_table(db_name):

	sql = """CREATE TABLE JobMaterials(
	JobMaterialsID integer,
	JobID integer,
	MaterialID integer,
	JobMaterialsQuantity integer,
	Primary Key(JobMaterialsID),
	Foreign Key(JobID) references Job(JobID),
	Foreign Key(MaterialID) references Material(MaterialID));"""


	create_table(db_name,"JobMaterials",sql)

def create_db(db_name):

	populate_db(db_name)
	referential_integrity(db_name)

	return True

def populate_db(db_name):
	
	
	create_client_table(db_name)
	create_plasterer_table(db_name)
	create_material_table(db_name)
	create_job_table(db_name)
	create_invoice_table(db_name)
	create_appointment_table(db_name)
	create_jobMaterials_table(db_name)

	


if __name__ == "__main__":

	create_db("Database.db")
