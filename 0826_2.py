#백준  11054 (가장 긴 바이토닉 부분 수열-내거)

N=int(input())
arr=list(map(int,input().split()))

dp=[1]*N
dp2=[1]*N
arr2=arr[0:]
arr2.reverse()
for cnt,val in enumerate(arr):
    idxs=[]
    
    for idx in range(0,cnt):
        if arr[idx]<val:
            idxs.append(dp[idx])
    if len(idxs)>0:
        dp[cnt]=max(idxs+[dp[cnt]])+1

for cnt2,val2 in enumerate(arr2):    
    idxs2=[]
    for idx2 in range(0,cnt2):
        if arr2[idx2]<val2:
            idxs2.append(dp2[idx2])
    if len(idxs2)>0:
        dp2[cnt2]=max(idxs2+[dp2[cnt2]])+1
dp2.reverse()
sumArr=[a+b-1 for a,b in zip(dp,dp2)]
print(max(sumArr))