correct_username = "admin"
correct_password = "1234"

attempt = 0

while attempt < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login Successful")
        break
    else:
        print("Wrong username or password")
        attempt += 1

if attempt == 3:
    print("Account Locked")