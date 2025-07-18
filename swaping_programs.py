# 1.swaping two numbers without temp
num1 = 10
num2 = 20
print(num1,num2)

num1, num2 = num2, num1

num1 = num1 + num2 # 10 + 20 = 30
num2 = num1 - num2 # 30 - 20 = 10
num1 = num1 - num2 # 30 - 10 = 20

num1 = num1 ^ num2 # XOR method
num2 = num1 ^ num2 
num1 = num1 ^ num2 

print(num1,num2)