# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    tmp = set(lottos) & set(win_nums)
    hits = len(tmp)
    
    missings = lottos.count(0)
    missings    

    ranks = [6,6,5,4,3,2,1]

    return [ranks[hits+missings], ranks[hits]]
