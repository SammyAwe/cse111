import math
import datetime


width = float(input("Enter the width of the tire in millimeters: "))
aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
diameter = float(input("Enter the diameter of the wheel in inches: "))
print()
#broke down my calculation in order to make it simpler
volumepart1 = math.pi * (width ** 2) * aspect_ratio
volumepart2 = width * aspect_ratio + 2540 * diameter
finalvolume = volumepart1 * volumepart2 / 10000000000
volume = round(finalvolume, 2)
print(f"The volume of space inside the tire is: {volume:.2f} liters.")
if 185 <= width <= 195 and 60 <= aspect_ratio <= 70 and 14<= diameter <= 17:
    price = 450
elif 205 <= width <= 225 and 50 <= aspect_ratio <= 65 and 15 <= diameter <= 18:
    price = 625
elif 365 <= width <= 505 and 70 <= aspect_ratio <= 90 and 24 <= diameter <= 32:
    750
else: 
    price = 0

purchase_inquiry = input("Do you want to buy tires with the dimensions that you entered?")
if purchase_inquiry.lower() == "yes":
    phone_number = (input("Enter your phone number we can use to reach you:"))
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    with open("volumes.txt", "a") as file:
       file.write(f"{phone_number}, {current_date}, {width}, {aspect_ratio}, {diameter}, {volume}, ${price}\n")
       print(f"Phone number stored successfully. The price for the tire size you chose is: ${price} Enjoy the rest of your day.")
else:
    print("Bye! Enjoy the rest of your day!")