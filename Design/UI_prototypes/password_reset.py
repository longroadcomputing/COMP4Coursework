def read_password():
    with open("password_data_file.pw", "r", encoding="UTF-8") as pf:
        password = pf.read().replace('\n','')
        pf.close()
        return password

def update_password(password):
    with open("password_data_file.pw", "w", encoding="UTF-8") as pf:
        pf.write("{0}".format(password))
        pf.close()

if __name__ == "__main__":
    read_password()
