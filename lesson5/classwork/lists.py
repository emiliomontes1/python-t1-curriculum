#A list is apple, banana, orange, etc..

            #1      #2      #3  
fruits = ["apple","banana","orange"]
#         0          1           2
#The computer counts from 0 we count from 1
#Lists use braces
y = len(fruits)#len is the same as length. The length of fruits
print(fruits[0])
c = y #This assigns c to the list fruits,variable y
# list starts at 0 when accessing elements but starts at 1 when finding the length
#functions of a list--------------------------
fruits.append("mushroom") # .append will add mushroom in this case to the end of the list # Append just means add to the end
fruits.insert( 2, "carrot")# .insert will insert the specified thing into the specified index aka position
print(fruits)
fruits.remove("carrot")#.remove removes the first value of the thing
c = fruits.pop()# I think pop makes a copy of the last element you can also pop the specified index
print(c)
b = fruits.pop(2)
m = fruits.index("apple")
g = fruits.count("mushroom")
print(fruits)