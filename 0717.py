#백준 15649(내거)

N,M= map(int,input().split())

nums=[]
def NM():
    if len(nums) == M:
        print(*nums)

    for i in range(1,N+1):
        if i  not in nums:
            nums.append(i)    
            NM()
            nums.pop()

NM()