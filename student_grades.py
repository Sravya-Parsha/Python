names=["raM","RAJ","rose","JaCk","PaVi"]
marks=[[30,40,50],[66,77,55],[33,78,90],[87,97,57],[47,88,44]]
for i in range(5):
    p=sum(marks[i])//3
    if p>80:
        g="S"
    elif p<40:
        g="F"
    elif p>40 and p<60:
        g="B"
    else:
        g="A"
    print("{}.Mr/Ms {} has scored {}%-{} Grade".format(i+1,names[i].title(),p,g))
