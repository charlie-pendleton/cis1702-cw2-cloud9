import json

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

def add_data(stock):
    inputs = False
    count = 0
    id_count=0
    while inputs == False:
        name = input("Enter the name of the additional item: ")
        try:
            quantity = int(input("what is the quantity of the stock: "))
        except ValueError:
            print("enter an integer amount")
            count +=1
        try:
            price = float(input("what is the price of your input: "))
        except ValueError:
            print("enter a float")
            count += 1
        try:
            id = int(input("Enter the id of your item: "))
            for s in stock:
                if stock[s] == id:
                    id_count += 1
            if id_count > 0:
                print("id already exists")
                count +=1
        except ValueError:
            print("enter an integer amount")
            count +=1
        if count == 0:
            inputs = True
        else:
            print("invalid set of data, please try again")
        

    
    stock[id] = {"name":name, "quantity":quantity, "price":price, }
    save_data(stock)
    return stock

def view_data():
    my_project_data = load_data()
    print(my_project_data) 
    
def update_data(stock):
    id_exists = False
    changes_valid = False
    count_of_invalid_inputs = 0
    while id_exists != True:
        try:
            item = int(input("Enter the ID of item: "))
        except ValueError:
            print("enter an integer")
        for s in stock:
            if stock[s] == item:
                print("ID of item found")
                id_exists = True
        print("ID not found re-enter value")  
    while changes_valid == False:
        change = input(("what attribute needs to be changed: ")).lower()
        if change != "name" or "quantity" or "price":
            print("attribute not found")
            count_of_invalid_inputs += 1
        try:
            new_value = float(input("Enter new value: "))
        except ValueError:
            print("new value is invalid, please enter a float next time")
            count_of_invalid_inputs += 1

    for id, value in stock.items():
        if id == item:
            value[change] = new_value
             
    save_data(stock)
    return stock
            

def remove_stock(stock):
    id_exists = False
    while id_exists != True:
        try:
            item = int(input("Enter the ID of item: "))
        except ValueError:
            print("input not valid, input an integer")
        for s in stock:
            if item == int(s):
                print("ID of item found")
                id_exists = True
                del stock[s]
                save_data(stock)
                print("ran")
                break

        if id_exists == False:
            print("ID not found reenter value")
    return stock
        

def check_stock_level(stock, quantity):
    pass



#works
def save_data(stock):
    with open("database.json", "w") as f:
        json.dump(stock, f, indent=3)
        
stock = load_data() or {}

welcome_menu()
