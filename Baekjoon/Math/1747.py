"""
백준 - https://www.acmicpc.net/problem/1747

< 소수&팰린드롬 >
"""

"""
백준 - https://www.acmicpc.net/problem/1747

< 소수&팰린드롬 >
"""
import sys, math

input = sys.stdin.readline


def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


def is_palindrome(x):
    x = str(x)
    for i in range(len(x) // 2):
        if x[i] != x[-1 - i]:
            return False
    return True


n = int(input())
result = n
while True:
    if is_prime(result) and is_palindrome(result):
        break
    result += 1
print(result)

"""
- 에라토스테네스의 체
"""
import sys, math

input = sys.stdin.readline


# def find_prime(x):
#     primes = [True] * (x + 1)
#     p = 2

#     primes[0] = primes[1] = False

#     # p가 n의 제곱근보다 작거나 같을 때까지 반복
#     while p * p <= n:
#         # 현재 p가 소수인 경우
#         if primes[p] == True:
#             # p의 배수들은 소수가 아니다.
#             for i in range(p * p, n + 1, p):
#                 primes[i] = False
#         p += 1

#     return [p for p in range(n + 1) if primes[p]]


def is_prime(x):
    if x <= 1:
        return False

    if x <= 3:
        return True

    if x % 2 == 0 or x % 3 == 0:
        return False

    p = 5
    # p가 n의 제곱근보다 작거나 같을 때까지 반복
    while p * p <= x:
        # 2와 3을 미리 체크하였기에, 남은 소수부터는 6의 배수 + 1이거나 6의 배수 - 1의 형태이다.
        if x % p == 0 or x % (p + 2) == 0:
            return False
        p += 6
    return True


def is_palindrome(x):
    x = str(x)
    for i in range(len(x) // 2):
        if x[i] != x[-1 - i]:
            return False
    return True


n = int(input())
result = n
while True:
    if is_prime(result) and is_palindrome(result):
        break
    result += 1
print(result)
