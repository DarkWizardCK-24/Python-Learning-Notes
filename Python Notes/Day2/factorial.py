num = int(input("Enter a number: "))
prod = 1
for i in range (1, num+1):
    prod *= i
print(f"Factorial of {num}: {prod}")