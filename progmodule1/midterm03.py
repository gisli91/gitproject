first = int(input("First: "))
step = int(input("Step: "))

sum_of_series = 0

for number_step in range(first, 300, step):
    sum_of_series += number_step
    print(number_step, end=" ")
    if sum_of_series >= 100:
        print("Sum of series: ", sum_of_series)
        break
        