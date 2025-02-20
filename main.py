import math

unit=input("what do you have, radius or diameter? ")

if unit == "radius":
      r = float(input("what is radius: "))
      Area = round((math.pi * pow(r, 2)), 2)
elif unit == "diameter":
      d = float(input("Enter is diameter: "))
      r=d/2
      Area = round((math.pi * pow(r, 2)), 2)
else:
      print("Wrong input")

