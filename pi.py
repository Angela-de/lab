import math
radius = float (input("radius of a sphere: "))
sa = 4 * math.pi * radius * radius
volume = (4 / 3) * math.pi* radius * radius *radius

print("\n surface area of a sphere = " + str(sa))
print("\n volume of a sphere = %.2f" %volume)