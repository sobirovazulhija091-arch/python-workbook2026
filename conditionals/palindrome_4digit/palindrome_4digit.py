num=int(input())
N1=num//1000 
N2=(num//100)%10 
N3=(num//10)%10 
N4=num%10
if N1==N4 and N2==N3:
    print("palindrome")
else:
    print("not palindrome")    