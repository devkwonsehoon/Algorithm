import sys
input = sys.stdin.readline

a = list(map(int, input().split()))
b = list(map(int, input().split()))

if a == b:
    print(10, 10); 
    print('D')
else:
    a_score, b_score = 0, 0

    for i in range(10):
        if a[i] > b[i]:
            a_score += 3; win = 'A'
        elif a[i] < b[i]:
            b_score += 3; win = 'B'
        else:
            a_score += 1; b_score += 1;
    print(a_score, b_score)

    if a_score == b_score:
        print(win)
    else:
        print('A' if a_score > b_score else 'B')