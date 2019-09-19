divisors = 0
mod_int1 = 0
mod_int2 = 0
mod_sum = 0



for first_loop_var in range(99, 1, -1):
    #This variable will be the first digit each iteration
    mod_int1 = first_loop_var % 10
    #This variable will be the second digit each iteration
    mod_int2 = first_loop_var // 10
    #Their sum
    mod_sum = mod_int1 + mod_int2
    if mod_sum ** 2 == first_loop_var and first_loop_var != 1:
        print("!",first_loop_var)

    #To make sure second loop starts with dividers as 0
    divisors = 0 

    #Second loop to iterate through each denominator 
    for denominator in range(1, first_loop_var + 1):
        if first_loop_var % denominator == 0:
            divisors += 1
    if divisors == 10:
        print("*",first_loop_var)


