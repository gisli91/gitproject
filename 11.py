Max_range = 10
Min_range = 1


#user_int = int(input("Input a position between 1 and 10: "))

#This function takes in the orginal number from the user and the chars input to move the "o" and returns a new value
#while making sure it does not go out of range. 
def input_interperator(user_str, user_int):

    if user_str == "l" and user_int > Min_range:
        user_int -= 1
    if user_str == "r" and user_int < Max_range:
        user_int += 1
    return user_int

#This function prints the "o" on the x-axis with a given input  
def mover(user_int):
    left_str = "x" * Max_range
    right_str = "x" * Max_range
    mid_str = "o"
    print_str = left_str[Min_range:user_int] + mid_str + right_str[user_int:Max_range]
    print(print_str)
    
    

def print_instructions(user_int = int(input("Input a position between 1 and 10: "))):
    print("l - for moving left\nr - for moving right\nAny other letter for quitting")
    return user_int



#mover(print_instructions())

#print_instructions()


loop_condition = True

while loop_condition:

    user_str = input("Input your choice: ")
    user_int = input_interperator(user_str, mover(print_instructions()))
    

    

    mover(user_int)

#To stop the loop
    if user_str != "l" and user_str != "r":
        loop_condition = False