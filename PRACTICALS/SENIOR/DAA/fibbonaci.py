def recursive(n):
    series=[]
    def fibrecur(num):
        if num<=0:
            return 0
        elif num == 1:
            return 1
        else:
            return fibrecur(num-1)+fibrecur(num-2)
    for i in range(n+1):
        series.append(fibrecur(i))
    print(f'recursive fibonacci is {n} : ')
    print(series)
n=int(input('enter value of n : '))
recursive(n)

def iterative(n):
    series=[]
    if n>=0:
        series.append(0)
    if n>=1:
        series.append(1)
    a,b=0,1
    for i in range(2,n+1):
        a,b=b,a+b
        series.append(b)
    print(f'iterative fibonacci is {n} :')
    print(series)

n=int(input('enter the value of n '))
iterative(n)
