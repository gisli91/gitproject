d1 = int(input("Input first dice: ")) # Do not change this line
d2 = int(input("Input second dice: ")) # Do not change this line
dice_sum = d1 + d2

if (d1 >= 1 and d1 <= 6) and (d2 >= 1 and d2 <= 6):
    if dice_sum == 7 or dice_sum == 11:
        print("Winner")
    elif dice_sum == (2, 3, 12):
        print("Loser")
    else:
        print(dice_sum)
else:
    print("Invalid input")