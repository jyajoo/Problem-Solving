'''
백준 - https://www.acmicpc.net/problem/11053

< 가장 긴 증가하는 부분 수열 >
'''
'''
A = {10, 20, 10, 30, 20, 50}의 경우
{10, 20}, {30}, {50} 이며 길이는 4

1 <= n < 1000
1 <= 수 < 1000
'''
'''
n = 1) {'10'}
n = 2) {10, '20'}
n = 3) {10, 20}
n = 4) {10, 20, '30'}
n = 5) {10, 20, 30} 
n = 6) {10, 20, 30, '50'}

i단계의 수보다 마지막 원소가 작은 단계(i-1, i-2, ...)가 있다면 i단계의 수를 추가하여 길이 계산
dp[i] = i단계의 수가 마지막 원소가 되는 가장 긴 증가하는 부분 수열

시간 복잡도는 O(n^2)
'''
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [[] for _ in range(n)]
dp[0].append(arr[0])

for i in range(1, n):
    new = []
    length = 0
    for j in range(i):
        if arr[i] > dp[j][-1] and length < len(dp[j]) + 1: # 현재 수보다 마지막 원소가 작을 경우, 포함시키기
            new = dp[j] + [arr[i]]
            length = len(dp[j]) + 1
    if len(new) == 0:
        new = [arr[i]]
    dp[i] = new

result = 0
for i in dp:
    result = max(result, len(i))
print(result)

'''
수열의 마지막 원소(최소값)를 기록해나가기
dp[i - 1] = 길이가 i인 수열의 최소값이 되는 마지막 원소

arr의 원소를 순차적으로 탐색하며 해당 원소를 어느 배열에 삽입할 지 이진탐색
=> dp에서 arr의 원소보다 크거나 같은 첫번째 원소의 위치에 arr의 원소 반영
이는 아래와 같은 의미를 가진다
1. 해당 위치의 값 >= arr의 원소 경우, 수열의 마지막 원소의 최소값으로 업데이트
2. 해당 위치의 값 < arr의 원소 경우, 수열의 길이 확장

시간 복잡도는 O(NlogN)
'''
import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]]

for i in arr:
    idx = bisect_left(dp, i)
    if idx == len(dp):
        dp.append(i)
    else:
        dp[idx] = i

print(len(dp))