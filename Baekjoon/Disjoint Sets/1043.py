"""
백준 - https://www.acmicpc.net/problem/1043

< 거짓말 >
"""

from sys import stdin

input = stdin.readline


def find_parent(x):
    # union이 음수이면, 현재의 노드가 부모 노드임을 의미
    if union[x] < 0:
        return x
    else:
        union[x] = find_parent(union[x])
        return union[x]


def find_union(x, y):
    a = find_parent(x)
    b = find_parent(y)
    # 둘의 부모 노드가 같다면, 같은 집합에 속함을 의미
    if a == b:
        return False
    # 둘의 부모 노드가 다르다면, 같은 집합에 속하도록 설정
    else:
        union[a] += union[b]
        union[b] = a
        return True


# 사람의 수, 파티의 수
n, m = map(int, input().split())
union = [-1] * (n + 1)

truth_length, *truth = map(int, input().split())

parties = []
for _ in range(m):
    _, *party = map(int, input().split())
    parties.append(party)

if truth_length == 0:
    print(m)
    exit()

# 진실을 아는 사람들 그룹화
for i in range(1, truth_length):
    a, b = truth[i - 1], truth[i]
    find_union(a, b)

changed = True
while changed:
    changed = False
    for party in parties:
        flag = False
        # 해당 파티에 진실을 아는 사람이 존재하는지 확인
        for p in party:
            if find_parent(p) == find_parent(truth[0]):
                flag = True
                break

        # 진실을 아는 사람이 한 명이라도 있다면, 그룹화
        if flag:
            for i in range(1, len(party)):
                a, b = party[i - 1], party[i]
                if find_union(a, b):
                    changed = True

answer = 0
# 최종적으로 모든 파티에서 진실을 아는 사람이 단 한명도 없는 파티 수를 센다
for party in parties:
    for p in party:
        if union[p] != -1:
            break
    else:
        answer += 1
print(answer)

"""
고려하지 못했던 반례
5 4
1 5
2 1 2
2 2 3
2 3 4
2 4 5
"""
