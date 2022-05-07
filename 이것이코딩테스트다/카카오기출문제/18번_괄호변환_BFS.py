# https://velog.io/@chaegil15/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4%ED%8C%8C%EC%9D%B4%EC%8D%AC-2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EA%B3%B5%EC%B1%84-%EA%B4%84%ED%98%B8-%EB%B3%80%ED%99%98
def is_balanced(p):
    bal = 0
    for p_ in p:
        if p_ == '(':
            bal += 1
        else: bal -= 1
    return not(bool(bal))

def is_right(p):
    bal = 0
    if is_balanced(p) == False:
        return False
    for p_ in p:
        if p_ == '(':
            bal += 1
        else: bal -= 1
        if bal < 0: return False
    return True

def solution(p):
    if is_right(p) == True:
        return p
    for i in range(2, len(p)+1, 3):
        if is_balanced(p[:i]) == True:
            u, v = p[:i], p[i:]
            break
    
		if is_right(u) == True:
        return u + solution(v)
    else:
        result = '(' + solution(v) + ')'

					# 4-4
        for i in u[1:-1]:
            if i == '(':
                result += ')'
            else:
                result += '('
        return result
