import matplotlib.pyplot as plt
import turtle

"""
# Collect data
print("Enter poekman data:")
print("Day 1:", end="")
day1 = int(input())
print("Day 2:", end="")
day2 = int(input())
print("Day 3:", end="")
day3 = int(input())

# Put the data in a list
data = [day1, day2, day3]

print()
total = sum(data)
print("The total number of pokeman caught", total)

MX = max(data)
print("Highest number of pokemans caught today", MX)

MN = min(data)
print("Least amout of pokemans caught today", MN)
"""
#New version - loop and get each day at a time
data = [] #empty list
num_days = turtle.numinput("Input","How many days")
num_days = int(num_days)
for day in range(num_days):
  #print("Day:",day  , end="")
  label = "Day #" + str(day)# "Day 1" and so on
  today = turtle.numinput(label, "How many pokeman?")
  print()
  data.append(today) # add it to the end of the list

# print min, max, and total
print()


MX = max(data)
print("Best day: ", MX)

MN = min(data)
print("Worst day: ", MN)

total = 0
for num in data:
  total += num
# total is now all the numbers in data, added up
average = total / num_days
print("Total:", total)
print("Average:", average)
#put the data in a list (DONE)

fig, ax = plt.subplots()
ax.plot(range(num_days), data)
plt.title("Pokeman Data")
plt.xlabel('day #')
plt.ylabel('pokemans collected')
plt.show()
