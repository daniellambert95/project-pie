#!/usr/bin/env python3
"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""
from data import warehouse1, warehouse2

# YOUR CODE STARTS HERE
print("Welcome to the Warehouse Ordering System")
# Get the user name
name = input("To proceed further please enter your name here: ")
# Greet the user
print(f"Welcome back {name}!")
# Show the menu and ask to pick a choice
print("What would you like to do next?\n1. List items in the warehouse\n2. Search an item and place an order\n3. Quit")
choice1 = int(input("Select the operation you would like to process by entering 1, 2 or 3: "))
# If they pick 1
if choice1 == 1:
    print(f"Items from warehouse 1: {warehouse1}\nItems from warehouse 2: {warehouse2}")
# Else, if they pick 2
elif choice1 == 2:
    item_name = input("Please enter the name of the item you are looking for here: ")
    if item_name in warehouse1 or item_name in warehouse2:
        sum_of_item = warehouse1.count(item_name) + warehouse2.count(item_name)
        print(f"The total amount of {item_name} is: {sum_of_item}")
        if item_name in warehouse1 and item_name in warehouse2:
            print(f"The item {item_name} can be found in both warehouses")
            if warehouse1.count(item_name) > warehouse2.count(item_name):
                print(f"Warehouse1 has more of {item_name} with a total of: {warehouse1.count(item_name)}")
            else:
                print(f"Warehouse2 has more of {item_name} with a total of: {warehouse2.count(item_name)}")
        elif item_name in warehouse1:
            print(f"The item {item_name} can be found in warehouse1")
        else:
            print(f"The item {item_name} can be found in warehouse2")
        choice1_2 = input("Would you like to place an order for this item? Type 'Y' for yes and 'N' for no: ")
        if choice1_2 == "N":
            print("Thank you, goodbye!")
        elif choice1_2 == "Y":
            choice1_2_3 = int(input("How many would you like to order?: "))
            if choice1_2_3 <= sum_of_item:
                print(f"That's fine {name}, you order of {choice1_2_3} X {item_name} has been placed successfully.")
            elif choice1_2_3 > sum_of_item:
                print("The amount you have requested exceeds the total amount")
                choice1_2_4 = input("Would you like to order the maximum? Type 'Y' for yes and 'N' for no:  ")
                if choice1_2_4 == "Y":
                    print(f"That's fine {name}, you order of {sum_of_item} X {item_name} has been placed successfully.")    
                else:
                    print(f"Ok, goodbye {name}!")
    else:
        print(f"Unfortunately, {item_name} is out of stock.")
# Else, if they pick 3
elif choice1 == 3:
    print(f"Thank you for your time {name}, goodbye! ")
# Else
else:
    print("The input you have given me isn't valid. Pleas try again.")
# Thank the user for the visit
print(f"Thank you for your time {name}, we hope to see you again soon.")


"""Command line interface to query the stock.

To iterate the source data you can use the following structure:

for item in warehouse1:
    # Your instructions here.
    # The `item` name will contain each of the strings (item names) in the list.
"""