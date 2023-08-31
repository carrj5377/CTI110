"""
CTI110
P1LAB2 - Sales
Julian Carr
8/31
Simple point of sales program

"""
# Set up our store

store_name = "Game Shack"
product = "games"
stock = 40
price = 49.99

#Greet Customer
print("Welcome to the", store_name)
print() # Blank line
print("Whats your name?")
customer_name = input()
print("Its nice to meet you", customer_name)
print() # Blank line

# Explain product
print("we have a bunch of", product)
print() # blank line
print("Our games cost: $",price)
print("only", stock, "left!")

#Take order
print("How many",product, "would you like")
# input gives us a string
# order = input()
# convert it to a number
# order = int(order)

# or .....
order = int(input())

# finish up
total_price = order * price
print("So you would like")
print( order,product,"for a total of $", total_price)