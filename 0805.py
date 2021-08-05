#백준 1149(내거)

import sys
N= int(sys.stdin.readline())
mat=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
min_num={0:26}
min_idx=[0]
def afterTwoprice(k):
    global twoPrice

    for i in range(3):
        if i != min_idx[k]:
            for j in range(3):
                if j !=i:
                    twoPrice[(i,j)]=mat[k+1][i]+mat[k+2][j]
    minTwoprice=min(twoPrice.values())
    for a,b in twoPrice.keys():
        if twoPrice[(a,b)]==minTwoprice:
            min_idx.append(a)
            min_idx.append(b)
    return minTwoprice


for k in range(N-1):
    min_num[k+2]=min_num[k]+afterTwoprice(k)
    
    if list(min_num.keys())[-1]==N-1:
        break
    
print(min_num[N-1])