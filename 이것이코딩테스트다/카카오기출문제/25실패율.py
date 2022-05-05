def solution(N, stages):

    rates = {}
    stages.sort()

    # stage == 5
    for stage in range(1, N+1):
        bunja = stages.count(stage) # 0
    
        try:
            point = stages.index(stage) # 5 없음
        except:
            rates[stage] = 0
            continue
        bunmo = len(stages[point:])
        rates[stage] = bunja / bunmo # 0/
        
        
        # https://programmers.co.kr/learn/courses/30/lessons/42889
        # 풀긴했는데 정렬로 다시 
