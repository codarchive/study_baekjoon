
N,M=map(int,input().split())

num=[1,2,3,4,5,6,7,8]
fst_set=num[0:M]
lst_set=sorted(num[N-M:N],reverse=True)

chg_set=fst_set[0:M]
while chg_set !=lst_set:
    if chg_set.count(chg_set[i-1]) ==1:
        print(*chg_set) 
    chg_set[-1]= chg_set[-1]+1
    for i in range(M):
        if chg_set[i] > N:
            chg_set[i-1]=chg_set[i-1]+1
            chg_set[i:] = fst_set[0:len(chg_set[i:])]

print(*lst_set)
       