# 백준 1427(내거)
# 
N=input()

li=[N[i] for i in range(len(N))]

li.sort(reverse=True)

s=''
li=s.join(li)

print(li) 