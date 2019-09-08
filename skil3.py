divider = 0
mod_int1 = 0
mod_int2 = 0


for x in range(0, 100):
    mod_int1 = 0
    mod_int2 = 0  
    for i in range(x):
        mod_int1 = x % 10
        mod_int2 = x // 10
        print(mod_int1, mod_int2)  
        if mod_int1 ** 2 + mod_int2 ** 2 == x:
            print(x)
