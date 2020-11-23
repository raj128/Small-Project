import string
import random
s1=string.ascii_lowercase
s2=string.ascii_uppercase
s3=string.digits
s4=string.punctuation
s=[]
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
random.shuffle(s)
while True:
    passlen=input("Enter the passward length:")
    a=passlen.isdigit()
    if a==True:
         break
    else:
        print("Enter the number like 4,7,11 etc")
passlen=int(passlen)    
print("".join(s[0:passlen]))
    
    
