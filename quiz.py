def show_menu()
    print("Quiz Game")
    print("----------")
    print()
    print("1. Run quiz")
    print("2. Enter a question")
    print("3. Exit")
    print()
    
    option = input("Enter option: ")
    return option

while True:
    option = show_menu() # No conflict with naming variable "option" as "option" variable in show_menu function appears within a function.
    
    if option == "3": # Important to use "" as comparing against a string in show_menu function above.
        break

