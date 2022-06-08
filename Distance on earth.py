# Create a program where you enter the latitudes and longitudes of 2 points on earth in degrees. The result should be the distance between them in km.
# For lat1, long1 and lat2, long2 distance is: distance = 6371.01(Average radius of earth in km)*arccos(sin(lat1)*sin(lat2)+cos(lat1)*cos(long1-long2))
# You need to convert input from degrees in radians as Python's trigonometric functions operate in radians

import math

pi = math.pi


lat1 = float(input("Enter latitide 1: "))
long1 = float(input("Enter longitude 1: "))

lat2 = float(input("Enter latitide 2: "))
long2 = float(input("Enter longitude 2: "))

# Convert degrees to radians
lati1 = lat1 * (pi/180)
longi1 = long1 * (pi/180)
lati2 = lat2 * (pi/180)
longi2 = long2 * (pi/180)

# Calculate Distance
distance = 6371.01 * math.acos(math.sin(lati1)*math.sin(lati2) + math.cos(lati1)*math.cos(longi1-longi2))

print(f'The distance between the two points is {distance: .1f}')