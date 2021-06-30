#백준 2839(내거)
N=int(input())
Big_bag=N//5

while (N-Big_bag*5)%3 != 0:
    Big_bag-=1
    if Big_bag<0:
        print("-1")
        exit()
print(int(Big_bag+(N-Big_bag*5)/3))

