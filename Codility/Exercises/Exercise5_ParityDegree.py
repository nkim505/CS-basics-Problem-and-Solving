def solution(N):
    # write your code in Python 3.6
    
    result = 0
    
    # 홀수인 경우
    if N % 2 != 0:
        result = -1
    
    # 소인수분해하기
    else:
        count = 0
        while N % 2 == 0:
            N = N / 2
            count += 1
        
        result = count
    
    return result
  # 결과 correctness: 50%
  # -1이 아니고 0이 나와야하나 봄(홀수일 때)
  
  
  
  ## 다시 시도
def solution(N):
    # write your code in Python 3.6
    
    result = 0
    
    # 홀수인 경우
    if N % 2 != 0:
        result = 0
    
    # 소인수분해하기
    else:
        count = 0
        while N % 2 == 0:
            N = N / 2
            count += 1
        
        result = count
    
    return result

# score 100%
  
