er between 1 and 10 (inclusive).
# Ask the user to guess the number.
# Print "Correct!" if the guess matches the random number, else print "Try again!".
import random
r = random.randint(1,10)
user_input = input("gimme a number between 1 and 10:")
if user_input == r:
    print("Correct!")
else:
    print("Womp Womp. Try again!")


# Problem 4
# Ask the user for a positive integer.
# If the number is divisible by 2 and greater than 10, print "Big even number".
# Otherwise print "Number does not meet criteria".
user_input = input("give me a positive integer.")
if int(user_input)% 2 and user_input > 10:
    print("Big even number.")
else:
    print("Number does not meet criteria.")

# Problem 5
# Ask the user for two numbers.
# Print which number is larger.
# If the numbers are equal, print "Numbers are equal".

user_input = input("gimme 1 number")
user_input2 = input("gimme another number.")
if user_input > user_input2:
    print(user_input)
elif user_input2 > user_input:
# Problem 1
# Ask the user to enter a number.
# Print "Even" if the number is divisible by 2, otherwise print "Odd".
user_input = input("Give me a number:")
if int(user_input) % 2 == 0:
    print("Even")
else:
    print("Odd")


# Problem 2
# Ask the user for the day of the week (all lowercase).
# Print "Weekend" if the day is "saturday" or "sunday",
# else print "Weekday".
day = input("What day of the week is it?")
if day == "saturday" or day == "sunday":
    print("Weekend")
else:
    print("Weekday")


# Problem 3
# Generate a random numb    print(user_input2)
else:
    print("Numbers are equal")


