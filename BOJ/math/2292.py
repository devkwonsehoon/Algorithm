# 숫자 N이 주어졌을 때, 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 
# 몇 개의 방을 지나가는지(시작과 끝을 포함하여)를 계산하는 프로그램을 작성하시오. 

# 예를 들면, 13까지는 3개, 58까지는 5개를 지난다.

n = int(*open(0))

first = 1
room = 1
room_count = 6

if n == 1 : print(1)
else :
  while True:
    first += room_count
    room += 1
    if n <= first:
      print(room)
      break
    room_count += 6
  

