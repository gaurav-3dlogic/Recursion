# 0 1 1 2 3 5 8 13 21 34
n = int(input("Enter a number: "))

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
print(fibo(n))