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
#det_list=[ac for ac in accounts if ac["acno"]==1002]
#print(det_list)

#print savings account details
#savin_list=[ac for ac in accounts if ac["ac_type"]=="savings"]
#print(savin_list)

#sort accounts based on balance by desc......list
#sort_list=sorted(accounts,key=lambda ite:ite["balance"],reverse=True)
#print(sort_list)

##print all phone pay transactions
#all_transactions=[ac["transactions"] for ac in accounts]
#phone_pay=[trans for trans_list in all_transactions for trans in trans_list if trans["method"]=="phone-pay"]
#print(phone_pay)

#print detailsof transaction amount >500
#all_transactions=[ac["transactions"]for ac in accounts]
#amount_list=[trans for trn_list in all_transactions for trans in trn_list if trans["amount"]>500]
#print(amount_list)

#print all the credits to 1002
#all_transactions=[ac["transactions"]for ac in accounts]
#credit_list=[trans for trn_list in all_transactions for trans in trn_list if trans["to"]==1002]
#print(credit_list)

#total aggregate of each payment method
pms={}
all_transactions=[ac["transactions"] for ac in accounts]
transactions=[t for trn_list in all_transactions for t in trn_list]
for transaction in transactions:
    p_method=transaction["method"]
    amount=transaction["amount"]
    if p_method in pms:
        pms[p_method]+=amount
    else:
        pms[p_method]=amount
print(pms)