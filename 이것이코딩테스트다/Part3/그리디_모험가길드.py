# 311p part3 Q01 모험가 길드
# 가장 공포도가 높은 사람 순으로 배열하고
# 가장 공포도가 높은 사람 먼저 그룹을 만드는데, 공포도가 높은 사람들로 구성하기
# 공포도가 낮으면 더 작게 그룹을 쪼갤 수 있으므로 (최대 그룹 구하기 문제)

# 모험가 수 n
# 각 모험가의 공포도의 값을 n 이하의 자연수로 주어짐, 각 자연수는 공백으로 구분
n=int(input())
array = list(map(int, input().split()))
 
array.sort(reverse=True) # 큰 수부터 내림차순 정렬

groups = []

while array :
    x = array[0] #가장 큰 공포도를 가진 사람의 공포도 x확인    
    if x <= len(array):#공포도만큼 데려갈 남은 사람이 존재해야함(본인 포함)
        groups += [array[0:x]] #0~x-1까지 총 x명의 사람을 모아서 group에 넣음
        array = array[x:]  #0~x-1까지 사람들은 제외하고 array 리셋
    else:
        break

print(len(groups))

# 테스트 케이스-1
# 5
# 2 3 1 2 2
# 답 : 2
# 테스트 케이스-2
# 8
# 4 4 3 3 3 3 2 2
# 답 : 2
