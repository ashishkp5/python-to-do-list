password = input("Enter the password:")

result = {}
if len(password) >= 9:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True
result["digit"] = digit

upper = False
for i in password:
    if i.isupper():
        upper = True
result["upper"] = upper

print(result.values())
print(all(result.values()))
