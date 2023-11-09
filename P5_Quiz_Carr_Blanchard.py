"""
CTI 110
M5LAB2 - Complete a Program
Julian carr
Ian Blanchard
11/9/23

The program will ask the user to enter the width and length of a rectangle. It will then calculate the area. Finally it will display all three values in well formatted output.

The program will contain the following functions as well as main().

getLength - Asks the user to enter a rectangle's length, and return that value as a float.

getWidth - Asks the user to enter a rectangle's width, and return that value as a float.

getArea - This function should take two arguments, length and width. It will calculate the area and return that value as a float.

displayData - This function should take three arguments, length, width, and area. It will then display these values as well formatted output. (Something like "The length is: 5".)
"""

def getLength():
   get_length = float(input('Enter the length: '))
   return get_length
    

def getWidth():
    get_width = float(input("Enter the width: "))
    return get_width

def getArea(length, width):
  area = length * width
  return area
  


def displayData(length, width, area):
  
    print(length)
    print(width)
    print(area)
    
def main():
  
    length = getLength()
    width = getWidth()
    area = getArea(length, width)
    displayData(length, width, area)

# start the program
main()