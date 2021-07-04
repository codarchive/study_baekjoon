# 백준 2231(내거)

num_in = int(input())

N=list(str(num_in))

k = num_in- (int(N[0])+len(N[1:])*9)

list_n=[]

for i in range(k,num_in+1):
    sum_i=sum(map(int,list(str(i))))
    if i+sum_i == num_in:
        list_n.append(i)
    
if list_n != []:

    M=min(list_n)
    print(M)
else:
    print(0)
