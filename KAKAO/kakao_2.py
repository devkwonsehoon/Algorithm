import sys
input = sys.stdin.readline

def solution(new_id):
    # 1
    new_id = new_id.lower()

    answer = ''
    
    # 2
    for x in new_id:
        if x.isalnum() or x in '-_.': answer += x

    # 3
    while '..' in answer: answer = answer.replace("..", ".")

    # 4
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer

    # 5
    if (answer == ''): answer += 'a'

    # 6
    if (len(answer) > 15): 
        answer = answer[:15]
        if (answer[-1] == '.'): answer = answer[:-1]

    # 7
    if (len(answer) <= 2):
        while(len(answer) < 3):
            answer += answer[-1]
    
    return answer

new_id = input()
print(solution(new_id))
