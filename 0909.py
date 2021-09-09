#백준  11279 (최대 힙-내거)

import sys
N=int(sys.stdin.readline())
import heapq
arr=[]
for _ in range(N):
    num=int(sys.stdin.readline())
    if num==0 and arr!=[]:
        popEle=heapq.heappop(arr)
        print(popEle[1])
    elif num==0 and arr==[]:
        print(0)
    else:
        heapq.heappush(arr,(-num,num))