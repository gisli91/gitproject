dividers = 0
mod_int1 = 0
mod_int2 = 0
mod_sum = 0



for x in range(1, 100):
    #This variable will be the first digit each iteration
    mod_int1 = x % 10
    #This variable will be the second digit each iteration
    mod_int2 = x // 10
    #Their sum
    mod_sum = mod_int1 + mod_int2
    if mod_sum ** 2 == x:
        print(x)

    #To make sure second loop starts with dividers as 0
    dividers = 0 

    #Second loop to iterate through each denominator 
    for y in range(1, x + 1):
        if x % y == 0:
            dividers += 1
            if dividers == 10:
                print(x)
            

