# 프로*래머* 위클리 챌린지
def solution(price, money, count):    
    result= money-sum(list(range(1,count+1)))*price
    if result>=0:
        answer=0
    else:
        answer=abs(result)

    return answer