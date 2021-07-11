# 백준 11651(내거)
import sys

N=int(input())
num_dic={}

for i in range(N): 
    x,y=map(int, sys.stdin.readline().split())
    num_dic[(y,x)]=(x,y)

an_idx=sorted(num_dic.keys())
    
for n in an_idx:    
    print(*num_dic[n])

