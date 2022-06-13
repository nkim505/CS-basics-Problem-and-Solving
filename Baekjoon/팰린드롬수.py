# 틀린 답
nums = []
results = []

while True:
    num = input()
    nums.append()
    if num == "0":
        break

nums = nums[:-1]

for num in nums:
    if len(int(num))%2 == 0:
        results.append("no")
    else:
        center = len(int(num))//2
        front = num[:center]
        rear = num[center+1:]
        reverse_rear = ''.join(reversed(rear))
        
        if int(front)-int(reverse_rear) ==0:
            results.append("yes")
        else:
            results.append("no")
        

for result in results:
    print(result)


# 런타임 오류
# NZEC	Exit code가 0이 아님
