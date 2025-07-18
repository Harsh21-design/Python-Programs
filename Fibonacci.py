# Fibonacci series
n = 5
count = 0
a = 0
b = 1
while count <= n:
    print(a,end=" ") # 0 1 1
    c = a + b # 0 #1 # 2 
    a = b # 1 1
    b = c # 1 # 2
    count+=1

def fib(n):
    a, b = 0, 1
    for i in range(0,n+1):
        print(a,end=" ")
        c = a + b
        a = b
        b = c
    
fib(10)
