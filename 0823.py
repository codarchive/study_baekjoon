#백준 10844 (쉬운 계단 수-내거)

def numStair(N):
    if N in dict_str.keys():
        return dict_str[N]
    else:
        arr=[0]*10
        arr[0]=numStair(N-1)[1]%1000000000
        for i in range(1,9):
            arr[i]=(numStair(N-1)[i-1]+numStair(N-1)[i+1])%1000000000
        arr[9]=numStair(N-1)[8]%1000000000
        dict_str[N]=arr
        return dict_str[N]

dict_str={1:[0,1,1,1,1,1,1,1,1,1]}  

print(sum(numStair(int(input())))%1000000000)