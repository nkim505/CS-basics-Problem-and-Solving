# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# 56분 100%
def solution(E, L):
    
    result = 2 # starts with entrance fee
    
    e_hr = int(E[:2])
    e_min = int(E[3:])
    l_hr = int(L[:2])
    l_min = int(L[3:])


    # within 1 hour
    if e_hr == l_hr: 
        result += (1 * 3)
    
    # within 1 hour
    elif (l_hr - e_hr == 1) and (l_min <= e_min) : 
        result += (1 * 3)

    else:
        if l_min - e_min >= 0:
            hrs = l_hr - e_hr
            mins = l_min - e_min
            result += (3 * 1) + (4 * (hrs - 1))
            result += (4 * min(mins, 1)) # mins 0이면 0, 1보다 크면 무조건 1 곱하게 됨.

        elif l_min - e_min < 0:
            hrs = l_hr - e_hr - 1
            mins = 60 + l_min - e_min
            result += (3 * 1) + (4 * (hrs - 1))
            result += 4 * min(mins, 1) # mins 0이면 0, 1보다 크면 무조건 1 곱하게 됨.
        
    return result
