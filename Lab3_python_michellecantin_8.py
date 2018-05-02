# EIGHT
# The formula: Area = pi * radius Exponent 2

# Prompts the user to enter the radius of the circle and returns it as a float
r = float(input("What is the radius of the circle? "))

# Imports math to later call the pi value
import math

# Calculates the area of the circle and turns it into a float
area = float((math.pi * r) ** 2)

# Takes the float for the area of the circle, keeps 2 decimals and turns it into a string
area_str = str(round(area,2))

# Tells the user what the area of the circle is
print("The exact area of the circle is " + area_str + "!")
