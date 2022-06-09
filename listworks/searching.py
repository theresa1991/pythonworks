num=[12,15,9,78,45,79,23,44,68]
flag=0
for i in range(len(num)):
    if num[i]==12:
        print(f"number found at position {i}")
        break
else:
    print(f"number not found")
