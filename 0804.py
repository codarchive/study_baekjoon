#백준 9461(내거)

import sys
T= int(sys.stdin.readline())
for _ in range(T):
    N=int(sys.stdin.readline())
    arr=[1,1,1,2,2,3]
    if N<len(arr):
        print(arr[N-1])
    else:
        arr.extend([0]*(N-6))
        for i in range(N-6):
            
            arr[i+6]=arr[i+1]+arr[i+5]
        print(arr[N-1])
