#백준 9020

import math 
prime_num=[2]

for nums in range(3,10000):
   if False == (0 in [nums%div_num for div_num in range(2,int(math.sqrt(nums)+1))]):
       prime_num.append(nums)

#위를 통해 소수를 10000까지 쭉 구했습니다

T=int(input())
exec("""
number=int(input())

num_1 = num_2 = int(number/2)

i=0
while (0 <= (num_1-prime_num[i])):
    i+=1

num_1=(prime_num[i-1])
num_2 = number-num_1

while not(num_2 in prime_num):
    i-=1
    num_1 = prime_num[i-1]
    num_2 = number-num_1

print("{0} {1}".format(num_1,num_2))

"""*T)