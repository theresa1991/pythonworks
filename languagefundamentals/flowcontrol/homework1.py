#if num/3 print fizz if num/5 print buzz if num/15 fizzbuzz
#num=20
#print("fizz" if num%3==0 else "not divisible")
#print("buzz" if num%5==0 else "not divisible")
#print("fizzbuzz" if ((num%3==0)&(num%5==0)) else "not divisible")
num=13
res=""
if(num%3==0):
    res+="fizz"
if(num%5==0):
    res+="buzz"
print(res)
