data = [{'user name':'ashik','password':'1234','mark':'272'},
        {'user name':'vishnu','password':'1357','mark':'256'},
        {'user name':'sayi','password':'9876','mark':'280'},
        {'user name':'vijay','password':'7532','mark':'295'},
        {'user name':'mohan','password':'3399','mark':'267'}]
name=(input('Enter user name : '))
pasw=(input('Enter password : '))
found=0

for i in data:
    if i['user name'] == name and i['password'] == pasw:
        print("Login successful")
        print("Mark : " , i['mark'])
        found +=1
        break
if found !=1:
    print("Invalid user name or password!")
    
