import sys
X= int(sys.stdin.readline())

def makeOne(num):

    if int(num) in num_dict.keys():
        return num_dict[int(num)]
    else:
        a=min((int(num%3+1)+makeOne(num//3)),int(num%2+1)+makeOne(num//2))
        num_dict[num]=a
        return a

num_dict={1:0,2:1,3:1}
makeOne(X)