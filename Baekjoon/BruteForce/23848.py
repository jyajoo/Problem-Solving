"""
백준 - https://www.acmicpc.net/problem/23848

< 등비수열의 합 >

1.
항이 3개일 때, 공비(r)가 가장 커질 수 있다.
1 + r + r^2라고 할 때, r^2가 n보다 작아야한다.
즉, r은 n^(1/2)보다 작다.

2.
공비가 가장 작은 2인 경우, 항의 개수가 가장 많아진다.
대략 2^40일 때, n의 최대값 넘기 때문에 항의 개수는 40보다 작다.
즉, 항의 개수는 log_2(n)보다 작다.

3.
공비(r)가 2, 항의 개수가 3일 때,
1 + 2 + 4 = 7
3 + 6 + 12 = 21

시작값이 1일 때의 총합이 n의 약수에 해당한 경우, 
n을 n의 약수로 나눈 몫만큼 곱하면 총합이 n이 되는 시작값을 구할 수 있다.

최종적으로 공비와 항의 개수에 따른 모든 경우의 수를 탐색한다.
시간 복잡도 : n^(1/2) * log_2(n)
"""
import sys
input = sys.stdin.readline

n = int(input())
flag = False
k = 0
sum_val = 0
for r in range(2, int(n ** (1/2)) + 1):
    if r ** 2 < n:
        k = 3
        sum_val = 1 + r + r * r
        while sum_val <= n:
            if n % sum_val == 0:
                flag = True
                break
            sum_val += r ** k
            k += 1
        if flag:
            break
    else:
        break

if flag:
    print(k)
    num = n // sum_val
    print(num, end = " ")
    for _ in range(k - 1):
        num *= r
        print(num, end = " ")

else:
    print(-1)
