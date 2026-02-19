data = [{'name':'Hari','place':'TVM','mark':'60'},
        {'name':'Manu','place':'KLM','mark':'75'},
        {'name':'Ram','place':'TVM','mark':'40'},
        {'name':'Vishnu','place':'KNR','mark':'97'},
        {'name':'Jos','place':'ERK','mark':'90'}]

for i in data:
    print(i['name'])

print('\n\n')

for i in data:
    if int(i['mark'])<50:
        print("mark < than 50 : ",i['name'],i['place'],i['mark'])

    if int(i['mark'])>50:
        print("mark >  50 : ",i['name'],i['place'],i['mark'])

print('\n\n')

for i in data:
    m = int(i['mark'])
    if m<95 :
        i['mark'] = str(m + 5)
        
    print(i['name'],i['place'],i['mark'])

print('\n\n')

for i in data:
    m = int(i['mark'])
    if m > 90:
        i['Grade']='A'
    elif m in range (80,90):
        i['Grade']='B'
    elif m in range (70,80):
        i['Grade']='C'
    elif m in range (60,70):
        i['Grade']='D'
    elif m in range (50,60):
        i['Grade']='E'
    else:
        i['Grade']='F'
        
    print(i['name'],i['place'],i['mark'],i['Grade'])

print('\n\n')

dpt = [{'dep_name':'MCA','Roll_no':'10'},
       {'dep_name':'Btech','Roll_no':'43'},
       {'dep_name':'EEE','Roll_no':'23'},
       {'dep_name':'MCA','Roll_no':'7'},
       {'dep_name':'EEE','Roll_no':'28'}]

j=0
for  i in data:
        i['department'] = dpt[j]
        print(i['name'],i['place'],i['mark'],i['Grade'],i['department'])
        j+=1
        
    
