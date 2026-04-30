names=["raM","RAJ","rose","JaCk","PaVi"]
age=[34,21,67,37,12]
res=list(zip(age,names))
res1=sorted(res)
pos=1
for i in res1:
    print("Rank {}: {} age is {} yrs old".format(pos,i[1],i[0]))
    pos=pos+1
