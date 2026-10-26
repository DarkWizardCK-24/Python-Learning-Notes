# Create variables for monthly income, rent, food expenses and travel expenses. Calculate the remaining balance and print a labelled summary.

income = int(input("Enter your income : "))
food = int(input("Enter your food expense : "))
travel = int(input("Enter your travel expense : "))
rent = int(input("Enter your rent : "))

balance = income - food - travel - rent

print(balance)
print(f"Your balance is {balance} after the food expense of {food}, rent {rent}, travel expense {travel} from the monthly income of {income}")