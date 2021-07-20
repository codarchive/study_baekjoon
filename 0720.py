#백준 15650(내거)
N,M= map(int,input().split())

nums=[]
k=1
def NM(k):
    for i in range(k,N+1):

        if i  not in nums:
            nums.append(i)    
            if len(nums) == M:
                print(*nums)
            k+=1
            NM(k)
            nums.pop()

NM(1)
