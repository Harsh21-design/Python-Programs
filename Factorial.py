# Factorial
n = 5
f = 1
for i in range(1,n+1):
    f = f*i
print(f)

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
f = fact(5)
print(f)
