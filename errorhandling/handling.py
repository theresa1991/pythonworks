#num1=int(input("Enter a number"))
#num2=int(input("Enter number 2"))
#res=num1/num2
#try:
    #res=num1/num2
    #print(f"result is {res}")
#except Exception as e:
    #print(e)
    #num2=int(input("Enter another number:"))
    #res=num1/num2
    #print(f"res is {res}")
#finally:
    #print("database transaction")
    #print("file transaction")

#age=int(input("Enter age"))
#if age<18:
    #raise Exception("Not eligible for booster dose")
#else:
    #print("eligible")

ph=input("Enter a phone number")
if ( len ( ph ) != 10 ) :
    raise Exception("Invalid phone number")
else:
    print("Valid")
