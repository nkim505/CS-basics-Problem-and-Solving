# 321p
n = input()
lenth = len(n)
summary = 0

for i in range(lenth //2):
  summary += int(n[i])
  
for i in range(lenth //2, lenth):
  summary -= int(n[i])

if summary == 0:
  prink("LUCKY")
  
else:
  print("READY")
 
