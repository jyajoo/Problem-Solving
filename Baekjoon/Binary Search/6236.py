'''
백준 - https://www.acmicpc.net/problem/6236

< 용돈 관리 >

n일간 사용할 금액 계산, 정확히 m번만 빼서 쓰기로 함
k원을 인출하여 하루를 보낼 수 있으면 그대로 사용,
모자라면 k원 또 인출

남은 금액이 그날 사용한 금액보다 많더라도
남은 금액을 통장에 넣고 다시 k원 인출 가능(m번을 채우기 위해)

최소 금액 k구하기

1 <= n <= 1000000
1 <= m <= n
1 <= 금액 <= 10000
'''
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

start = max(arr)
end = sum(arr)
result = int(1e9)
while start <= end:
    middle = (start + end) // 2
    count = 1
    current = middle 
    for i in arr:
        if i <= current:
            current -= i
        else:
            current = middle - i
            count += 1

    if count > m:
        start = middle + 1
    else:
        end = middle - 1
        result = min(result, middle)

print(result)