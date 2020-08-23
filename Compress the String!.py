from itertools import groupby
data=input()
for key,grp in groupby(data): 
    l1=[]
    l1.append(len(list(grp)))
    l1.append(int(key))
    print(tuple(l1),end=" ")
