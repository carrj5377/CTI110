# CTI 110
# P5LAB2 - Functions
# Julian Carr
# 11/2/23
#
# First, print a table of squares

def main():
  print("P5T2 - Squares")
  print("number\tnumber squared")
  for num in range(1,11):
    num_squared = square(num)
    print_row(num, num_squared)
    
# square() is a value-returning function
def square(number):
  """Input : a number
  output: the number squared"""
  square = number * number
  return square

# print_row() is a void function
def print_row(num, num_squared):
  print(num, "\t\t", num_squared)




main()