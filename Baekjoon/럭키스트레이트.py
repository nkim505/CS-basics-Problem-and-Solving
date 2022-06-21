s = input()
tmp = len(s)//2
left = 0
right = 0


for letter in s[:tmp]:
  left += int(letter)

for letter in s[tmp:len(s)]:
  right += int(letter)
  

if left == right :
  print("LUCKY")
  
else:
  print("READY")
  
