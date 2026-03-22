age = int(input("How old are you?"))
has_ticket = input("Do you have a movie ticket?(yes/no)")

if age >= 13 and has_ticket == "yes":# AND: means both conditions must be true for the code inside the if statement to run
    print("You can enter the PG-13 movie.")
else:
    print("You cannot enter the PG-13 movie.")
print("Movie check complete.")

has_pass = input("Do you have a pass?(yes/no)")
has_coins = input("Do you have coins to pay?(yes/no)")
if has_pass == "yes" or has_coins == "yes":# OR: at least one condition must be true for our code inside the if statement to run
    print("You can ride the bus.")
else:
    print("You cannot ride the bus.")
print("Bus check complete.")

has_fun = input("Did you have fun on the link?(yes/no)")
has_water = input("Do you need water?(yes/no)")
if has_water == "yes" and has_fun == "no":
    print("I'm sorry you did not have fun. Drink some water!")
elif has_fun == "yes" and has_water == "yes":
    print("I'm glad you had fun! You must be tired so drink up!")
elif has_fun == "no" and has_water == "no":
    print("Too bad. Let us go home to drink.")
else:
    print("Oh well.")



homework_done = input("Did you do your homework?(yes/no)")
if not homework_done == "yes":# NOT: Flips False to True and True to False
    print("Go finish your homework.")
else:
    print("Good job! You're all done.")
print("Homework check complete.")

# You can combine multiple logical operators
is_raining = input("Is it raining? (yes/no)")
has_umbrella = input("Do you have an umbrella? (yes/no)")

if is_raining == "yes" and not has_umbrella == "yes":# Order of operations: first not, then and, then or.
    print("Stay inside. You might get wet!")
elif is_raining == "yes" and has_umbrella == "yes":
    print("You're ready to go outside.")
else:
    print("No rain! You can go outside.")


got_job = input("Are you employed?(yes/no)")
got_home = input("Do you have a home?(yes/no)")
got_money = input("Are you broke?(yes/no)")
got_family = input("Are you single?(yes/no)")
got_computer = input("Do you have your windows computer?(yes/no)")
if got_job == "yes" and got_home == "yes":
    print("You're kind of ready for a happy life.")
elif got_job == "yes" and not got_home == "yes":
    print("You better get a home soon!")
elif got_job == "yes" and got_family == "yes" and got_home =="yes":
    print("You're ready to have a happy life.")
else:
    print("The crystal ball is clueless.")

my_weight = int(input("What is your weight?"))
if my_weight >= 150:
    print("You are extremely obese")
elif my_weight >= 100:
    print("You are overweight")  
elif my_weight <= 100:
    print("You are a wuss.") 
else:
    print("You are surely an adult.")

    
