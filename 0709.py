# 백준 11650(내거)

import sys

N=int(input())
cord_li=[]

for _ in range(N):
    a,b=map(int,sys.stdin.readline().split())
    cord_li.append((a,b))

cord_li.sort()

for i in range(N):print(*cord_li[i]) 
