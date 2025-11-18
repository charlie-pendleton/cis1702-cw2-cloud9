import json

stock = {"carrot":"1000"}

def welcome_menu():
    correct_input = False
    print("Welcome to the database manager, here you can manage your stock")
    print("Enter 1 to add to database") 
    print("2 to View the database") 
    print("3 to update the database") 
    print("4 to Remove Items From The Database") 
    print("5 to close and save")
    while correct_input == False:
        try:
            choice_from_menu = int(input("enter your choice: "))
        except ValueError:
            print("invalid choice, please enter a number")
            continue
        else:
            if choice_from_menu > 5:
                print("your number is too large please try again")
            else:
                correct_input = True

    return choice_from_menu

def load_data():
    try:
        with open("database.json", "r") as f:
            print("yea")
            return json.load(f)
    except FileNotFoundError:
        print("file doesnt exist already, creating database now")
        with open("database.json", "w") as f:
            json.dump(stock, f, indent=2)
    except json.JSONDecodeError:
        print("save file is corrupted! Starting fresh")
        with open("database.json", "w") as f:
            json.dump(stock, f, indent=2)

def add_data():
    pass

def view_data():
    pass

def update_data():
    pass

def remove_stock():
    pass



choice = welcome_menu()
my_project_data = load_data()

print(my_project_data)




