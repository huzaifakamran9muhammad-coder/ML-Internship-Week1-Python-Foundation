username = "admin"
password = "12345"

user = input("Username: ")
pwd = input("Password: ")

if user == username and pwd == password:
    print("Login Successful")
else:
    print("Invalid Credentials")
