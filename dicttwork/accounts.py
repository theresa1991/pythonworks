accounts = [
    {
        "acno": 1000, "ac_type": "savings", "balance": 5000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1001, "ac_type": "savings", "balance": 6000, "transactions": [
        {"to": 1000, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1002, "ac_type": "current", "balance": 8000, "transactions": [
        {"to": 1001, "amount": 700, "note": "ebill", "method": "g-pay"},
        {"to": 1000, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 800, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1003, "ac_type": "credit", "balance": 15000, "transactions": [
        {"to": 1001, "amount": 1500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 800, "note": "geto", "method": "neft"},
        {"to": 1000, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },
    {
        "acno": 1004, "ac_type": "savings", "balance": 50000, "transactions": [
        {"to": 1001, "amount": 500, "note": "ebill", "method": "g-pay"},
        {"to": 1002, "amount": 600, "note": "geto", "method": "neft"},
        {"to": 1003, "amount": 100, "note": "erchrge", "method": "phone-pay"}
    ]
    },

]
#print details of 1002
#acc_details=[ac for ac in accounts if ac["acno"]==1002]#list comprehension
#print(acc_details)


#print savings account details
ac_savins=[ac["acno"]for ac in accounts if ac["ac_type"]=="savings"]
print(ac_savins)

#sort accounts based on balance by desc......list
print(sorted(accounts,key=lambda item:item["balance"],reverse=True))

#print all phone pay transactions
all_transactions=[ac["transactions"] for ac in accounts]
phon_pay=[trans for trn_list in all_transactions for trans in trn_list if trans["method"]=="phone-pay"]#flatten list
print(phon_pay)

stmt_list=[trans for trn_list in all_transactions for trans in trn_list if trans["amount"]>500]#fl
print(stmt_list)

all_transactions=[ac["transactions"] for ac in accounts]
credit_list=[trans for trn_list in all_transactions for trans in trn_list if trans["to"]==1002]#fl
print(credit_list)

#total aggregate of each payment method
pms={}
all_transactions=[ac["transactions"] for ac in accounts]
transactions=[t for tlist in all_transactions for t in tlist]
for transaction in transactions:
    p_method=transaction["method"]
    amount=transaction["amount"]
    if p_method in pms:
        pms[p_method]+=amount
    else:
        pms[p_method]=amount#key and value createdgpay 500 varum
print(pms)
print(max(pms.items(),key=lambda item:item[1]))#list of tuples then use max function  so using 1st location



