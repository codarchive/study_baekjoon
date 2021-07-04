N= int(input())

list_n=[1]*N

for i in range(0,N):
    list_n[i]=input().split()

count_list=list_n[0:]


rank_n=[1]*N

for j in range(0,N):
    cnt_num=0

    for k in range(0,N):
        
        if int(count_list[j][0]) < int(count_list[k][0]) and int(count_list[j][1]) < int(count_list[k][1]) :
            cnt_num+=1

        rank_n[j]=cnt_num+1

print(*rank_n[0:], sep=" ")  