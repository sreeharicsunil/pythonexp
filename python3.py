#geatest of a ,b and c

a = 4
b = 7
c = 13

print(f"the thre numbers are a ={a} , b ={b} , c ={c} ")
 
if a>b and a>c :
    print("a is gratest")
elif b>a and b>c:
    print("b is graitest")
elif c>a and c>b:
    print("c is gratest")
else:
    print("the numbers are eaqal")

#odd or even
    
num = int(input("Enter a valid positive number : "))

mod = num % 2
if num == 0:
    print("the number is zero.")
elif mod == 0:
    print("the number is even")
else:
    print("the number is odd")
