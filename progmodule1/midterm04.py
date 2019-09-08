user_input = int(input("Number of stars: "))

for x in range(1, user_input+1):
    for i in range(x):
        print("*", end="")
    print()
