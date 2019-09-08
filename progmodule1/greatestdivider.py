m = int(input("Input the first integer: ")) # Do not change this line
n = int(input("Input the second integer: ")) # Do not change this line

highernum = m
greatest_divider = 0

if n > m:
    highernum = n

for i in range(1, highernum):
    if n % i == 0 and m % i == 0:
        greatest_divider = i
print(greatest_divider)