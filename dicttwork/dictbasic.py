#bank_acct={"accno":10001,"pname":"priya","type":"savings","balance":35000}
#print(bank_acct["accno"])
#print(bank_acct["pname"])
#print("ifsc" in bank_acct)
#bank_acct["ifsc"]=123456789
#print(bank_acct)
#print(bank_acct["ifsc"])
#bank_acct["balance"]=bank_acct["balance"]+35000
#print(bank_acct["balance"])
#print(bank_acct.get("pname"))
#bank_acct["micr"]="5g" if "micr" in bank_acct else "4g"
#print(bank_acct)
mobile={
    "mobile_name":"iphone",
    "price":45000,
    "display":"led",
    "ram":"6gb",
    "memory":"64gb"
}
if mobile["price"]>40000:
    mobile["price"]+=1000
else:
    mobile["price"]+=500
print(mobile)