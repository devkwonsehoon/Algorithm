# 과제 1
input = 20


def find_prime_list_under_number(number):
    answer = []

    for n in range(2, number+1):
        for i in answer:
            if n % i == 0 and i * i <= n:
                break
        else:
            answer.append(n)

    return answer


result = find_prime_list_under_number(input)
print(result)
