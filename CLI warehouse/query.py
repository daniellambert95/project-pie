#!/usr/bin/env python3

from data import stock
import tabulate

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
print("What would you like to do next?\n1. See a tabled list of all the stock \n2. List items in the warehouses seperately\n3. Search for an item and place an order\n4. Quit")
choice1 = int(input("Select the operation you would like to process by entering 1, 2, 3 or 4: "))

# If they pick 1
# This will create a nice tabled list of evrything
if choice1 == 1:
    print("\nItems in all warehouses:\n")
    header = stock[0].keys()
    rows = [x.values() for x in stock]
    print (tabulate.tabulate(rows, header))
    
# If they pick 2

if choice1 == 2:
    print("\nItems in warehouse 1:\n")
    for item in warehouse_1_stock:
        print("-",item['state'], item['category'])

    print('\n')

    print("\nItems in warehouse 2:\n")
    for item in warehouse_2_stock:
        print("-",item['state'], item['category'])

# Else, if they pick 3


elif choice1 == 3:
    item_name = input("Please enter the name of the item you are looking for here: ")
    total_amount = 0

    warehouse_1_amount = 0
    for x in warehouse_1_stock:
        if x['category'] == item_name:
            warehouse_1_amount +=1

    warehouse_2_amount = 0
    for x in warehouse_2_stock:
        if x['category'] == item_name:
            warehouse_2_amount +=1

    total_amount = (warehouse_1_amount + warehouse_2_amount)
   
    if total_amount > 0 :
        print(f"The total amount of {item_name} is: {total_amount}\n")

        if warehouse_1_amount > 0 and warehouse_2_amount > 0:
            print(f"The item {item_name} can be found in both warehouses")
            if warehouse_1_amount > warehouse_2_amount:
                print(f"Warehouse1 has more of {item_name} with a total of: {warehouse_1_amount}")
            else:
                print(f"Warehouse2 has more of {item_name} with a total of: {warehouse_2_amount}")

        elif warehouse_1_amount > 0:
            print(f"The item {item_name} can be found in warehouse1")
        else:
            print(f"The item {item_name} can be found in warehouse2")

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
    print(f"")
# Else
else:
    print("The input you have given me isn't valid. Pleas try again.")
# Thank the user for the visit
print(f"Thank you for your time {name}, we hope to see you again soon.")