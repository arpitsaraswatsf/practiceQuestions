# Login System with Maximum 3 Attempts

correct_username = "admin"
correct_password = "1234"

attempts = 0
max_attempts = 3

while attempts < max_attempts:
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == correct_username and password == correct_password:
        print("Login Successful! Welcome.")
        break
    else:
        attempts += 1
        print("Invalid Username or Password.")
        print("Attempts left:", max_attempts - attempts)

if attempts == max_attempts:
    print("Account Locked! Maximum login attempts exceeded.")