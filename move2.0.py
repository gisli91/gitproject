Max_range = 10
Min_range = 1





def get_int():
    
    user_int = int(input("Please enter int: "))
    return user_int

def get_str():
    global user_str
    user_str = input("Input your choice: ")
    return user_str


def input_interperator(some_int, user_str):
    global user_int
    if user_str == "l" and user_int > Min_range:
        user_int -= 1
    if user_str == "r" and user_int < Max_range:
        user_int += 1
    return user_int

def print_instructions():
    print("l - for moving left\nr - for moving right\nAny other letter for quitting")

def mover(user_int):
    left_str = "x" * Max_range
    right_str = "x" * Max_range
    mid_str = "o"
    print_str = left_str[Min_range:user_int] + mid_str + right_str[user_int:Max_range]
    print(print_str)
    
mover(get_int())

print_instructions()


while True:
    get_str()
    mover(input_interperator(user_int, user_str))