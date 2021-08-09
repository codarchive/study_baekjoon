# 백준 2798(내거)

N,M=map(int,input().split())
nums=list(map(int,input().split()))[0:N] #list안하면 프린트해도 <map object at 0x06A6F9A0> 이딴식으로 나옴.

sum_of_3=[]

for i in range(0,N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if nums[i]+nums[j]+nums[k]-M <= 0:
                sum_of_3.append(nums[i]+nums[j]+nums[k])

print(max(sum_of_3))