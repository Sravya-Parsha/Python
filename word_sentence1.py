a=input("enter any sentence: ")
c=0
for i in range(len(a)):
    if a[i]== " " and a[i+1]!=" ":
        c=c+1
print(c+1)
