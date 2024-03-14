import math
a = int(input(" a : "))
b = int(input(" b : "))
c = int(input(" c : "))
delta = b * b - 4  * a * c
if delta > 0 :
    x1=float(-b+ math.sqrt(delta)) / (a * 2)
    x2=float(-b- math.sqrt(delta)) / (a * 2)

else :
    if delta==0:
        x = float(-b/(2*a))
        print (f"x1={x} x2={x}")
    else:
        print("not root")