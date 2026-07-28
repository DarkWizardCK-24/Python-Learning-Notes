num = int(input("Enter a number: "))
match = 0
for i in range(1, 51):
    if i % num == 0:
        match += 1 
print(f"Total match: {match}")
print(i)