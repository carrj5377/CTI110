"""
CTI 110
P2LAB1 -- Gas Prices
write program with a c

 Output each floating-point value with two digits after the decimal point,                  
 which can be achieved as follows:
print(f'{your_value1:.2f} {your_value2:.2f} {your_value3:.2f}')

print"""

# Ask for miles per gallon
miles_per_gallon = float(input("what is the car's MPG? "))
print()
# Ask for price per gallon of gas
price_per_gallon = float(input("price per gallon? "))
print()
# show the price per mile to drive
# unit we want is $/miles
price_per_mile = price_per_gallon / miles_per_gallon

# print("this vehicle costs $", price_per_mile, "to drive 1 mile." )
# f strings are like this : {variable:.2f} for 2 decimal places

print (f"This vehicle costs ${price_per_mile:.2f} to drive 1 mile.")

# Last step: Tell the user the cost to drive 20, 75, and 500 miles
print()
# cost for 20 miles
print(f"the cost to drive this vehicle 20 miles is ${price_per_mile * 20:.2f}")

print()
# cost for 75 miles
print(f"the cost to drive this vehicle 75 miles is ${price_per_mile * 75:.2f}")

print()
# cost for 500 miles
print(f"the cost to drive this vehicle 500 miles is ${price_per_mile * 500:.2f}")