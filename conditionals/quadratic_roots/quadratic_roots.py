import math
a = float(input())
b = float(input())
c = float(input())
D = b**2 - 4*a*c
if D < 0:
    print("No real roots")
elif D == 0:
    root = -b / (2*a)
    print(f"1 root: {root:.2f}")
else:
    root1 = (-b - math.sqrt(D)) / (2*a)
    root2 = (-b + math.sqrt(D)) / (2*a)
    print(f"2 roots: {root1:.2f} and {root2:.2f}")