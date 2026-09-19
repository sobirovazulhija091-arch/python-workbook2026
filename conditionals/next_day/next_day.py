year = int(input())
month = int(input())
day = int(input())
is_leap = False
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    is_leap = True
if month in:
    max_days = 31
elif month in:
    max_days = 30
elif month == 2:
    max_days = 29 if is_leap else 28
else:
    max_days = 0 
day += 1
if day > max_days:
    day = 1
    month += 1
if month > 12:
        month = 1
        year += 1
print(f"{year}-{month:02d}-{day:02d}")