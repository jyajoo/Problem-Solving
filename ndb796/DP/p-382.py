'''
< 편집 거리 >
'''

str1 = input()
str2 = input()

n, m = len(str1), len(str2)

dp = [[0] * (m + 1) for _ in range(n + 1)]

# 공백과 비교되는 경우 초기화
for i in range(1, n + 1):
    dp[i][0] = i
for j in range(1, m + 1):
    dp[0][j] = i

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

print(dp[n][m])

'''
'''
str1 = input()
str2 = input()
n, m = len(str1), len(str2)
previous = [i for i in range(m + 1)]
current = [0] * (m + 1)

for i in range(1, n + 1):
    current[0] = i
    for j in range(1, m + 1):
        if str1[i - 1] == str2[j - 1]:
            current[j] = previous[j - 1]
        else:
            current[j] = min(current[j - 1], previous[j], previous[j - 1]) + 1
    previous, current = current, previous

print(previous[-1])
