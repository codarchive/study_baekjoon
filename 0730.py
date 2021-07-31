#백준 14888(내거)

import sys
import copy

N=int(input())
nums=list(map(int,sys.stdin.readline().split()))
arr=list(map(int,sys.stdin.readline().split()))
init_cal_arr=arr[0:]


vals=[]


def calcul(i):
    if i==0:
        cal_result= val[depth-1]+nums[depth]
    elif i==1:
        cal_result= val[depth-1]-nums[depth]
    elif i==2:
        cal_result= val[depth-1]*nums[depth]
    else:
        if val[depth-1]*nums[depth]>0:
            cal_result= int(val[depth-1]/nums[depth])
        else: 
            cal_result= 0-int(abs(val[depth-1])/abs(nums[depth]))
    return cal_result
        

val=[nums[0]]*N
vals=[]
depth=0

def dfs(cal_arr={0:init_cal_arr}):
    global vals
    global val
    global depth
    
    if set(cal_arr[depth])=={0}:
        tmp_v=copy.copy(val[depth])
        vals.append(tmp_v)


    else:
        for i in range(4):
            if cal_arr[depth][i]>0:
                
                depth+=1
                val[depth]=calcul(i)
                
                cal_arr[depth]=cal_arr[depth-1][0:]
                cal_arr[depth][i]-=1
                
                dfs()
                depth-=1
    
    
dfs()
print(max(vals))
print(min(vals))