num = float(input())
if num == 40:
    print("Quiet Room")
elif num == 70:
    print("Alarm Clock")
elif num == 106:
    print("Gas Lawnmower")
elif num == 130:
    print("Jackhammer")
elif num < 40:
    print("Quieter than Quiet Room")
elif num < 70:
    print("Between Quiet Room and Alarm Clock")
elif num < 106:
    print("Between Alarm Clock and Gas Lawnmower")
elif num < 130:
    print("Between Gas Lawnmower and Jackhammer")
else:
    print("Louder than Jackhammer")