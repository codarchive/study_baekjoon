#백준 15652(내거)

N,M= map(int,input().split())

nums=[]
srt=1

def NM():
    global srt
    for i in range(srt,N+1):
        
        nums.append(i)
        if len(nums)==M:
            print(*nums)
        
        
        else:
            srt=i
            NM()
        nums.pop()



            


NM()