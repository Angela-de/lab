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