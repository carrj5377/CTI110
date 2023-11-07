# **************************************************
# CTI-110 - P5LAB3
# Julian Carr
# 11/7/2023
#
# 
# **************************************************

score = 0
def ask_question(question, answer):
    global score
    user_answer = input(question)
    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
# Welcome message
print("Welcome to the Quiz Game!")
# List of questions and answers
questions = [
   # List of multiple-choice anime questions

    ("What is the name of the protagonist in 'One Piece'?\n(a) Monkey D. Luffy\n(b) Roronoa Zoro\n(c) Nami\n(d) Usopp\n", "a"),
    ("Who is the main character in 'Naruto'?\n(a) Naruto Uzumaki\n(b) Sasuke Uchiha\n(c) Kakashi Hatake\n(d) Sakura Haruno\n", "a"),
    ("Which anime features the character 'Goku'?\n(a) Dragon Ball\n(b) Attack on Titan\n(c) My Hero Academia\n(d) Death Note\n", "a"),
    ("What is the name of the giant humanoid creatures in 'Attack on Titan'?\n(a) Titans\n(b) Shinigami\n(c) Hollows\n(d) Akatsuki\n", "a"),
    ("In 'My Hero Academia', what is the name of the main protagonist?\n(a) Izuku Midoriya\n(b) Katsuki Bakugo\n(c) Shoto Todoroki\n(d) All Might\n", "a"),
    ("Who is the main character in 'Death Note'?\n(a) Light Yagami\n(b) L Lawliet\n(c) Misa Amane\n(d) Ryuk\n", "a")
]

# Ask questions from the list
for question, answer in questions:
    ask_question(question, answer)
# Display score
print(f"Your total score is {score} out of {len(questions)}.")
# Goodbye message
print("Thank you for playing the Quiz Game!")