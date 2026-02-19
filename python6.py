#temprature alert message,optiaml temp range is 20 to 50 c,temprature vari range 15 to 30 c,message alert
import random
count = 0
for i in range (50):
    t = int(random.randint(15,31))
    if t < 20:
        print(t, "c ,alert! cold")
        count +=1
    elif t > 25:
        print(t, "c ,alert! Hot")
        count +=1
    else:
        None
    
print("total alert" , count)
