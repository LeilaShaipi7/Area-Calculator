# Create a program that allows the user to enter 2 numbers representing the width and length of a rectangle. The program calculates and displays the area of the rectangle.

length1 = int(input("Enter a number "))
width1 = int(input("Enter a number "))
print(length1 * width1)


# BONUS PROGRAMS >>>>

#PerimeterCalc
#Create a program that allows the user to enter 2 numbers representing the width and length of a rectangle. The program calculates and displays the perimeter of the rectangle. 

length2 = int(input("Enter a number "))
width2 = int(input("Enter a number "))
print(2 * (length2 + width2))

#Restaurant Tip Calculator 
#Create a program that allows the user to enter the price of a meal at a restaurant. The program calculates the amount of the tip to be paid at 20%. The tip and total price are then displayed separately.

price = int(input("Enter price "))
tip = price/100*20
print(tip)
print(price + tip)

#Volume and Surface Calc 
#Create a program that allows the user to enter 3 numbers representing the height, width and length of a cuboid. The program calculates and displays the volume and total surface area of the cuboid. 

length3 = int(input("Enter length "))
width3 = int(input("Enter width "))
height = int(input("Enter height "))
volume = length3 * width3 * height
print(volume)
SA = (length3*width3) + (length3*height) + (height*width3)
TSA = SA*2
print(TSA)
