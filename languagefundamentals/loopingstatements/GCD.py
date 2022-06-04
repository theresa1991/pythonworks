num1=15
num2=35
hcf=1
limit=num1 if num1<num2 else num2
for i in range(2,limit+1):
    if(num1%i==0 and num2%i==0):
        hcf=i
print(hcf)