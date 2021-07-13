#백준 10814(내거)
import sys

N=int(input())
mem_li={}
for i in range(N):
    age, name=sys.stdin.readline().split()
    mem_li.update({i+int(age)*(N+1): age+' '+name})


mem_keys=sorted(mem_li)  

for i in mem_keys:print(mem_li[i])