#백준 9184(내거)

w_dic=dict()
def w_cal(a,b,c):
    i=0
    if a <= 0 or b <= 0 or c <= 0:
        i+=1
        return i
    elif a > 20 or b > 20 or c > 20:
        return w_cal(20,20,20)

    elif (a,b,c) in w_dic.keys():
        return w_dic[(a,b,c)]

    elif a < b and b < c:
        return w_cal(a, b, c-1)+w_cal(a, b-1, c-1)-w_cal(a, b-1, c)
    
    else:
        return w_cal(a-1, b, c) + w_cal(a-1, b-1, c) + w_cal(a-1, b, c-1) - w_cal(a-1, b-1, c-1)
    
        

a=b=c=1

while (a,b,c) != (-1,-1,-1):
    a,b,c= map(int,input().split())
    ans=w_cal(a,b,c)
    w_dic[(a,b,c)]=ans
    print("w({})={}".format((a,b,c),ans))
