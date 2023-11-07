# CTI 110
# P5LAB1 - CYOA
# name
# date
# Feel free to fork this REPL and make changes.

# first function: main_menu().

from typing import Generator


def main_menu():
    print("Main Menu")
    print("You're in front of a spooky old house...")
    print("Do you:")
    print("1. Try the front door")
    print("2. Sneak around back")
    print("3. Forget it and go home")
    print("4. [Quit]")
    choice = input("Choose: ")
    if choice == '1':
        choice_front_door()
    elif choice == '2':
        # Call choice 2 here (You can add the corresponding function)
        choice_back_door()
    elif choice == '3':
        # Call choice 3 here (You can add the corresponding function)
        Give_up()
    elif choice == '4':
        print("Ok, quitting game")
        return
    else:
        print("That's not a valid choice, please try again.")
        main_menu()

# now we have the choice functions. Feel free to add more.
def choice_front_door():
    print("Try the front door.")
    print("It's locked.")
    print("Do you:")
    print("1. Check around back")
    print("2. Give up and go home")
    choice = input("Choose: ")
    if choice == '1':
        choice_back_door()
    elif choice == '2':
        Give_up()
    else:
        print("You have to choose...")
        choice_front_door()

def choice_back_door():
    print("You see a door around back.")
    print("Do you:")
    print("1. Try to open door")
    print("2. Lockpick door")
    print("3. Walk away")
    choice = input("Choose: ")
    if choice == '1':
      print("The door opens suprisingly easy. You walk in and the door closes")
      inside()
    elif choice == '2':
      print("Your lockpicking skill is not high enough. try again!")
      choice_back_door()
    else:
      print("You took to long to choose and fear kicked in you ran. Try again!")
      choice_back_door()
      
def inside():
  print("You are inside the spooky house.")
  print("You see old stairs that go upstairs and stairs that go down")
  print("A kitchen and a living room")
  print("1. Go upstairs")
  print("2. Go downstairs")
  print("3. Check the kitchen")
  print("4. Check the living room")
  print("5. Try to open closed door")
  choice = input("Choose: ")
  if choice == '1':
    upstairs()
  elif choice == '2':
    downstairs()
  elif choice == '3':
    kitchen()
  elif choice == '4':
    Living_room()
  elif choice == '5':
    closed_door()
def upstairs():
  print("The floor caves in")
  print("you died.")
  main_menu()
def downstairs():
  print("You slipped on oil that was on the steps.")
  print("you died to a trap")
  main_menu()
def kitchen():
  print("you see a pile of candy on the counter")
  print("1. Do you grab it ")
  print("2. Do you leave it")
  choice = input("choose: ")
  if choice == '1':
    print("You take the candy and find out it's the legendary candy pile")
    print("YOU WIN")
  elif choice == '2': 
    inside()
def Living_room():
  print("The TV is on and you see someone crawling out")
  print("Game over")
  main_menu()
def closed_door():
  print("Its still unlocked")
  print("1. go home")
  print("2. Keep exploring")
  choice = input("Whats your choice: ")
  if choice == '1':
    Give_up()
  elif choice == '2':
    inside(
      
    )

def Give_up():
    print("You decide to go home")
    print("when you get home you have the option to either")
    print("1. place bag down and see what candy you have")
    print("2. Go to bed")
    choice = input("Choose: ")
    if choice == '1':
      print("You chose 1 of 2 peaceful options.")
    elif choice == '2':
      print("you chose 2 of 2 peaceful options.")
# finally, we have main -- which we use to start the program 
def main():
    print("M5LAB1 - Choose Your Own Adventure")
    main_menu()
    print("Thanks for playing!")

#start the program
main()
