 백준 4344(내거)
N=int(input())
for i in range(N):
    list=input().split( )
    list.pop(0)
    superior = 0
    for elm in range(len(list)):
        list = [int(item) for item in list]
        if list[elm]>sum(list)/len(list):
            superior+=1
    print("{0:.3f}%".format(superior*100/len(list)))
    
#백준 4344(남거)
n=int(input())
exec("""
l=list(map(int,input().split()))
m=l.pop(0)
print("%.3f%%"%(sum(1.0 for x in l if x>sum(l)/m)/m*100))
"""*n)    