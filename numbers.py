divisors = 0
mod_int1 = 0
mod_int2 = 0
mod_sum = 0



for first_loop_var in range(99, 1, -1):
    #This variable will be the first digit each iteration
    mod_int1 = first_loop_var % 10
    #This variable will be the second digit each iteration
    mod_int2 = first_loop_var // 10

    mod_sum = mod_int1 + mod_int2

    if mod_sum ** 2 == first_loop_var and first_loop_var != 1:
        print(first_loop_var)

#Here is the double loop that cycles through all numbers from 1 to 100, checks if they are divisible and if so adds to the divisors counter. 
for numerator in range(1, 100):
    divisors = 0 

    for denominator in range(1, numerator+1):
        if numerator % denominator == 0:
            divisors +=1
            
    if divisors == 10:
        print(numerator)

    