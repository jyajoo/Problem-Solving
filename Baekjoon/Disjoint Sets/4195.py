"""
백준 - https://www.acmicpc.net/problem/4195

< 친구 네트워크 >
"""
import sys
input = sys.stdin.readline
from collections import defaultdict

def find_parent(x):
    # x가 union의 부모 노드인 경우, 그대로 리턴
    if union[x] < 0:
        return x
    else:
        # x가 부모 노드가 아닌 경우, 계속 부모 노드를 찾으러 거슬러 올라가지 않도록 저장해준다.
        union[x] = find_parent(union[x])
        return union[x]
    
def find_union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    # 둘의 부모가 같다면, 이미 같은 집합에 속함을 의미
    if x == y:
        return abs(union[x])
    else:
        # 부모가 같지 않다면, 같은 집합에 속하도록 반영한다.
        union[x] += union[y] # y가 속한 집합을 합하여 x 집합에 반영
        union[y] = x # y의 부모 노드를 x로 반영한다
        return abs(union[x])


t = int(input())
for _ in range(t):
    f = int(input())
    friendship = []
    name = {}
    union = [-1] * (f * 2)
    count = 0
    for _ in range(f):
        a, b = input().split()
        friendship.append((a, b))
        
        for p in [a, b]:
            if name.get(p) == None:
                name[p] = count
                count += 1

        x, y = name.get(a), name.get(b)
        print(find_union(x, y))



