a=int(input("enter any number:"))
if (a%2==0):
    for i in range(1,11):
        print(i,"*", a, "=", i*a)
else:
    for i in range(1,a+1):
         print(i,"*", a, "=", i*a)
