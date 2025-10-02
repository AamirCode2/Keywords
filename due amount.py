def due_amount(x,y):
    return x - y

total_bill = int(input("Enter the total bill of the item/items you are purchasing: "))
money = int(input("Enter the total amount of money you are spending: "))

change = due_amount(money,total_bill)
print("Amount of change is: ", change)