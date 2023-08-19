password = input("Enter new password: ")

length = len(password)

result = {}
if length >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digit"] = digit

uppercase = False
for i in password:
    if i.isupper():
        uppercase = True

result["uppercase"] = uppercase

if all(result.values()):
    print("Strong password")
else:
    print("Weak password")

if (length >= 8) and digit and uppercase:
    print("Strong password")
else:
    print("Weak password")
