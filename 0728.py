import sys
import copy

N=int(input())
nums=list(map(int,input().split()))
cal_arr=list(map(int,input().split()))
init_cal_arr=copy.copy(cal_arr)


vals=[]


def calcul(i):
    if i==0:
        cal_result= val+nums[cnt]
    elif i==1:
        cal_result= val-nums[cnt]
    elif i==2:
        cal_result= val*nums[cnt]
    else:
        if val*nums[cnt]>0:
            cal_result= int(val/nums[cnt])
        else: 
            cal_result= 0-int(abs(val)/abs(nums[cnt]))
    return cal_result
        

cnt=1
val=nums[0]
vals=[]

def dfs():
    global vals
    global cnt
    global val
    global cal_arr

    if set(cal_arr)=={0}:
        tmp_v=copy.copy(val)
        vals.append(tmp_v)
        cal_arr=copy.copy(init_cal_arr)
        cnt=1
        val=nums[0]

    else:
        for i in range(4):
            if cal_arr[i]>0:
                val=calcul(i)
                cal_arr[i]=cal_arr[i]-1
                print("we did {} cal".format(i))
                cnt+=1
                dfs()
                


dfs()