<<<<<<< HEAD
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




=======
import json


#works
def welcome_menu():
    correct_input = False
    choice_from_menu = 0
    print("Welcome to the database manager, here you can manage your stock")
    print("Enter 1 to add to database") 
    print("2 to View the database") 
    print("3 to update the database") 
    print("4 to Remove Items From The Database") 
    print("5 to close and save")
    while correct_input == False and choice_from_menu !=5:
        try:
            choice_from_menu = int(input("enter your choice: "))
        except ValueError:
            print("invalid choice, please enter a number")
            continue
        else:
            if choice_from_menu > 5:
                print("your number is too large please try again")
            else:
                

    
                if choice_from_menu == 1:
                    add_data(stock)
                elif choice_from_menu == 2:
                    view_data()
                elif choice_from_menu == 3:
                    update_data(stock)
                elif choice_from_menu == 4:
                    remove_stock(stock)
                
    
    save_data(stock)

#works
def load_data():
    try:
        with open("database.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("file doesnt exist already, creating database now")
        save_data()
    except json.JSONDecodeError:
        print("save file is corrupted! Starting fresh")
        save_data()

#works
def add_data(stock):
    name = input("Enter the name of the additional item: ")
    quantity = int(input("what is the quantity of the stock: "))
    price = input("what is the price of your input: ")
    id = int(input("Enter the id of your item: "))
    
    stock[id] = {"name":name, "quantity":quantity, "price":price, }
    save_data(stock)
    return stock

#works
def view_data():
    my_project_data = load_data()
    print(my_project_data) 
    
#works
def update_data(stock):
    item = input("Enter the ID of item: ")
    change = input(("what attribute needs to be changed: ")).lower()
    new_value = input("Enter new value: ")
    for id, value in stock.items():
        if id == item:
            value[change] = new_value
             
    save_data(stock)
    return stock
            
#works
def remove_stock(stock):
    id = input("Enter the ID of the item you wish to delete: ")
    del stock[id]
    save_data(stock)
    return stock
        

def check_stock_level(stock, quantity):
    pass



#works
def save_data(stock):
    with open("database.json", "w") as f:
        json.dump(stock, f, indent=3)
        
stock = load_data() or {}

welcome_menu()
>>>>>>> 09cc0ad (initial commit)
