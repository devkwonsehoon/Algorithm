# 입력받은 그대로 출력한다.
while True:
  try:print(input())
  except EOFError: break

# 숏코딩
print(open(0).read())

# open(0) -> 파일 자체를 오브젝트로 읽어줌 
# read() -> 파일 전체의 내용을 하나의 문자열로 읽는다.
# readline() -> 한번에 하나의 라인을 읽어온다.
# readlines() -> 파일 전체를 한라인씩 읽어서 리스트로 만들어준다. 