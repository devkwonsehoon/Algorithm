import sys
input = sys.stdin.readline

case = int(input())

for _ in range(case):  
    
    floor = int(input())
    num = int(input())

    zero_floor = [x for x in range(1, num+1)]
    
    for _ in range(floor):
        for i in range(1, num):
            zero_floor[i] += zero_floor[i-1]
    
    print(zero_floor[-1])