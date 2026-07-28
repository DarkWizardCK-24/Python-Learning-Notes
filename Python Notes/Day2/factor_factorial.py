num = int(input("Enter a number: "))
prod = 1
for i in range (1, num+1):
    if num % i == 0:
        prod *= i
        print(i)
print(f"Product of factors of {num}: {prod}")