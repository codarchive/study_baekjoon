# 백준 1932 정수삼각형 (내거)

Nn= int(input())
tri_nums=list(list(map(int,input().split())) for _ in range(n))

sum_n=dict()
sum_ns=[]

def tri(depth=0):
    import copy
    global sum_n
    global sum_ns
    for i in range(len(tri_nums[depth])):
        
        if depth==0:
            sum_n[(0,0)]=tri_nums[0][0]
            
        else :

            a=[]
            if (depth-1,i) in sum_n.keys():
                a.append(sum_n[(depth-1,i)]+tri_nums[depth][i])
            if (depth-1,i-1) in sum_n.keys():
                a.append(sum_n[(depth-1,i-1)]+tri_nums[depth][i])
            if a !=[]:
                sum_n[(depth,i)]=copy.deepcopy(max(a))
for i in range(n):
    tri(i)

print(max(sum_n.values()))             


# 백준 1932(남거)
import sys
n = int(input())
x = [0]*n
for i in range(n):
  a = list(map(int, sys.stdin.readline().split()))
  x[0: i + 1] = [a[j] + max(x[j - 1], x[j]) for j in range(i + 1)]
print(max(x))
