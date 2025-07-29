a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

minNum = min(a,b)

for i in range(1,minNum+1):
    if a%i==0 and b%i==0:
        hcf = i

print(f"HCF/GCD of {a} and {b} is: {hcf}")