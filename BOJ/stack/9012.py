# 6
# (())()) NO
# (((()())() NO
# (()())((())) YES
# ((()()(()))(((())))() NO
# ()()()()(()()())() YES
# (()((())()( NO


for _ in range(int(input())):
  sum = 0
  check = list(input())
  for x in check:
    if x == '(': sum += 1
    elif x == ')': sum -= 1
    
    if sum < 0: 
      print("NO")
      break
  
  if sum > 0: print("NO")
  elif sum == 0 : print("YES")

