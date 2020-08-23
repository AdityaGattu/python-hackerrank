from itertools import permutations
st,n=input().split()
for ele in permutations(sorted(st),int(n)):
    print(''.join(ele),end="\n")
