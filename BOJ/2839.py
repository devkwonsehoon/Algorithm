# 상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 
# 예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 
# 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.

# 상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 
# 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

sugar = int(input())
pack = 0

while sugar >= 0 :
  
  if sugar % 5 == 0:
    pack += (sugar//5)
    print(pack)
    break
  
  sugar -= 3
  pack += 1

else:
  print(-1)
