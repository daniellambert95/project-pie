#!/usr/bin/env python3

from data import stock

warehouse_1_stock = []
for warehouse_item_1 in stock:
    if warehouse_item_1['warehouse'] == 1:
        warehouse_1_stock.append(warehouse_item_1)

warehouse_2_stock = []
for warehouse_item_2 in stock:
    if warehouse_item_2['warehouse'] == 2:
        warehouse_2_stock.append(warehouse_item_2)

item_name = input("Please enter the name of the item you are looking for here: ")
item_name = item_name.lower()
item_name = item_name.title()

total_amount = 0



warehouse_1_amount = 0
for x,y in warehouse_1_stock:
    if x['state'] == item_name[0] and y['category'] == item_name[1]:
        warehouse_1_amount +=1

warehouse_2_amount = 0
for x,y in warehouse_2_stock:
    if x['state'] == item_name[0] and y['category'] == item_name[1]:
        warehouse_2_amount +=1

total_amount = (warehouse_1_amount + warehouse_2_amount)
print(f"The total amount of {item_name} is: {total_amount}")

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

choice1_2 = input("Would you like to place an order for this item?\n Type 'Y' for yes and 'N' for no: ")
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
            break
    elif choice1_2_3 > total_amount:
        print("The amount you have requested exceeds the total amount")
        choice1_2_4 = input("Would you like to order the maximum? Type 'Y' for yes and 'N' for no:  ")
        if choice1_2_4 == "Y":
            print(f"That's fine {name}, your order of {total_amount} : {item_name} has been placed successfully.") 
            print(f"Would you like to order anything else while you're logged in?")
            order = input("Enter 'Y' for yes or 'N' for no: ")
            if order == "N":
                print("That's fine.")
                break
        else:
            print(f"Ok, goodbye {name}!")
else:
print(f"Unfortunately, {item_name} is out of stock.")