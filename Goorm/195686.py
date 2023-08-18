"""
구름톤 챌린지 - https://level.goorm.io/exam/195686/%EC%99%84%EB%B2%BD%ED%95%9C-%ED%96%84%EB%B2%84%EA%B1%B0-%EB%A7%8C%EB%93%A4%EA%B8%B0/quiz/1

<완벽한 햄버거 만들기>
"""
import sys

input = sys.stdin.readline

N = int(input())
K = list(map(int, input().split()))

top_val = max(K)
top = K.index(top_val)
K1 = K[:top]
K2 = K[top:]
result = 0

for i in K1:
    result += i

prev = K2[0]
for i in K2:
    result += i
    if i > prev:
        result = 0
        break
    prev = i
print(result)

"""
"""
import sys

input = sys.stdin.readline

N = int(input())
K = list(map(int, input().split()))

top_val = max(K)
top = K.index(top_val)

K1 = K[:top]
K2 = K[top:]

K1.sort()
K2.sort(reverse=True)

sortedK = K1 + K2
result = 0
for i in range(N):
    if K[i] != sortedK[i]:
        result = 0
        break
    else:
        result += K[i]

print(result)

"""
"""
import sys

input = sys.stdin.readline

N = int(input())
K = list(map(int, input().split()))

top_val = max(K)
top = K.index(top_val)

K1 = K[:top]
K2 = K[top:]

K1.sort()
K2.sort(reverse=True)

sortedK = K1 + K2
for i in range(N):
    if K[i] != sortedK[i]:
        print(0)
        break
else:
    print(sum(K))
