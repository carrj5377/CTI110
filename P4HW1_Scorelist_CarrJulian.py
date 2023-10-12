# CTI-110
 # P4HW1 - Score List
# Julian Carr
 # 10/10/23
 # ask users to enter number of scores they would like to enter 
# create a loop to collect the number of scores
# scores should be between 0 and 100
# if score is not between 0 and 100, ask user to enter a valid score


  
  # ask user to enter number of scores they would like to enter
num_scores = int(input("Enter the number of scores: "))

# define a list to store the scores
scores = []

  # create a loop to collect the number of scores

for num in range(num_scores):
  # ask user to enter a score
  print(f"Enter score {num+1}: ", end="")
  score = int(input())
    
  if score >= 0 or score <= 100:
    
  # if score is not between 0 and 100, ask user to enter a valid score
  
    
    while score < 0 or score > 100:
      score = int(input("Invalid score try again. Enter score: "))
    # add the score to the list
  scores.append(score)
lowest = min(scores)
print("-"*40)
print("RESULT")
print("Lowest Score:", lowest)
scores.remove(lowest)
print('Modified list:', scores)
total = sum(scores)
avg = total / len(scores)
print("scores average: ", avg)

if avg >= 90:
  print("A")
elif avg >= 80:
  print("B")
elif avg >= 70:
  print("C")
elif avg >= 60:
  print("D")
else:
  print("F")