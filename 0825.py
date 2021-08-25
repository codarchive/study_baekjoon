#백준  2156 (포도주시식-내거)

import sys
N=int(sys.stdin.readline())
arr=[int(sys.stdin.readline()) for _ in range(N)]
dp=[0]*N

if N<3:
    dp[N-1]=sum(arr)
elif N==3:
    dp[2]=max((arr[0]+arr[1]),(arr[1]+arr[2]),(arr[0]+arr[2]))
else:
    dp[0]=arr[0];dp[1]=arr[1]+arr[0]
    dp[2]=max((arr[0]+arr[1]),(arr[1]+arr[2]),(arr[0]+arr[2]))
    for n in range(3,N):
        dp[n]=max((dp[n-3]+arr[n-1]+arr[n]),(dp[n-2]+arr[n]),dp[n-1])