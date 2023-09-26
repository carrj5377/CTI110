""" CTI 110
P3T2 - choices and Menus
Carr Julian
9/26/23
"""

# The most simple program, with main()
def main():
  # print the menu
  print("-"*10, 'Main Menu', "-"*10)

  print("1. video game")
  print("2. Consoles")
  print("3. graphics card")
  print("-"*30)
  
  print("Your choice? ", end="")
  choice = int(input())
  print("you chose:", choice)

  # branch (if) on choice
  if choice == 1:
    option_1()
  elif choice == 2:
    option_2()
  elif choice == 3:
    option_3()
  else:
    print("Sorry, that's not an option.")
  



def option_1():
  print("Video games")
  print()
  print("We have Baldurs gate 3, Revanant 2, or starfield")
  print("Would you like one of these games")
  print()
  game = input() 
  if game == "BG3":
    print("Good choice i'll bring up for you now")
  elif game == "Rev 2":
    print("I heard that one is good,i'll bring it up for you now")
  elif game == ("Starfield"):
    print("Here you go")
  else:
    print("Out of stock")
    
def option_2():
  print("Consoles")
  print()
  print("We have The Playstion 5, xbox series X, Nintendo switch")
  print("Whats console would you like? ")
  
  Console = input()
  if Console == "PS5":
    print("I'll bring that right out for you")
  elif Console == 'Xbox series X':
    print("alright, i'll get that for you")
  elif Console == "Nintendo switch":
    print('Great I will be right back with that')
  else:
    print("we do not that, sorry")

def option_3():
  print("Graphics Card")
  print()
  print("We have the 30's series")
  print("3070, 3080, 3080ti, and 3090")
  print("What would you like?")
  Card = input()
  if Card == "3070":
    print("Thats what i have , I'll get that for you")
  elif Card == "3080":
    print('Great I will be right back with that')
  elif Card == "3080ti":
    print("Great I will be right out with it")
  elif Card == ("3090"):
    print("Nice choice ill get that for you")
  else:
    print("We do not have those yet")
    
  
  
  

# Start the program
main()          