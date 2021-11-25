#Select an option, Login or Register
action = input("SELECT : LOGIN = L / REGISTER = R  ")
str_action = str(action)

#Login input
if str_action == "L":
    print("LOGIN")
    old_email = input("Enter your email = ")
    old_password = input("Enter your password = ")

#Register input
if str_action == "R":
    print("REGISTER")
    new_name = input("Enter your name = ")
    new_email = input("Enter your email = ")
    new_password = input("Enter a password = ")
    new_data = "{} | {} | {}".format(new_name, new_email, new_password)

user_data = open("user.txt", "r+")
user_data.seek(0)
data = user_data.read(100)
if len(data) > 0 :
    user_data.write("\n")
user_data.write(new_data)
user_data.close()