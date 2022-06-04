num1=200
num2=200
num3=200
if num1>num2 and num1>num3:
    if num2>num3:
        print("the second largest number is",num2)
    else:
        print("The second largest number is",num3)
elif num2>num1 and num2>num3:
    if num1>num3:
        print("the second largest no",num1)
    else:
        print("the second largest number is",num3)
elif num3>num1 and num3>num2:
    if num1>num2:
        print("The second largest number is",num1)
    else:
        print("the second largest number is",num2)
else:
    print("all numbers are equal")