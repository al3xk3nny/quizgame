def show_menu():
    print("Quiz Game")
    print("----------")
    print()
    print("1. Run quiz")
    print("2. Enter a question")
    print("3. Exit")
    print()
    
    option = input("Enter option: ")
    return option

# 1. Run quiz.
def ask_questions():
    with open("questions.txt") as f:
        questions = f.read().split("\n")[:-1] # Read the text file using file handel, f. This returns a string. Split the string at "\n". When you split a string you return a list. The [:-1] returns everything bar the last entry. This is important as in the add_a_question function we added a "\n" to ensure each question|answer combination returned on a separate line giving us an empty new line at the end. 
        
    score = 0
    total = len(questions)
        
    for q in questions:
        # question = q.split("|")[0]
        # answer = q.split("|")[1]
        
        # Also written as this;
        question, answer = q.split("|")
        
        guess = input(question)
        print(guess)
        
        if guess.lower() == answer.lower(): # Case insensitive at point of comparison.
            score += 1
            
    # print("You scored {0}".format(score) + " out of {0}".format(len(questions)))
    # Can also be written like this if you add a variable called "total" above and call it below.
    print("You scored {0} out of {1}".format(score, total))
    
# 2. Enter a question.
def add_a_question():
    question = input("Enter a question: ")
    answer = input("Ok then tell me, " + question + ": ")

    with open("questions.txt", "a") as f: 
        line= question + "|" + answer + "\n"
        f.write(line)

# 3. Exit.
while True:
    option = show_menu() # No conflict with naming variable "option" as "option" variable in show_menu function appears within a function.
    
    if option == "1":
        ask_questions()
        
    if option == "2":
        add_a_question()
    
    if option == "3": # Important to use "" as comparing against a string in show_menu function above.
        break

