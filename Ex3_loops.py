# -------------------------------------------
# Exercise 3: Loops and Decisions Homework
# -------------------------------------------
# This exercise will help you practise everything you’ve learned so far:
# - Variables
# - Input and Output
# - Decision Making (if / elif / else)
# - Loops (while or for)
#
# Complete this exercise individually.
# Make sure your code runs correctly before submitting.
# -------------------------------------------


# -------------------------------------------
# Task 1: Collect Multiple Inputs
# -------------------------------------------
# TODO:
# 1. Ask the user for the names of three friends (or classmates).
# 2. Store them in separate variables.
# 3. Use a loop to print a greeting for each friend.
#
# Example idea:
# friend1 = Use input() to ask for the name
# friend2 = ...
# friend3 = ...
# friends = [friend1, friend2, friend3]  # put variables in a list
# for name in friends:
#     print("Hello " + name)  # loop through and greet

# Write your code below:
print()
print("Task 1 - Collect multiple inputs and output a list")
print()
friend1 = input("Write your first friends name: ")
friend2 = input("Write your second friends name: ")
friend3 = input("Write your third friends name: ")
friend_list = [friend1, friend2, friend3]
for name in friend_list:
    print("Hello " + name, "How have you been?")
print()



# -------------------------------------------
# Task 2: Number Input and Decisions
# -------------------------------------------
# TODO:
# 1. Ask the user to enter a number between 1 and 10.
# 2. Use if / elif / else to print:
#    - Message if the number is too low (<1)
#    - Message if the number is too high (>10)
#    - Message if the number is in the correct range
# 3. Use a loop so that if the number is invalid, the user is asked again.
#
# Example idea:
# number = Use input() to ask the user for a number 
# (HINT: When using input(), the user response is always saved as a string)
#
# while some_condition_is_not_met:
#     print("Invalid number, try again")
#     number = Use input() to ask the user for a number
#
# if some_condition1:
#     print("Message for first case")
# elif some_condition2:
#     print("Message for second case")
# else:
#     print("Message for other cases")

# Write your code below:
print()
print("Task 2: Number Input and Decisions")
print()
count = 0
sec_num = 
guess_num = int(input("Enter a number between 1 and 100: "))
while sec_num != guess_num:
    if guess_num < sec_num:
        guess_num = int(input("Too low! Guess again: ")) 
        count = count + 1
    elif guess_num > sec_num:
        guess_num = int(input("Too high Guess again: ")) 
        count = count + 1
print(f"You got the number and it took you {count} guesses!")
print()


# -------------------------------------------
# Task 3: Mini Quiz Project Using a List
# -------------------------------------------
# TODO:
# 1. Ask the user multiple questions.
# 2. Use a list to store your questions. HINT: Look at Task 1 to see how this is done.
#    Example of a list:
#    questions = ["What is 2 + 2?", "Type the color of the sky.", "First letter of the alphabet?"]
# 3. Use a loop to go through the list of questions and ask each one.
# 4. Use if / elif / else to give feedback for each answer.
#
# Example idea:
# for i in questions:
#     answer = input(i + " ")
#     # if answer == "something":
#     #     print("Good!")
#     # elif answer == "something else":
#     #     print("Try again")
#     # else:
#     #     print("Check your answer")

# Write your code below:
print()
print("Task 3: Mini Quiz Project Using a List")
count = 0
q1 = "What is the square root of 64? "
q2 = "What is quarter past six pm in the 24 hour clock? "
q3 = "what is the Russian equivalent of the American Astronaut? "
q_list = [q1, q2, q3]
for question in q_list:
    answer = input(question )
    if question == q1 and answer == "8":
        print("Correct!") 
        count = count + 1
        print(f"Current score {count}")
    elif question == q2 and answer == "18:15":
        print("Correct!")
        count = count + 1
        print(f"Current score {count}")
    elif question == q3 and answer == "Cosmonaut":
        print("Correct!")
        count = count + 1
        print(f"Final score {count}")
    else:
        print("Incorrect. Try again.")
print()


# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------
# Complete any of these for extra practice.

# Extension 1: Input Validation
# -------------------------------------------
# TODO:
# 1. Make sure that text answers are not empty.
# 2. Make sure number answers are within a valid range.
# 3. Keep asking until valid input is given.
#
# Example idea (syntax only):
# answer = input("Enter something: ")
# while answer_is_empty:
#     print("You must type something")
#     answer = input("Try again: ")

# Write your code below:



# Extension 2: Multiple Feedback Options
# -------------------------------------------
# TODO:
# 1. Ask the user to input one of at least three possible responses. E.g. "Type A, B, or C: "
# 2. Use if / elif / else to handle different answers.
# 3. Use a suitable loop (for/while) to repeat the question if input is not valid.
#
# Example idea (syntax only):
# answer = Use input() to ask for a response
# if answer == "A":
#     print something here
# elif answer == "B":
#     print something here
# else:
#     print something here

# Write your code below:



# Extension 3: Repeat Quiz for Another User
# -------------------------------------------
# TODO:
# 1. After one user finishes, ask a new user to enter their name.
# 2. Repeat the same quiz questions for the new user.
# 3. Give feedback for each answer using if / elif / else.
# 4. Loop through all questions for each user.
#
# Example idea:
# new_user = input("Enter your name: ")
# for i in questions:
#     answer = input(i + " ")
#     # check answer and print feedback

# Write your code below:



# -------------------------------------------
# ADVANCED TASK: Combine Everything
# -------------------------------------------
# TODO:
# 1. Ask the names of three friends and greet each using a loop.
# 2. Ask the user to enter a number between 1 and 10, with loop validation.
# 3. Run a mini-quiz using a list of questions.
# 4. Use loops to repeat all tasks above and if / elif / else to give feedback.
# Hint: combine loops and decisions, and you can nest loops inside loops.

# Write your advanced code below:



# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# Once you have completed all required tasks:
# 1. Save your file.
# 2. Open the terminal and use Git commands to stage, commit, and push your changes.
#    (Hint: recall the commands for adding, committing, and pushing.)
# 3. Check GitHub to confirm your final version appears in your repository.
# -------------------------------------------
