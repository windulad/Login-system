#Enter to the system
print("------WINDULA'S LOGIN SYSTEM------")

#Select an option, Login or Register
action = input("Enter your needed action; LOGIN = L , REGISTER = R : ")
str_action = str(action)
if str_action == "L":
    print("Login window opens...")
if str_action == "R":
    print("Register window opens...")

#Login pathway

#Enter data, email, password
print("Please enter your email and password")
old_email = input("Enter your email  : ")
old_password = input("Enter your password  :  ")

#Database
stored_email = "charithwinwindula@gmail.com"
stored_password = "password"

#Compare input with data in database
if stored_email == str(old_email) and stored_password == str(old_password):
    print("Your entered data are valid")
else:
    print("check your input")

#Login permision granted

#Register pathway

#Enter data, name, email, password, confirm password
print("Please enter your Name, Email, Password and Confirm Password")
new_name = input("Enter your Name  :  ")
new_email = input("Enter your Email  : ")
new_password = input("Enter your password  :  ")
new_password2 = input("Confirm your password  :  ")

#Check password accuracy
if new_password == new_password2:
    print("Two passwords match")
else:
    print("Two password do not match")

#Check for old records
if new_email == old_email and new_password == old_password:
    print("This user has registered before. Please Login")
else:
    print("Registration successful")

#Save and exit