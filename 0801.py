#백준 1003(내거)
T= int(input())

cnt={0:[1,0],1:[0,1],2:[1,1]}

for i in range(3,41):
    cnt[i]=[cnt[i-1][0]+cnt[i-2][0],cnt[i-1][1]+cnt[i-2][1]]
    
for _ in range(T):
    print(*cnt[int(input())])

