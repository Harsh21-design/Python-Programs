# reverse of a string
# Method-1
str1 = "Hello!"
str2 = str1[::-1]
print(str2)

# Method-2
str1 = "hsraH"
str2 = ""
for i in str1:
    str2 = i + str2
print(str1)
print(str2)