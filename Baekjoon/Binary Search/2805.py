'''
백준 - https://www.acmicpc.net/problem/2805

< 나무 자르기 >

나무 높이 중 H만큼에 절단기 작동
적어도 m미터의 나무를 가져가기 위한 높이의 최댓값
1 <= n <= 1000000 (나무 수)
1 <= m <= 2000000000 (나무 길이)
시간 복잡도 <= O(n)
'''
'''
이진 탐색
시간 복잡도 O(nlogn)
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort(reverse=True)

start = 0
end = max(trees)
result = 0
while start <= end:
    middle = (start + end) // 2
    val = 0
    for i in trees:
        if i > middle:
            val += i - middle
        else:
            break
    if val < m:
        end = middle - 1
    else:
        start = middle + 1
        result = max(result, middle)
print(result)