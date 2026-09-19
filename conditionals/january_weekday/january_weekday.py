from math import floor
year = int(input())
dayofweek = (year + floor((year - 1) / 4) - floor((year - 1) / 100) + floor((year - 1) / 400)) % 7
match dayofweek:
    case 0:
        print("Sunday")
    case 1:
        print("Monday")    
    case 2:
        print("Tuesday") 
    case 3:
        print("Wednesday")    
    case 4:
        print("Thursday")    
    case 5:
        print("Friday")    
    case 6:
        print("Saturday")