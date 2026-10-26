# Create variables for income = 20000 and expenses = 12500. Calculate and print the remaining

income = int(input("Enter your income : "))
expense = int(input("Enter your expense : "))
balance = income - expense
print(balance)
print(f"Your balance is {balance} after the expense of {expense} from the monthly income of {income}")