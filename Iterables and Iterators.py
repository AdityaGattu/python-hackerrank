from itertools import combinations
n = input()
l = input().split()
k = input()
cnt = 0

comp_list = list(combinations(l,int(k)))

for ele in comp_list:
    if 'a' in ele : 
        cnt += 1
print(round(cnt/len(comp_list),3))

