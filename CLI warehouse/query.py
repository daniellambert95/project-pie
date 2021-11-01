#!/usr/bin/env python3

from data import stock
import tabulate
from datetime import datetime

warehouse_1_stock = []
for warehouse_item_1 in stock:
    if warehouse_item_1['warehouse'] == 1:
        warehouse_1_stock.append(warehouse_item_1)

warehouse_2_stock = []
for warehouse_item_2 in stock:
    if warehouse_item_2['warehouse'] == 2:
        warehouse_2_stock.append(warehouse_item_2)

# Welcome message
print("Welcome to the Warehouse Ordering System")
# Assigning the user name to a variable
name = input("To proceed further please enter your name here: ")
# Welcome the user
print(f"Welcome back {name}!")
# Show the menu and ask the user to pick a choice
print("What would you like to do next?\n1. See a tabled list of all the stock \n2. List items in the warehouses seperately\n3. Search for an item and place an order\n4. Browse by Category \n5. Quit")
choice1 = int(input("\nSelect the operation you would like to process by entering 1, 2, 3, 4 or 5: "))
print("\n")

# If they pick 1
# This will create a nice tabled list of evrything
if choice1 == 1:
    print("\nItems in all warehouses:\n")
    header = stock[0].keys()
    rows = [x.values() for x in stock]
    print (tabulate.tabulate(rows, header))
    
# If they pick 2

if choice1 == 2:
    total_stock_warehouse1 = 0
    print("\nItems in warehouse 1:\n")
    for item in warehouse_1_stock:
        total_stock_warehouse1 +=1
        print("-",item['state'], item['category'])

    print('\n')
    total_stock_warehouse2 = 0
    print("\nItems in warehouse 2:\n")
    for item in warehouse_2_stock:    
        total_stock_warehouse2 +=1
        print("-",item['state'], item['category'])
    print(f'\nTotal items in warehouse 1: {total_stock_warehouse1}')
    print(f'Total items in warehouse 2: {total_stock_warehouse2}')

# Else, if they pick 3


elif choice1 == 3:
    item_name = input("Please enter the name of the item you are looking for here: ")
    item_name = item_name.lower()
    # item_name = item_name.title()
    # item_name = item_name.split()
    total_amount = 0

    warehouse_1_amount = 0
    for x in warehouse_1_stock:
        state_category = f"{x['state']} {x['category']}"
        state_category = state_category.lower()
        if  state_category == item_name:
            warehouse_1_amount +=1

    warehouse_2_amount = 0
    for x in warehouse_2_stock:
        state_category = f"{x['state']} {x['category']}"
        state_category = state_category.lower()
        if  state_category == item_name:
            warehouse_2_amount +=1

    total_amount = (warehouse_1_amount + warehouse_2_amount)
   
    if total_amount > 0 :
        print(f"Amount of {item_name} available: {total_amount}\n")
        print(f"Location:")
        for x in warehouse_1_stock:
            if x['category'] == item_name:
                date_item_stocked = x['date_of_stock']
                date_item_stocked = datetime.strptime(date_item_stocked, '%Y-%m-%d %H:%M:%S')
                time_in_stock = str(datetime.utcnow() - date_item_stocked)
                time_in_stock = time_in_stock.split(' ', 1)[0]
                print(f"- Warehouse {x['warehouse']} (in stock for {time_in_stock} days)")
        for x in warehouse_2_stock:
            if x['category'] == item_name:
                date_item_stocked = x['date_of_stock']
                date_item_stocked = datetime.strptime(date_item_stocked, '%Y-%m-%d %H:%M:%S')
                time_in_stock = str(datetime.utcnow() - date_item_stocked)
                time_in_stock = time_in_stock.split(' ', 1)[0]
                print(f"- Warehouse {x['warehouse']} (in stock for {time_in_stock} days)")
        if warehouse_1_amount > warehouse_2_amount:
            print(f"Maximum availability: {warehouse_1_amount} in Warehouse 1")
        else:
            print(f"Maximum availability: {warehouse_2_amount} in Warehouse 2")

        choice1_2 = input("\nWould you like to place an order for this item?\n Type 'Y' for yes and 'N' for no: ")
        if choice1_2 == "N":
            print("Thank you, goodbye!")
        elif choice1_2 == "Y":
            choice1_2_3 = int(input("\nHow many would you like to order?: "))
            if choice1_2_3 <= total_amount:
                print(f"\nThat's fine {name}, your order of {choice1_2_3} : {item_name} has been placed successfully.")
                print(f"\nWould you like to order anything else while you're logged in?")
                order = input("Enter 'Y' for yes or 'N' for no: ")
                if order == "N":
                    print("That's fine.")
                    
            elif choice1_2_3 > total_amount:
                print("The amount you have requested exceeds the total amount")
                choice1_2_4 = input("Would you like to order the maximum? Type 'Y' for yes and 'N' for no:  ")
                if choice1_2_4 == "Y":
                    print(f"That's fine {name}, your order of {total_amount} : {item_name} has been placed successfully.") 
                    print(f"Would you like to order anything else while you're logged in?")
                    order = input("Enter 'Y' for yes or 'N' for no: ")
                    if order == "N":
                        print("That's fine.")
                    
    else:
        print(f"Unfortunately, {item_name} is out of stock.")
    
# Else, if they pick 4
elif choice1 == 4:
    total_cat = 0
    for x in stock:
        if x['category'] == "Keyboard":
            total_cat +=1
    print(f"1. Keyboard ({total_cat})")
    total_cat = 0
    for x in stock:
        if x['category'] == "Smartphone":
            total_cat +=1
    print(f"2. Smartphone({total_cat})")
    total_cat = 0
    for x in stock:
        if x['category'] == "Mouse":
            total_cat +=1
    print(f"3. Mouse({total_cat})")
    total_cat = 0
    for x in stock:
        if x['category'] == "Laptop":
            total_cat +=1
    print(f"4. Laptop({total_cat})")
    total_cat = 0
    for x in stock:
        if x['category'] == "Headphones":
            total_cat +=1
    print(f"5. Headphones({total_cat})")
    total_cat = 0
    for x in stock:
        if x['category'] == "Monitor":
            total_cat +=1
    print(f"6. Monitor({total_cat})")
    total_cat = 0
    for x in stock:
        if x['category'] == "Router":
            total_cat +=1
    print(f"7. Router({total_cat})")
    total_cat = 0
    for x in stock:
        if x['category'] == "Tablet":
            total_cat +=1
    print(f"8. Tablet({total_cat})\n")
    
    choice4 = int(input("Type the number of the category you would like to browse: "))
    print("\n")

    if choice4 == 1:
        print("List of keyboards available: ")
        for x in stock:
            if x['category'] == "Keyboard": 
                print(f"{x['state']} {x['category']}, Warehouse {x['warehouse']}")

    elif choice4 == 2:
        print("List of smartphones available: ")
        for x in stock:
            if x['category'] == "Smartphone": 
                print(f"{x['state']} {x['category']}, Warehouse {x['warehouse']}")

    elif choice4 == 3:
        print("List of mouse's available: ")
        for x in stock:
            if x['category'] == "Mouse": 
                print(f"{x['state']} {x['category']}, Warehouse {x['warehouse']}")

    elif choice4 == 4:
        print("List of laptops available: ")
        for x in stock:
            if x['category'] == "Laptop": 
                print(f"{x['state']} {x['category']}, Warehouse {x['warehouse']}")

    elif choice4 == 5:
        print("List of headphones available: ")
        for x in stock:
            if x['category'] == "Headphones": 
                print(f"{x['state']} {x['category']}, Warehouse {x['warehouse']}")

    elif choice4 == 6:
        print("List of monitor's available: ")
        for x in stock:
            if x['category'] == "Monitor": 
                print(f"{x['state']} {x['category']}, Warehouse {x['warehouse']}")

    elif choice4 == 7:
        print("List of routers available: ")
        for x in stock:
            if x['category'] == "Router": 
                print(f"{x['state']} {x['category']}, Warehouse {x['warehouse']}")

    elif choice4 == 8:
        print("List of tablets available: ")
        for x in stock:
            if x['category'] == "Tablet": 
                print(f"{x['state']} {x['category']}, Warehouse {x['warehouse']}")

    

# Show a menu of available categories. This menu will have to include a numeric code 
# (the number the user will type in to select a category), 
# the name of the category and the amount of items available in that category (in any warehouse).

# There is no list of categories in the dataset, so you will have to iterate all the stock to identify the categories and 
# count their items.

# You will also have to find a way to produce a numeric identifier for each category.

# The menu list should show single categories (each category should only appear once).

# Ask the user to type the category number of their choice.

# List all items in that category. This time, print them one after the other (not separated by warehouse) and 
# include the name of the warehouse at the end of each line.

# Be aware that the code associated to each category will be an auto-generated numeric code and 
# the items have a text value as category. You will have to think of a way to identify each number typed by the user to
#  the correct category name to be able to filter the stock.

# Else, if they pick 5
elif choice1 == 5:
    print(f"")
# Else
else:
    print("The input you have given me isn't valid. Pleas try again.")
# Thank the user for the visit
print(f"Thank you for your time {name}, we hope to see you again soon.")