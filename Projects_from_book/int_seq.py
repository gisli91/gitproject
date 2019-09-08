


user_int = 0
number_of_ods = 0
number_of_evens = 0
highest_int = 0
total_input = 0


user_int = int(input("Enter an integer: "))

#Highest int starting point
highest_int = user_int

#Heres the arithemitc and the loop
while user_int > 0:

    total_input += user_int

    print("Cumulative total:",total_input)

    #Here is what decides which is the highest number
    if highest_int < user_int:
        highest_int = user_int
    
    #The even number counter 
    if user_int % 2 == 0:
        number_of_evens += 1

    #The odd number counter
    if user_int % 2 != 0:
        number_of_ods += 1
    
    #Promt user for another int
    user_int = int(input("Enter an integer: "))
    
    #Evaluate the totals
    if user_int <= 0:
        print("Largest number:",highest_int)
        print("Count of even numbers:",number_of_evens)
        print("Count of odd numbers:",number_of_ods)



