from math import pi

while True:
    r = float(input("Input the radius of a circle: "))
    area = pi * r ** 2
    print("the area of the circle with radius " + str(r) + " is " + str(area))

    continue_calculator = input ("Would you like to continue? yes/no: ").lower()
    if continue_calculator != 'yes':
        print ("Thank you for playing!")
        break
