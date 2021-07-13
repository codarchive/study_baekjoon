# 백준 1181(내거)
import sys
N=int(input())
li=[]
for _ in range(N):
    li.append(sys.stdin.readline().rstrip())

li=list(set(li))

li_dic=sorted(li)
leng=len(li)
li_new={li_dic[i]:len(li_dic[i])*leng+i for i in range(leng)}
li_new=li_new.items()
li_new=sorted(li_new, key=lambda x: x[1])

for i in range(len(li)):print(li_new[i][0]);