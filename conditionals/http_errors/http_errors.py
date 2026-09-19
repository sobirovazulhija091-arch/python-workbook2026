num = int(input())

if 100 <= num <= 199:
    print("Informational")
elif 200 <= num <= 299:
    print("Success")
elif 300 <= num <= 399:
    print("Redirection")
elif 400 <= num <= 499:
    print("Client Error")
elif 500 <= num <= 599:
    print("Server Error")
else:
    print("Unknown status code")