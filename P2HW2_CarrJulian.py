# CTI-110
# P2HW2 - List
# Julian Carr
# 09/19/2023
# This program allows the user to input grades for 6 modules then puts them in a list
# then gives back minimum grade, maximum grade, sum of the grades, and the grades  
# average in the list

# Asking user to input their grades for each module
print("Enter grade for Module 1: ", end='')
mod1 = float(input())

print("Enter grade for Module 2: ", end='')
mod2 = float(input())

print("Enter grade for Module 3: ", end='')
mod3 = float(input())

print("Enter grade for Module 4: ", end='')
mod4 = float(input())

print("Enter grade for Module 5: ", end='')
mod5 = float(input())

print("Enter grade for Module 6: ", end='')
mod6 = float(input())

# inputing all the modules into a list
module_grades = [mod1,mod2,mod3,mod4,mod5,mod6]

# A variable to provide the sum of all the grades
# Also to set up for the average
total = sum(module_grades)

print("------------Results------------")
# Provides the minimum from the list by using the min function
print("Your Lowest Grade:\t\t", min(module_grades))

# Provides the maximum from the list by using the max function
print("Your Highest Grade:\t\t", max(module_grades))

# Uses the total variable which holds the sum function and then adds all the grades
# thats been input into each module
print("The Sum of Your Grades:\t", total)

# variable used to learn the average  of all the grades in the list
AVG = total / len(module_grades)
print(f"Your Average:\t\t\t {AVG:.2f}")
print("-------------------------------")