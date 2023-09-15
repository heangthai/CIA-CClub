

login = 1
while login == 1:
    choice = input("Do you want to sign up or log in? s/l ")

    if choice == "s":
     new_username = input("Username: ")
     new_password = input("Password: ")
     tries = 1
     login = 0
    elif choice == "l":
     print("You haven't sign up yet!")
     login = 1
 
while tries <= 3:
    username = input("What is your username? ")
    tries += 1
    
    if username == new_username:
     password = input("What is yours password? ")
     if password == new_password:
      print("Sucessful login")
      tries += 100
     elif password != new_password:
      print("Error, incorrect password!")
 
    elif username != new_username:
     print("Error, wrong username!")
     tries += 1

