num=int(input())
N1=num//100 
N2=(num//10)%10 
N3=num%10
if N1==N3:
    print("palindrome")
else:
    print("not palindrome")    