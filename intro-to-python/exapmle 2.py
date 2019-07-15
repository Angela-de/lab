# converting 32 degrees to radian

import math
degree = float (input("Input degree: "))
radian = degree*(math.pi/180)
print(radian)
PI = 3.14
radius = float (input("radius of a sphere: "))
sa = 4 * PI * radius * radius
volume = (4 / 3) * PI * radius * radius *radius

print("\n surface area of a sphere = " + str(sa))
print("\n volume of a sphere = %.2f" %volume)

def add(x, y):
   return x + y
# This function subtracts two numbers 
def subtract(x, y):
   return x - y
# This function multiplies two numbers
def multiply(x, y):
   return x * y
# This function divides two numbers
def divide(x, y):
   return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
# Take input from the user 
choice = input("Enter choice(1/2/3/4):")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")