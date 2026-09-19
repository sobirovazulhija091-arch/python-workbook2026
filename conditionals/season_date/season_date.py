month = input().capitalize()
day = int(input())
if (month == "March" and day >= 20) or month in ["April", "May"] or (month == "June" and day <= 20):
    season = "Spring"
elif (month == "June" and day >= 21) or month in ["July", "August"] or (month == "September" and day <= 21):
    season = "Summer"
elif (month == "September" and day >= 22) or month in ["October", "November"] or (month == "December" and day <= 20):
    season = "Fall"
else:
    season = "Winter"
print(season)
#.capitalize is make June from june(input)