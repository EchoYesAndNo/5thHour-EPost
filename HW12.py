#Name: Echo Post
#Class: 5th Hour
#Assignment: HW12


#1. Print Hello World!
print("Hello World")
#2. Create three different boolean variables named wifi, login, and admin.
Wifi = True
Login = True
Admin = False
#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.
times_logged_in = 99
#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".
if Wifi == True:
    if Login == True:
        if Admin == True:
            print("Welcome User")
            times_logged_in += 1
        else:
            print("Admin is missing")
    else:
        print("Login is missing")
else:
    print("Wifi is missing")
