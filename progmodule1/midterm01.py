

#Age of user
user_age = int(input("Enter your age: "))

if user_age < 0:
    print("Invalid age")
elif user_age <= 34:
    print("Young")
elif user_age <= 50:
    print("Mature")
elif user_age <= 69:
    print("Middle-aged")
elif user_age >= 70:
    print("Old")