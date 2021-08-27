#백준  2565 (전깃줄-내거)

import sys

N=int(sys.stdin.readline())
line=dict()
for _ in range(N):
    a,b=sys.stdin.readline().split()
    line[int(a)]=int(b)
lineSort=sorted(line.items())
dp=[1]*N
for num,val in enumerate(lineSort):
    if num>0:
        hi=dp[num]
        bool=False
        for i in range(0,num):
            if lineSort[i][1]<val[1]:
                hi=max(dp[i],hi)
                bool=True
        dp[num]=hi+1*bool
print(N-max(dp))