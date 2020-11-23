print("Find out greatest no")
while True:
    a=input("Enter the number1=")
    d=a.isdigit()
    if d==True:
        break
    else:
        print("Enter the integer like 3,6,1")
a=int(a)
while True:
    b=input("Enter the number2=")
    e=b.isdigit()
    if e==True:
        break
    else:
        print("Enter the integer like 3,6,1")
b=int(b)
while True:
    c=input("Enter the number3=")
    f=c.isdigit()
    if f==True:
        break
    else:
        print("Enter the integer like 3,6,1")
c=int(c)        
largest=a
if b>largest :
    largest=b
if c>largest:
    largest=c
print("largest no is=",largest)    

    
