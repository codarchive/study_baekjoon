#백준  11053 (가장 긴 증가하는 부분 수열-내거)

N=int(input())
arr=list(map(int,input().split()))
dp=[1]*N
hi=1
for cnt,val in enumerate(arr):
    idxs=[]
    for idx in range(0,cnt):
        if arr[idx]<val:
            idxs.append(dp[idx])
    if len(idxs)>0:
        dp[cnt]=max(idxs+[dp[cnt]])+1
        if dp[cnt]>hi:
            hi=dp[cnt]

print(hi)