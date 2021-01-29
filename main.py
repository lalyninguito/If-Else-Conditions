a = 200
b = 33

if(b > a):
  print("b is greater than a")
else:
  print("b is not greater than a")

# Write a conditional statement that evaluates if the user input is positive or negative

# a = 5000 is called hard coding because we as a coder specify what the number is as opposed to having the user decide

userInput = int(input("Please type in a number: "))

if(userInput > 0):
  print("Your number is positive")
elif(userInput == 0):
  print("Your number is 0")
else:
  print("Your number is negative")

# Ask the user for their age
# If they are younger than 13, tell them they can only watch PG/G movies
# If they are 13 and older, but younger than 17, they can only watch PG-13/PG/G movies
# If they are 17 and older, they can watch all movies

userAge = int(input("Please type in your age: "))

if(userAge < 13):
  print("You can only watch PG/G rated movies")
elif(13 <= userAge < 17):
  print("You can watch PG/G/PG-13 rated movies")
else:
  print("You can watch all the movies")

is_Hungry = False
is_Sleepy = False
if(is_Hungry == True):
  print("You should go eat")
if(is_Sleepy == True):
  print("You should go to sleep")
if(is_Sleepy == False):
  print("Wow you're well-rested")

# Ask the user for a number
# Tell the user if their number is even or odd

userNumber = int(input("Please input a number: "))
if(userNumber % 2 == 0):
  print("Your number is even")
else:
  print("Your number is odd")