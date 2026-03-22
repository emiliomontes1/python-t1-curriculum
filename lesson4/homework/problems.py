# Problem 1
# Ask user for two test scores.
# If BOTH scores are at least 50, print "You passed both!"
# Otherwise, print "You failed at least one."
test_score = int(input("Give me a test score."))
test_score2 = int(input("Give me your second test score."))
if (test_score) and (test_score2)>= 50:
    print("You passed both!")
else:
    print("You failed at least one.")


# Problem 2
# Ask user if they brought lunch and water (yes/no).
# If they brought lunch OR water, print "You're somewhat ready."
# If they brought both, print "You're fully ready!"
# If they brought neither, print "You're not ready."
has_lunch = input("Did you bring lunch?(yes/no)")
has_water = input("Did you bring water?(yes/no)")
if has_lunch == "yes" or has_water == "yes":
    print("You are somewhat ready.")
elif has_lunch == "yes" and has_water == "yes":
    print("You are fully ready!")
else:
    print("You are not ready.")

# Problem 3
# Ask user to enter a number.
# If the number is NOT between 1 and 10 (inclusive), print "Out of range."
# Otherwise, print "In range."



# Problem 4
# Generate a random number between 1 and 10.
# Ask the user to guess.
# If the guess is right AND the number is even, print "Even match!"
# Else if guess is right OR number is 5, print "Nice try!"
# Otherwise, print "Nope."



# Problem 5
# Ask the user for two numbers.
# If one is divisible by 5 AND the other is NOT divisible by 2, print "Interesting pair!"
# Otherwise, print "Plain pair."