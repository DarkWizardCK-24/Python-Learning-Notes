score = int(input("Enter your score: "))
if score >= 75:
    print("Congratulations! You cleared the cutoff.")
elif score >= 50:
    print("Close! You are on the waitlist.")
else:
    print("We regret to inform you that you did not clear the cutoff.")