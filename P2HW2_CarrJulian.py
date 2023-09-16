#calculates and displays travel expense by using input commmand
#08/26/2023
# CTI-110 P1HW2 - Travel Expense
#Julian Carr

#ask user to enter budget
print("Please enter your budget: ", end='') 
b = int(input())
print()

#Ask user for the destination
print("Next enter your destination: ", end='')  
dest = input()
print()

# ask user how they will spend on gas
print("How much is gas going to cost you? ", end='')
gas = int(input())
print()

#ask user how much there hotel will cost
print("how much will your hotel/hotels cost you? ", end='')
h = int(input())
print()

#finally ask how much food will cost them
print("Lastly, how much will food cost you? ", end='')
food = int(input())
print()
print()


#Seperate the categories
print("----------------TRAVEL EXPENSES----------------")


#return expenses
print("location:\t\t", dest)


print("intial budget:\t", b)


#expense from the gas quetsion
print("Fuel cost:\t\t ", end='')
print(gas)


#expense from the hotels question
print("Hotels expense:\t ", end='')
print(h)


#expense from the food question
print("Food expense:\t ", end='')
print(food)
print("-----------------------------------------------")

#Subtract Gas,hotel, and food from intial budget to get remaining balance
r = b - gas - h - food
print("Remaing Balance: ", end='')  
print(r)


