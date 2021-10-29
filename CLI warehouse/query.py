#!/usr/bin/env python3

from data import stock

# Welcome message
print("Welcome to the Warehouse Ordering System")
# Assigning the user name to a variable
name = input("To proceed further please enter your name here: ")
# Welcome the user
print(f"Welcome back {name}!")
# Show the menu and ask the user to pick a choice
print("What would you like to do next?\n1. List items in the warehouse\n2. Search for an item and place an order\n3. Quit")
choice1 = int(input("Select the operation you would like to process by entering 1, 2 or 3: "))
# If they pick 1
if choice1 == 1:
    print("\nItems in warehouse 1:\n")
    for item in stock:
        print("-",item)
    print("\nItems in warehouse 2:\n")
    for item in stock:
        print("-",item)
# Else, if they pick 2
elif choice1 == 2:
    order = "Y"
    while order == "Y":
        item_name = input("Please enter the name of the item you are looking for here: ")
        if item_name in stock or item_name in stock:
            sum_of_item = stock.count(item_name) + stock.count(item_name)
            print(f"The total amount of {item_name} is: {sum_of_item}")
            if item_name in stock and item_name in stock:
                print(f"The item {item_name} can be found in both warehouses")
                if stock.count(item_name) > stock.count(item_name):
                    print(f"Warehouse1 has more of {item_name} with a total of: {stock.count(item_name)}")
                else:
                    print(f"Warehouse2 has more of {item_name} with a total of: {stock.count(item_name)}")
            elif item_name in stock:
                print(f"The item {item_name} can be found in warehouse1")
            else:
                print(f"The item {item_name} can be found in warehouse2")
            choice1_2 = input("Would you like to place an order for this item? Type 'Y' for yes and 'N' for no: ")
            if choice1_2 == "N":
                print("Thank you, goodbye!")
            elif choice1_2 == "Y":
                choice1_2_3 = int(input("How many would you like to order?: "))
                if choice1_2_3 <= sum_of_item:
                    print(f"\nThat's fine {name}, your order of {choice1_2_3} X {item_name} has been placed successfully.")
                    print(f"\nWould you like to order anything else while you're logged in?")
                    order = input("Enter 'Y' for yes or 'N' for no: ")
                    if order == "N":
                        print("That's fine.")
                        break
                elif choice1_2_3 > sum_of_item:
                    print("The amount you have requested exceeds the total amount")
                    choice1_2_4 = input("Would you like to order the maximum? Type 'Y' for yes and 'N' for no:  ")
                    if choice1_2_4 == "Y":
                        print(f"That's fine {name}, your order of {sum_of_item} X {item_name} has been placed successfully.") 
                        print(f"Would you like to order anything else while you're logged in?")
                        order = input("Enter 'Y' for yes or 'N' for no: ")
                        if order == "N":
                            print("That's fine.")
                            break
                    else:
                        print(f"Ok, goodbye {name}!")
    else:
        print(f"Unfortunately, {item_name} is out of stock.")
# Else, if they pick 3
elif choice1 == 3:
    print(f"")
# Else
else:
    print("The input you have given me isn't valid. Pleas try again.")
# Thank the user for the visit
print(f"Thank you for your time {name}, we hope to see you again soon.")