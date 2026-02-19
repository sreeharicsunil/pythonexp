#usinf fungtion ,find area and perimeter of a rectangle.

l=int(input("Enter the length of the rectangle : "))
b=int(input("Enter the bredth of the rectangle : "))

opt=int(input("Chose wether area (1) or perimeter (2) to find, Enter the option : "))

def area(l,b):
    a = l*b
    return a

def perimeter(l,b):
    p = 2*(l+b)
    return p


if opt == 1:
    print("Area is : ", area(l,b))
elif opt == 2:
    print("Preimeter is : ", perimeter(l,b))
else:
    print("Invalid opt")
    
    
