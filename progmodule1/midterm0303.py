first = int(input("First: "))
step = int(input("Step: "))

sum_of_series = first
counter = 0
step_int = first

print(first, end=" ")
while counter < 100:
    
    step_int += step
    print(step_int, end=" ")
    sum_of_series += step_int
    
    if sum_of_series >= 100:
        print()
        print("Sum of series:",sum_of_series)
        break