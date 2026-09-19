num = float(input())

if abs(num - 261.63) <= 1:
    print("C4")
elif abs(num - 293.66) <= 1:
    print("D4")
elif abs(num - 329.63) <= 1:
    print("E4")
elif abs(num - 349.23) <= 1:
    print("F4")
elif abs(num - 392.00) <= 1:
    print("G4")
elif abs(num - 440.00) <= 1:
    print("A4")
elif abs(num - 493.88) <= 1:
    print("B4")
else:
    print("No match")