def Fibo(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return Fibo(n-2)+Fibo(n-1)

if __name__ == '__main__':
    print (Fibo(9))