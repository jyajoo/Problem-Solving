'''
백준 - https://www.acmicpc.net/problem/11497

< 통나무 건너뛰기 >
n개의 통나무가 원형으로 배치
난이도는 인접한 두 통나무 간의 높이 차의 최댓값으로 결정됨
최소 난이도를 출력

5 <= n <= 10000 (개수)
1 <= ㅣ <= 100000 (높이)
시간 복잡도 <= O(N^2)
'''
'''
1.   9
2.  5  7
3. 2    4
의 형태로 배치.
시간 복잡도는 O(NlogN)
'''
import sys
import heapq
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    minus_arr = [-i for i in arr]
    heapq.heapify(minus_arr)

    result_arr = deque()
    result_arr.append(-heapq.heappop(minus_arr))
    
    while minus_arr:
        if len(minus_arr) > 1:
            a, b = -heapq.heappop(minus_arr), -heapq.heappop(minus_arr)
            result_arr.append(a)
            result_arr.appendleft(b)
        else:
            result_arr.appendleft(-heapq.heappop(minus_arr))

    result = 0
    for i in range(n):
        result = max(result, abs(result_arr[i] - result_arr[i - 1]))
    print(result)