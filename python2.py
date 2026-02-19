#create two list and each list should contain more than 6 elementse with uniqe and duplicate elements

a=[23,76,4,23,9]
b=[15,4,23,76,5]

c= a+b
print(c)

d={}

for i in c:
    d[i] = c.count(i)

print(d)

