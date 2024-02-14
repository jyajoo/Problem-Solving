'''
< 정렬된 배열에서 특정 수의 개수 구하기 >
'''
import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
nums = list(map(int, input().split()))

start = bisect_left(nums, x)
end = bisect_right(nums, x)
print(end - start)

"""
7 2
1 1 2 2 2 2 3
"""
