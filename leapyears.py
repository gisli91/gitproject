leapyear= 0 
notaleapyear = 0 


for x in range(1900, 2021):
    
    if x % 4 == 0:
        if x % 100:
            notaleapyear += 1
            print(x, "Its not a leayear")
        else:
            notaleapyear += 1
            (x, "Its not a leapyear")
        if x % 400 == 0:
            print(x,"Its a leapyear")
        else:
            notaleapyear += 1
            print(x, "Its not a leapyear") 

    else: 
        notaleapyear += 1
        print(x, "Its not a leapyear")