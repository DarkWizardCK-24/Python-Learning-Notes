hours_worked = int(input("Enter hours you worked this week: "))
hourly_rate = int(input("Enter your hourly rate: "))

if hours_worked <= 40:
    total_wage = hours_worked * hourly_rate
    print("Your total wage is: $" + str(total_wage))
else:
    overtime_hours = hours_worked - 40
    overtime_wage = overtime_hours * (hourly_rate * 1.5)
    total_wage = (40 * hourly_rate) + overtime_wage
    print("Your total wage is: $" + str(total_wage))