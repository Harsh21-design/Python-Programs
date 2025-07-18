# 2. Prime number check and series
n = 47
if n == 1:
    print("")
else:
    for i in range(2,n//2+1):
        if n%i==0:
            print("Not Prime")
            break
    else:
        print("Prime Number")

# 2 3 5 7 11 13 17 19 23 29
n = 30
for num in range(2,n+1):
    for i in range(2,num//2+1):
        if num % i == 0:
            break
    else:
        print(num,end=" ")
    
