# Create variables for your name, age, city and whether you are learning Python. Print all four values.

name = input("Enter your name : ")
age = int(input("Enter your age : "))
city = input("Enter your city : ")
learning_goal = input("Enter your learning goal : ")
skill = bool(input(f"Are you learning {learning_goal} ? "))
print(name)
print(age)
print(learning_goal)
print(city)
print(skill)