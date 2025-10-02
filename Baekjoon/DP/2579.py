'''
백준 - https://www.acmicpc.net/problem/2579

< 계단 오르기 >

1. 한 번에 1계단 또는 2계단을 오른다.
2. 연속된 3개의 계단을 밟을 수 없다. (시작점은 계단으로 안침)
3. 마지막 도착 계단은 꼭 밟아야 한다.
총 점수의 최댓값을 구하기

계단의 개수 <= 300
점수 <= 10000
'''

'''
DP - 작은 문제들을 재활용하며 큰 문제 해결하는 알고리즘

arr = [10, 20, 15, 25, 10, 20]

n = 1) 10, 10
n = 2) 20(이전 단계 선택 x), 10 + 20 = 30(이전 단계 선택)
n = 3) max(dp[1])(10) + 15(이전 단계 선택 x), dp[2][0] + 15(이전 단계 선택)
...

시간 복잡도는 O(N)
'''
import sys

input = sys.stdin.readline

n = int(input())
arr = [0] + [int(input()) for i in range(n)]
dp = [[0, 0] for _ in range(n + 1)]

if n <= 2:
    print(sum(arr))
else:
    # dp[i][0] : 이전 단계 선택안할 시 최대점수
    # dp[i][1] : 이전 단계 선택할 시 최대점수

    dp[1][0] = dp[1][1] = arr[1]
    dp[2][0] = arr[2]
    dp[2][1] = dp[1][0] + arr[2]

    for i in range(3, n + 1):
        dp[i][0] = max(dp[i - 2]) + arr[i]
        dp[i][1] = dp[i - 1][0] + arr[i]
    
    print(max(dp[n]))
