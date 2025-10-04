'''
백준 - https://www.acmicpc.net/problem/1912

< 연속합 >

n개의 수열 중 연속된 몇 개의 수 중 가장 큰 합
1 <= n <= 100000(10만)
-1000 <= 수 <= 1000
시간복잡도 <= O(N)여야 한다
'''
'''
dp[i] = i번째 원소가 무조건 포함된 경우의 최대합
시간 복잡도는 O(N)
'''
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [-int(1e9)] * n

for i in range(n):
    dp[i] = max(dp[i - 1] + arr[i], arr[i])

print(max(dp))