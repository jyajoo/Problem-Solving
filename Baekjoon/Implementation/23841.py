import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]

for lst in arr:
    lst1 = lst[: m // 2]
    lst2 = lst[m // 2 :]

    for i in range(m // 2):
        if lst1[i] != ".":
            lst2[-(i + 1)] = lst1[i]

        if lst2[i] != ".":
            lst1[-(i + 1)] = lst2[i]

    print(''.join(lst1) + ''.join(lst2))
