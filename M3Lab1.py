# CTI 110
# M3 LAB1 - Leap Year
# Carr Julian
# 9/21/23

# Calculate if a year is a leap year
# Leap years are:
# divisble by 4
# unless it's a century, then its's divisible by 400


# todo : handle the century case
is_leap_year = False

print("What year to check?")
year = int(input())

# If the year is divisible by 4, it's a leap year
# We use %, the modulo opperator
if year % 4 == 0:
  is_leap_year = True

# Century exception:
# if if it's divisible by 100
if year % 100 == 0:
# Then it isnt a leap year
  is_leap_year = False
# unless its also divisble by 400
  if year % 400 == 0:
# and the its a leap year
    is_leap_year = True


# output the answer
if is_leap_year:
  print(year,"is a leap year.")
else:
  print(year,"is not a leap year.")