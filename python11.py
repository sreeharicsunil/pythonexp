atm_bal=100000

data={'101':{'Name':'Ashik','Pin':2211,'Acc_amt':50600},
      '102':{'Name':'Manu','Pin':6611,'Acc_amt':15000},
      '103':{'Name':'Ram','Pin':1022,'Acc_amt':25000},
      '104':{'Name':'Hari','Pin':9023,'Acc_amt':4500},
      '105':{'Name':'Rohin','Pin':2551,'Acc_amt':1500000},
      }



def auth():
    if amt_bal < 10000:
        print("Insuffitiont ATM balence!!!!")
        
    acc_no = input("Enter Account Number :")

    if acc_no in data:
        pasw = int(input("Enetr your 4 Digit PIN : "))
        if data[acc_no]['Pin'] == pasw:
            print("Welcom")
            display(acc_no)
        else:
            print("Invalid password")
            auth()
    else:
        print("Enter valid Account Number : ")
        auth()
        
def display(acc_no):
    opt = int(input("1)Balence\n2)Withdraw\n3)Exit\nEnter option : "))
    if opt == 1:
        print("Balence : ",data[acc_no]['Acc_amt'])
        display(acc_no)
    elif opt == 2:
        w=int(input(("Enter the amount (limit per withdrow is 10000) : ")))
        if w not in range(1,10001):
            print("Execed limit")
            display(acc_no)
        else:
            print(f"Sucesfully widrown {w}")
            data[acc_no]['Acc_amt'] -= w
            amt_bal -= w
            display(acc_no)
            
    elif opt == 3:
        auth()
    else:
        auth()
        
auth()
