# this is a really simple login form run in the command line 
# feel free to add or remove anything you want!

import time 

print("Welcome to this simple login form") 
start = input("Do You Want to Continue (y/n)? ")
time.sleep(0.6)

if start.lower() != "y":
    print('[-] exiting...')
    quit()

login = 'admin'
passwrd = 'password' 

loginI = input("Please Enter your Username: ")
loginI = input("Please Enter your Password: ")

# checks if username and password are valid
if login.lower() == 'admin':
    login = input("Login correct, Are you sure you would like to continue(y/n)? ")
else: 
    print("Wrong username and/or password!")
    quit()

if passwrd.lower() == 'password':
    print("Password correct!")
    print("yay you made it too the end!")
else:
    print("Password incorrect!")
    print("oops that was incorrect Try running this program again...")
    quit()

