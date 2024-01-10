import math

width = float(input("Enter the width of the tire in millimeters: "))
aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
diameter = float(input("Enter the diameter of the wheel in inches: "))
print()
#broke down my calculation in order to make it simpler
volumepart1 = (math.pi * (width ** 2) * aspect_ratio)
volumepart2 = width * aspect_ratio + 2540 * diameter
finalvolume = volumepart1 * volumepart2 / 10000000000



print(f"The volume of space inside the tire is: {finalvolume:.2f} liters")