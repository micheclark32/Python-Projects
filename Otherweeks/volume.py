from datetime import datetime
from typing import final

width = float(input("Enter the width of the tire in mm: "))
aspect_ratio = float(input("Enter in the aspect ratio: "))
diameter = float(input("Enter the diameter: "))
pie = 22/7
current_date_and_time = datetime.now()

volume1 = pie*width**2 * aspect_ratio
volume2 = width * aspect_ratio + 2540 * diameter
volume3 = volume1 * volume2
final_vol = volume3 / 10000000000
print(f"The approximate volume is {final_vol:.2f}")

answer = open("volume.txt", 'a')
current_date_and_time = str(current_date_and_time)
width = repr(width)
aspect_ratio = repr(aspect_ratio)
diameter = repr(diameter)
final_vol = repr(final_vol)

answer.write("DATE/TIME: " + current_date_and_time + " " + "WIDTH: " + width + " " +
             "ASPECT: " + aspect_ratio + " " + "DIAMETER: " + diameter + " " + "VOLUME: " + final_vol)
answer.close

# Open and read file
answer = open("volume.txt", "r")
print(answer.read())
