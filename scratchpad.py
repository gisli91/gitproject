
def deilarinn(x,y):
    m = x % y
    f = x / y
    q = x // y
    print("Mod: ", m, "Qout: ", q, "Float: ", f)



program_go = True

while program_go:
    
    x = int(input("x :"))
    y = int(input("y :"))

    deilarinn(x, y)

