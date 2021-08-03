#백준 1904(내거)
N= int(input())
arrs=[]

arr=dict()
def fillN(depth=0):
    import copy
    global arrs
    global arr
    print(depth)
    for i in range(0,2):
        if depth==N:
            print("depth:{} and arr:{}".format(depth,arr))
            arrs.append(copy.copy(arr))
        
        elif list(arr.values())[0:depth+1].count(0)%2==1:
            arr[depth]=0
            print("add zeros")
            depth+=1
            print("go deeper")
            fillN(depth)
            depth-=1
            
        else:
            arr[depth]=i
            print("append {} to arr {}".format(i,arr))
            depth+=1
            print("go deeper")
            fillN(depth)
            depth-=1

fillN()
            