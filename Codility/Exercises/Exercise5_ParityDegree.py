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
# 하지만 Integer Decimal Occurrence 라는 말이 뜬다. 이게 뭐지?
# "If you’re using this test for recruitment we recommend swapping it with: IntegerDecimalOccurrence."
# 정수로만 해줘봄


#### 3번째 시도
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
            N = int(N / 2)
            count += 1
        
        result = count
    
    return result
  
