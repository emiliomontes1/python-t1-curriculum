fruits = ["apple","banana","cherry"]

            
if "apple" in fruits:
    print("Found apple")
else:
    print("Apple not found.")


found = False 
for i in range(len(fruits)):    # Looping through the list
    if fruits[i] == "apple":    # Checking if the current item is apple
        found = True            # Mark as found
        break                   # Exit the loop since we found apple
if found == True:
    print("Found apple at index", index)
else:
    print("No apples in list.")



