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
print("TRAVEL EXPENSE")
print()

#return expenses
print("location ",dest)
print()

print("intial budget ", b)
print()

#expense from the gas quetsion
print("Gas: ", end='')
print(gas)
print()

#expense from the hotels question
print("Hotels: ",end='')
print(h)
print()

#expense from the food question
print("Food:",end='')
print(food)
print()

#Subtract Gas,hotel, and food from intial budget to get remaining balance
r = b - gas - h - food
print("Remaing Balance: ",end='')  
print(r)


