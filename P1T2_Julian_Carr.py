import matplotlib.pyplot as plt


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
num_days = int(input("How many days? "))
for day in range(num_days):
  print("Day", day, ":", end="")
  today = int(input())
  data.append(today) # add it to the end of the list

# print min, max, and total
print()
total = sum(data)
print("Total number of pokemans caught today. ", total)

MX = max(data)
print("Best day: ", MX)

MN = min(data)
print("Worst day: ", MN)

avg = total / num_days
print("average: ", avg)
#put the data in a list (DONE)

fig, ax = plt.subplots()
ax.plot(range(num_days), data)
plt.title("Pokeman Data")
plt.xlabel('day #')
plt.ylabel('pokemans collected')
plt.show()
