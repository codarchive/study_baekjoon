#백준 4673(내거)
def selfnum():
    gen_set=set() #empty셋 정의할때 {}이렇게 하면 딕셔너리로 타입이 정해져서 이렇게 해야함 ㅡ,ㅡ;
    for i in range(1,10001):
        generated_nunber=i+sum(int(num) for num in str(i))
        gen_set= gen_set | {generated_nunber}
    self_list=list(set(range(1,10001))-gen_set)
    self_list.sort()
    
    for i in self_list:
        print(i)