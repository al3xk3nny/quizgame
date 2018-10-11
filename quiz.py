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

def add_a_question():
    question = input("Enter a question: ")
    answer = input("Ok then tell me, " + question + ": ")

    with open("questions.txt", "a") as f: 
        line= question + "|" + answer + "\n"
        f.write(line)

while True:
    option = show_menu() # No conflict with naming variable "option" as "option" variable in show_menu function appears within a function.
    
    if option == "1":
        print("You picked run a quiz")
        
    if option == "2":
        add_a_question()
    
    if option == "3": # Important to use "" as comparing against a string in show_menu function above.
        break

