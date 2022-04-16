# Find longest sequence of zeros only between 1s in binary representation of an integer.
# example: 1000 -> 0, 10010001 -> 3, 10100-> 1 ...
# link: https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

def solution(N):
    # write your code in Python 3.6
    binary = bin(N)[2:] # 10진수 숫자를 2진수 문자열로 바꾸는 함수 ex. bin(10)-> 0b1010
    count_one = [] # 2진수에서 1들의 위치를 저장
    zerobins = [] # 1 사이의 sequence를 계산한 값을 넣을 array

    # 1의 위치값 저장하기
    for i in range(len(binary)):
        if binary[i] == '1' : #bin()이 문자열로 나오기 때문에 1에 '' 처리.
            count_one.append(i)
    
    if len(count_one) < 2 : #10000, 1000 의 경우 count_one =>[0], len(count_one)=1
        return 0

    else:
        for j in range(len(count_one)-1): # 나머지 경우 중, 1111, 1100 등의 경우는 아래 식에서 역시 0으로 처리된다.((n+1)-(n)-1 이므로)
            zerobins.append(count_one[j+1]-count_one[j]-1)
    
    return max(zerobins)

    pass
    
    
# After code review, I got the simplest solution from my peer.
# The simplest solution

def solution_2(n: int):
    binary = bin(n)[2:]
    length_max = 0
    length_max_temp = 0
    for i in range(len(binary)):
        if binary[i] == '0':
            length_max_temp +=1
            length_max = max(length_max, length_max_temp)
        else:
            length_max_temp = 0
    return length_max

# Even shorter solution

def solution_3(n): 
    binary = bin(n)[2:]
    rep = binary.split('1')
    rep = rep[1:(len(rep)-1)]
    if len(rep) > 0: return max([len(x) for x in rep])
    return 0

# Even much shorter solution

def solution_4(n): 
    rep = bin(n)[2:].split('1')
    rep = rep[1:(len(rep)-1)]
    return max([[0],[len(x) for x in rep]][len(rep) > 0])
    
    
