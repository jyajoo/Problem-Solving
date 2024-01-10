"""
백준 - https://www.acmicpc.net/problem/11687

< 팩토리얼 0의 개수 >
"""
import sys
input = sys.stdin.readline

def find_zero(n):
    result = 0
    count = 1
    while True:
        zero = n // (5 ** count)
        if zero == 0:
            break
        result += zero
        count += 1

    return result


m = int(input())

end = 1
while True:
    zero = find_zero(end)
    if zero >= m:
        break
    end *= 5
start = end // 5

while True:
    if start > end:
        print(-1)
        break
    if find_zero(start) == m:
        print(start)
        break
    elif find_zero(end) == m:
        print(end)
        break

    total = start + end
    if total % 2 != 0:
        total += 5
        
    middle = total // 2

    zero = find_zero(middle)
    if zero == m:
        print(middle)
        break
    elif zero > m:
        end = middle - 5
    else:
        start = middle + 5

    
