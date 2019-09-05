n = int(input("Enter the length of the sequence: ")) # Do not change this line

counter = 0

#Need 3 ints which change values since the sequence is int1 + int2 + int3
first_int = 1
second_int = 1
third_int = 0
printed_int = first_int



for x in range(n):

    print(printed_int)
    
    
    first_int, second_int = second_int, third_int
    third_int = printed_int
    printed_int = first_int + second_int + third_int
    
    
    