"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/92335

< k진수에서 소수 개수 구하기 >
"""
import math


def find_prime(x):
    if x < 2:
        return False
    # 2부터 x의 제곱근까지
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def covert(n, k):
    num = ""
    while n > 0:
        n, mod = divmod(n, k)
        num += str(mod)
    return num[::-1]


def solution(n, k):
    answer = 0
    k_num = covert(n, k)

    number = k_num[0]
    for i in range(1, len(k_num)):
        if k_num[i] == "0":
            if len(number) != 0 and find_prime(int(number)):
                answer += 1
            number = ""
        else:
            number += k_num[i]

    if k_num[-1] != "0":
        if len(number) != 0 and find_prime(int(number)):
            answer += 1

    return answer


"""
- split으로 더 간단하게
"""
def solution(n, k):
    answer = 0
    k_num = covert(n, k).split("0")

    for num in k_num:
        if len(num) != 0 and find_prime(int(num)):
            answer += 1

    return answer


# n = 437674
# k = 3

n = 110011
k = 10

# n = 1
# k = 3
print(solution(n, k))
