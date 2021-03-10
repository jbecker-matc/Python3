#!/usr/bin/env python3

print ("Name: Jon Becker")

password_database = {
"Username":"dnedry",
"Password":"please"
}

command_database = {
"a. reboot":"OK. I will reboot all park systems.",
"b. shutdown":"OK. I will shut down all park systems.",
"c. done":"I hate all this hacker stuff."
}

#Used to break out of while loop
white_rabbit_object = 0

#Used to count the number of failed authentication attempts
counter = 0

input_user = input("Username: ")
input_password = input("Password: ")

while white_rabbit_object == 0 and counter < 3:

     if input_user == password_database["Username"] and input_password == password_database["Password"]:
          white_rabbit_object += 1
          print ("Hi, Dennis. You're still the best hacker in Jurassic Park.")

          input_command = input(
"Please enter a command: ""\n"
"a. reboot""\n"
"b. shutdown""\n"
"c. done""\n"
"> "
 )
          if input_command == "a":
               print (command_database["a. reboot"])
          if input_command == "b":
               print (command_database["b. shutdown"])
          if input_command == "c":
               print (command_database["c. done"])
          else:
               print ("The Lysine Contingency has been put into effect.")

     elif input_user != password_database["Username"] or input_password != password_database["Password"]:
          counter += 1
          if counter == 3:
               print ("You didn't say the magic word""\n" * 25)
               quit()
          elif counter < 3:
               print (f"You didn't say the magic word. {counter}")
     input_user = input("Username: ")
     input_password = input("Password: ")
