"""
코드 트리 - https://www.codetree.ai/missions/2/problems/n-permutations-of-k-with-repetition?&utm_source=clipboard&utm_medium=text

< k개 중에 1개를 n번 뽑기 >
"""

def dfs(num):
    if len(num) == n:
        print(*num)
        return

    for i in range(1, k + 1):
        num.append(i)
        dfs(num)
        num.pop()

# 1부터 k, n번 반복
k, n = map(int, input().split())

num = []
dfs(num)
