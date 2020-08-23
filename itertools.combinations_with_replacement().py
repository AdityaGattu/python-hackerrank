from itertools import combinations_with_replacement
 
st,n = input().split()

for ele in combinations_with_replacement(sorted(st),int(n)):
    print(''.join(ele),end="\n")
