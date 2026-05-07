from tabulate import tabulate
title=["Name","Age","Dept"]
data=["Pavi",19,"CSE"],["Raj",20,"AIML"],["Meera",34,"CSM"],["Teja",22,"CSO"]
res=tabulate(data,headers=title,tablefmt="pretty")
print(res)
