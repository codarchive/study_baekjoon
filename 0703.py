
# 백준 1018(내거)


M,N=map(int,input().split())

board=[input() for _ in[1]*M]

board=[board[i].replace('W','1') for i in range(0,M)]
board=[board[i].replace('B','0') for i in range(0,M)]



mat_cnt=[]

for num1 in range(M-7):
    for num2 in range(N-7):
        
        for num in range(2):
            
            cnt=0
            for x in range(8):
                for y in range(8):

                    if int(board[num1+y][num2+x])==num: 
                        num= (num+1)%2

                    else:
                        num= (num+1)%2
                        cnt+=1
                num= (num+1)%2
        

                
            mat_cnt.append(cnt)

print(min(mat_cnt))                
