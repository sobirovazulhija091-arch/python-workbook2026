temp = float(input())
if temp < 0:
    print("solid")
elif temp == 0:
    print("solid or liquid")
elif temp > 0 and temp < 100:
    print("liquid")
elif temp == 100:
    print("liquid or gas")
else:
    print("gas")