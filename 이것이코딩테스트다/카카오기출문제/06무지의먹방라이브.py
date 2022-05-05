def solution(food_times, k):
    answer = 0
    sec = 0 
    
    while true:
        
        for i in range(len(food_times)):
            if sec < k:
                if food_times[i] != 0 and sec < k:
                    food_times[i] -= 1
                    sec += 1
                else: continue
            else:
                if food_time[i] != 0:
                    answer = 1
                else: answer = -1
    
    return answer
  
  # 2022.05.05 풀이. 결과 틀림.
