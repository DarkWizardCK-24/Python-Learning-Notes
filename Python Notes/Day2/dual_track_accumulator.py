sum = 0
prod = 1
for i in range (1, 11):
    if i % 2 != 0:
        prod *= i
    else:
        sum += i
print(f"Product of odd numbers from 1 to 10: {prod}")
print(f"Sum of even numbers from 1 to 10: {sum}")