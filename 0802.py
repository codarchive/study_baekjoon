#백준 9184(내거)

w_dic=dict()
def w_cal(a,b,c):

    if a <= 0 or b <= 0 or c <= 0 :
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w_cal(20,20,20)

    elif (a,b,c) in w_dic.keys():
        return w_dic[(a,b,c)]

    elif a < b and b < c:
        ans=w_cal(a, b, c-1)+w_cal(a, b-1, c-1)-w_cal(a, b-1, c)
        w_dic[(a,b,c)]=ans
        return ans
    
    else:
        ans=w_cal(a-1, b, c) + w_cal(a-1, b-1, c) + w_cal(a-1, b, c-1) - w_cal(a-1, b-1, c-1)
        w_dic[(a,b,c)]=ans
        return ans 
a=b=c=1

while True:
    a,b,c= map(int,input().split())
    if (a,b,c) == (-1,-1,-1):
        break
    ans=w_cal(a,b,c)
    w_dic[(a,b,c)]=ans
    print("w{} = {}".format((a,b,c),ans))  