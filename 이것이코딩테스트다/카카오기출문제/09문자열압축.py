 
def solution(s):
    answer = 1001
    max_num = len(s)//2 
    x = 1 #세는 갯수
    cnt = 1
    lines = ""
    while x <= max_num:
        for i in range(0, len(s), x):
            if s[i:i+x] == s[i+x:i+x+x]:
                cnt += 1
            else:
                if cnt = 1:
                    lines = s[i:i+x]
                elif cnt > 1:
                    lines += str(cnt) + s[i:i+x]
                    cnt = 1 # 다시 cnt 초기화
        new_answer = len(lines)             
        answer = min(answer, new_answer)
        x += 1 # x+1개씩 슬라이싱 하는 단계로 넘어감
    return answer
    
    
    # 결과 실패
