''' print n naturel number ,
multi plication tabel of specific number from userup to 10,
fibonacci,
factorial'''

#print n naturel number
num = int(input("Enter a naturel number : "))

print(f"the first {num} naturel numbers are ")
for i in range(1,num+1):
    print(i)

print("\n\n")

#multi plication tabel of specific number from userup to 10,
print(f"multipication of {num} from 1 to 10 as follow ")
for i in range(1,11):
    mul = i*num
    print(f"{i} x {num} = {mul}")

print("\n\n")

#fibonacci
print(f"the first {num} fibonacci are : " , end=" ")

a=0
b=1

if num==0:
    print("not avilabel")
elif num==1:
    print(a)
elif num==1:
    print(a ,b )
else:
    print(a, b, end=" ")

    for i in range (2,num):
        c= a+b
        print(c, end=" ")
        a=b
        b=c

print("\n\n")

#factorial
print(f"{num}! = " , end = " ")

fact = 1
if num == 0:
    print(0)
else:
    for i in range(1,num+1):
        fact=fact*i
    

print(fact)

