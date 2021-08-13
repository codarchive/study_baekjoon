# 프로*래머* 레벨2

def solution(orders, course):
    import itertools
    import collections
    for num in course:
        cour_set=[]
        for set in orders:
            if len(set)>=num:
                cour_set+=list("".join(j) for j in itertools.combinations(set,2))
        answer=collections.Counter(cour_set)
    print(answer)
    return answer

solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4])