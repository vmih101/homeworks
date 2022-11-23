import math

a = math.fabs(int(input("Input rectangle length: ")))
b = math.fabs(int(input("Input rectangle width: ")))
s = a*b
p = 2*(a+b)
print("Rectangle area: ", s)
print("Rectangle perimeter: ", p)
