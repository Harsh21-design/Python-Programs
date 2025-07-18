# Armstrong number (# 153, 407)
n = 407 
num = n
sum = 0
while n>0:
   dig =  n%10
   sum += dig ** 3
   n = n//10

if num == sum:
    print("Armstong no.",num)
else:
    print(-1)
