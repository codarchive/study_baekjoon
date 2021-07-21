#백준 15651(내거)

N,M= map(int,input().split())

nums=[]

def NM():

    for i in range(1,N+1):
        nums.append(i)
        if len(nums)==M:
            print(*nums)
        
        
        else:
            NM()
        nums.pop()



            


NM()