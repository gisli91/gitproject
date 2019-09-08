import math

radius_int = input("Please input the radius of a circle: ")
radius_float = float(radius_int)

print("The radius of a circle is: ", radius_float*2*math.pi)
area = math.pi * (radius_float ** 2)
print("The area of a circle is : ", area)
if radius_float == 0b10:
    print("test")
print(id(area))
print(2e8)
print(2*10**8)