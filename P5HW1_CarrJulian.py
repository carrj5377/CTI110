# CTI-110 
# P5HW1 - Math Quiz
# Julian Carr
# 10/31/2023
"""Let the user choose between 3 options on a menu adding, subtracting, and exit. 
use random numbers and ask for user input and when user inputs 3 end program.
"""

import random




def main_menu():
  print("Main Menu")
  print("1. Adding Random Numbers")
  print("2. Subtracting Random Numbers")
  print("3. Exit")
  choice = input("Please choose on of the menu options: ")
  if choice == '1':
   adding()
  elif choice == '2':
    subtracting()
  elif choice == '3':
    exit()
  else:
    print("That is not a valid option try again")
    return main_menu()

def adding():
  # use different random numbers each question
  numb1 = random.randint(1, 100)
  numb2 = random.randint(1, 100)
  print ("", numb1)
  print("+")
  print("", numb2)
  addition = numb1 + numb2
  answer = int(input( ))
  if answer == addition:
    print("Correct!")
    
    keep_going = input("1. Keep going  2.Main menu  3.Exit:  ")
    if keep_going == "1":
      adding()
    elif keep_going == '2':
      main_menu()
    elif keep_going == '3':
      exit()
  while answer != addition:
    if answer > addition:
      print("Incorrect!")
      print("Answer to high")
      print("Try again")
      answer = int(input())
    elif answer < addition:
      print("Incorrect")
      print("Answer to Low")
      print("Try again")
      answer = int(input())
  print("That's Correct")
  try_again = input("Would You like to keep doing addition? Y/N. ")
  if try_again == "Y":
    adding()
  elif try_again == "N":
    main_menu()

def subtracting():
  # use different random numbers each question
  numb1 = random.randint(1, 100)
  numb2 = random.randint(1, 100)
  print ("", numb1)
  print("-")
  print("",  numb2)
  subtraction = numb1 - numb2
  answer = int(input())
  if answer == subtraction:
    print("Correct!")
    
    keep_going = input("1. Keep going  2.Main menu  3.Exit: ")
    if keep_going == "1":
      subtracting()
    elif keep_going == '2':
      main_menu()
    elif keep_going == '3':
      exit()
  while answer != subtraction:
      if answer > subtraction:
        print("Incorrect!")
        print("Answer to high")
        print("Try again")
        answer = int(input())
      elif answer < subtraction:
        print("Incorrect")
        print("Answer to Low")
        print("Try again")
        answer = int(input())
  print("That's Correct")
  try_again = input("Would You like to keep doing Subtraction? Y/N. ")
  if try_again == "Y":
      subtracting()
  elif try_again == "N":
      main_menu()
def exit():
  print("THANKS FOR PLAYING!!")
  
    
main_menu()
