# 프로*래머* 레벨 2테스트

clothes=[["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]
cloths=clothes

cloths_dict=dict()
num=1
for i in range(len(cloths)):
    if cloths[i][-1] in cloths_dict.keys():
        num+=1
        cloths_dict[cloths[i][-1]]=num
    else:
        cloths_dict[cloths[i][-1]]=1
    

def solution(clothes_dict=cloths_dict):
    import copy
    a=sum(cloths_dict.values())
    b=0
    if len(cloths_dict.values())>1:
        b=1
        for i in cloths_dict.values():
            b=copy.deepcopy(b*i)
    answer = a+b
  
    return answer

solution()
