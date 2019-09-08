first = int(input("First: "))
step = int(input("Step: "))

sum_of_series = first
counter = 0
step_int = first


while counter < 100:
    
    print(step_int, end=" ")

    if sum_of_series >= 100:
        print()
        print("Sum of series:",sum_of_series)
        break
    
    step_int += step
    
    sum_of_series += step_int
    
