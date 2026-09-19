num=float(input())
if num < 3 * 10**9:
    print("Radio Waves")
elif num < 3 * 10**12:
    print("Microwaves")
elif num < 4.3 * 10**14:
    print("Infrared Light")
elif num < 7.5 * 10**14:
    print("Visible Light")
elif num < 3 * 10**17:
    print("Ultraviolet Light")
elif num < 3 * 10**19:
    print("X-Rays")
else:
    print("Gamma Rays")