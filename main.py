a= int(input("enter the number "))
b= int(input("enter the number "))
try:
    c=a/b
except:
    print("b is divisor")
else:
    print(c)
finally:
    print("code executed")
    
