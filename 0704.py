
# 백준 1436(내거)


N=int(input())

num_li=[]
for i in range(666,5000000):
    if '666' in str(i): 
        num_li.append(i)

num_li.sort()

print(num_li[N-1])

