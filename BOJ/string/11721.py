# 알파벳 소문자와 대문자로만 이루어진 길이가 N인 단어가 주어진다.

# 한 줄에 10글자씩 끊어서 출력하는 프로그램을 작성하시오.

import sys
string = sys.stdin.readline()

for x in range(0, len(string), 10):
  print(string[x:x+10])

# 숏코딩
# string 자체를 10개씩 끊어서 출력하고 바로 자른값으로 새롭게 할당
# s=input()
# while s: print(s[:10]); s = s[10:] 
