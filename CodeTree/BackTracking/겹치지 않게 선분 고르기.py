"""
코드 트리 - https://www.codetree.ai/missions/2/problems/select-segments-without-overlap?&utm_source=clipboard&utm_medium=text

< 겹치지 않게 선분 고르기 >
"""

# 선분 종류를 1 ~ n개로 이루어진 조합을 구하여, 겹치는지 확인할 것
def find(count):
    global answer
    if count == n:
        if possible():
            answer = max(answer, len(result_lst))
        return

    result_lst.append(lines[count])
    find(count + 1)
    result_lst.pop()
    find(count + 1)


def possible():
    for i, (x, y) in enumerate(result_lst):
        for a, b in result_lst[i + 1 :]:
            if a <= x < b or a <= y <= b or x <= a <= y or x <= b <= y:
                return False
    return True


n = int(input())
lines = []
for _ in range(n):
    a, b = map(int, input().split())
    lines.append((a, b))

result_lst = []
answer = 0
find(0)
print(answer)
