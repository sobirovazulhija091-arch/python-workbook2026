a1=int(input())
a2=int(input())
a3=int(input())
if a1 < 90 and a2 < 90 and a3 < 90:
        return "Acute Triangle"
elif a1 == 90 or a2 == 90 or a3 == 90:
        return "Right Triangle"
elif a1 > 90 or a2 > 90 or a3 > 90:
        return "Obtuse Triangle"
elif (a1 + a2 + a3) != 180:
        return "Invalid Triangle"