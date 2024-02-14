'''
< 고정점 찾기 >
'''
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

start = 0
end = n - 1
answer = -1
while start <= end:
    middle = (start + end) // 2

    if nums[middle] == middle:
        answer = middle
        break

    if nums[middle] < middle:
        start = middle + 1
    else:
        end = middle - 1

print(answer)
'''
5
-15 -6 1 3 7
'''