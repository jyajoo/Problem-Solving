"""
백준 - https://www.acmicpc.net/problem/25635

< 자유 이용권 >
"""
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
sum_val = sum(arr)
max_val = max(arr)

val = sum_val - max_val
result = 0
if val >= max_val:
    result = sum_val
elif abs(val - max_val) == 1:
    result = sum_val

# 가장 큰 값과 총 합에서의 남은 값의 차이가 1이상이라면,
# 예를 들어 남은 값이 2 + 2 + 2 = 6, max = 8이라면,
# 8282828이 되므로 남은 값의 2배에서 1을 추가한 값만큼만 이용 가능
else:
    result = val * 2 + 1

print(result)