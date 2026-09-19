num = float(input())
if num < 2.0:
    print("Micro")
elif 2.0 <= num < 3.0:
    print("Very Minor")
elif 3.0 <= num < 4.0:
    print("Minor")
elif 4.0 <= num < 5.0:
    print("Light")
elif 5.0 <= num < 6.0:
    print("Moderate")
elif 6.0 <= num < 7.0:
    print("Strong")
elif 7.0 <= num < 8.0:
    print("Major")
elif 8.0 <= num < 10.0:
    print("Great")
else:
    print("Meteoric")