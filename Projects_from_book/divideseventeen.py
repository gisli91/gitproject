x = 0
counter = 0
for x in range(1, 1000):
    if x % 17 == 0:
        counter += 1
        print("Divisible by 17",x)
else:
    print(counter)