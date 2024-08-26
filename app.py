a = 2
b = 3
print (a+b)

favorite_number = 42
print("My favorite number is " + str(favorite_number))
print(f"My favorite number is {favorite_number}")

#boolean
is_python_fun = True
is_python_boring = False
print(f"Is Python fun? {is_python_fun}")
print(f"Is Python boring? {is_python_boring}")


#Control Flow
temperature = 30
if temperature > 25:
    print("It's hot outside! Wear Shorts.")
elif temperature > 15:
    print("It's warm. Maybe wear a light jacket")
else:
    print("Brrrr! It's cold. Bundle up!")

#Loops
# Includes for loops and while loops
#for loops meant for a scenario where you have a definite number of iterations that you want to happen
 
for i in range(7):
    print(f"This is a car {i}")

#while loop an event will be iterated until a certain condition is met

CountDown = 5
while CountDown > 0:
    print(f"Count Down: {CountDown}")
    CountDown -= 1
print("Blast Off!")

#Modules
#In-built modules comes already packed in python you can jaz call it in order to use e.g

import math 

result = math.sqrt(16)
print(f"The square root of 16 is: {result}")

#Customized module
#User created module. Created by the developer

import Salamu

print(Salamu.greet("Racer"))



