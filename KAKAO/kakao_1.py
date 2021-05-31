def solution(s):
# s = {{2},{2,1},{2,1,3},{2,1,3,4}}
    S = s[2:-2].split("}, {")
    print(S)

    for i in range(len(S)):
        s = S[i].split(",")
        numArr.append(set(s))


s = "{{2}, {2,1}, {2,1,3}, {2,1,3,4}}"
solution(s)
    
