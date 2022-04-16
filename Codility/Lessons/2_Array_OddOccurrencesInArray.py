# Find value that occurs in odd number of elements.
# Link: https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/start/

# trial 1
# ---------------------------------------------------
# task score: 66%, Correctness: 100%, Performance: 25%
# Detected time complexity: O(N**2)
# ---------------------------------------------------
def solution(A):
  seen = []
  for i in A:
      if i not in seen:
        seen += [i]
      else:
        seen.remove(i)
  uniq = seen[0]
  return uniq 
  
  pass

# trial 2
# After code review from a peer, I got better solutions
# ---------------------------------------------------
# task score: 66%, Correctness: 80%, Performance: 50%
# Detected time complexity: O(N**2)
# Test tests: small random test n=201 -> runtime error
# Performance tests: medium random test n=100003 -> runtime error
# Performance tests: big random test n=999,999, multiple repetitions -> runtime error
#----------------------------------------------------
def solution(A):
    dic = dict.fromkeys(A, 0) #dict.fromkeys(seq 키, value 값) 딕셔너리 생성 메소드: seq 생성하려는 dict key의 목록, value 생성하려는 값
    for i in A:
        dic[i] +=1 # dic[key] : dict의 해당 키의 값으로 +1이 할당된다. []안에 index 아니고 key 명칭이 들어간다는 것이 특징.
    return list(dic.keys())[list(dic.values()).index(1)] # list(dic.keys()): key값 반환한 것을 리스트로 만들고, list(dic.values()): 값 목록 구하기
                                                         # list(dic.values()).index(1): 특정한 원소가 몇 번째 처음으로 등장하는지 index 알려줌


# trial 3
# ---------------------------------------------------
# task score: 100%, Correctness: 100%, Performance: 100%
# Detected time complexity: O(N) or O(N*log(N))
# ---------------------------------------------------
def solution(A):
  dic = dict.fromkeys(A, 0)
  for i in A:
    dic[i]+=1
  inv_map = {v: k for k, v in dic.items()} # dic.items(): 키, 값 쌍 튜플로 리턴 예) dict_items([(8, 0), (1, 1), (7, 0)])
  key = list(filter(lambda x: x%2, inv_map.keys()))[0] # % 나누기 후 몫이 아닌 나머지 구함
  return list(dic.keys())[list(dic.values()).index(key)]
