from itertools import combinations
st,n=input().split()

for i in range(1,int(n)+1):
    for ele in combinations(sorted(st),i):
        print(''.join(ele),end="\n")
