top_num = int(input("Upper number for the range: ")) # Do not change this line
num_sum = 0



for x in range(1, top_num+1):
    num_sum = 0
    for i in range(1, x):
        if x % i == 0:
            num_sum += i
    if num_sum == x:
        print(num_sum)
    
    
    