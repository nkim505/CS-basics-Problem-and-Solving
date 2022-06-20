# 참고: https://codingpractices.tistory.com/72)
s = input()

cnt = 0
for i in range(len(s)-1):
    if s[i] != s[i+1]:
        cnt += 1
        
print((cnt+1)//2)
