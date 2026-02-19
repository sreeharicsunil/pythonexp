a=5
#1
print("1)")
for i in range (1,a+1):
    for j in range (1,i+1):
        print(i , end =" ")
    print(end = "\n")

print("\n")
#2
print("2)")
for i in range (1,a+1):
    for j in range (1,i+1):
        print(j , end =" ")
    print(end = "\n")

print("\n")
#3
print("3)")
for i in range (a):
    for j in range (i+1):
        print("*", end =" ")
    print(end = "\n")

print("\n")
#4
print("4)")
for i in range (a):
    for j in range (a-i):
        print("*", end =" ")
    print(end = "\n")

print("\n")
#5
print("5)")
for i in range (a):
    for j in range (i):
        print(" ", end =" ")
    for j in range (a-i):
        print("*", end =" ")
    print(end = "\n")

print("\n")
#6
print("6)")
for i in range (a+1):
    for j in range (a-i):
        print(" ", end =" ")
    for j in range (i):
        print("*", end =" ")
    print(end = "\n")
print(end = "\n")
#7
print("7)")
for i in range (a+1):
    for j in range (a-i):
        print(" " , end ="")
    for j in range (i):
        print("*" , end =" ")
    print(end = "\n")

print("\n")
#8
print("8)")
for i in range (a):
    for j in range (i):
        print("" , end =" ")
    for j in range (a-i):
        print("*" , end =" ")
    print(end = "\n")

print("\n")
#9
print("9)")
for i in range (a):
    for j in range (a-i):
        print(" " , end ="")
    for j in range (i):
        print("*" , end =" ")
    print(end = "\n")
for i in range (a):
    for j in range (i):
        print("" , end =" ")
    for j in range (a-i):
        print("*" , end =" ")
    print(end = "\n")

print("\n")

