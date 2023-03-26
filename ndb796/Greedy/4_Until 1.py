'''
< 1이 될 때까지 >

- 나눠떨어지지 않을 때까지 나누어준다.
- 나눠 떨어지지 않는다면, 1을 빼준다.
- 해당 연산들의 총 횟수를 구한다.
'''

n, k = map(int, input().split())

cnt = 0

while (n != 1):      # n이 1이 아닐 동안
    if(n % k == 0):  
        n //= k
    else:
        n -= 1
    cnt += 1

print(cnt)

'''
시간 초과 방지!

- 나누어 떨어지도록 조건을 맞춰준 후, N의 크기를 기하급수적으로 감소시킨다.
'''

n, k = map(int, input().split())
cnt = 0
while True:
    # n이 k로 나눠 떨어질 때까지 1 빼기
    target = (n // k) * k  # k로 나누어떨어지는 가장 큰 값을 찾는다.(나눠떨어지는지 확인을 하기 위함)
    cnt += n - target      # target이 될 때까지 1 빼기 연산 횟수를 구할 수 있다. (나눠떨어지는 경우, 결과가 0이 됨)
    n = target             # 1을 빼주었으니, 이제 n을 target으로 설정(나눠떨어진다면 그대로)

    if n < k: 
        break

    n //= k
    cnt += 1

# n이 k보다 작을 경우, 1이 될 때까지 빼기 연산 횟수를 더해준다.
result = n - 1
print(cnt)


'''
2023.03.26
'''
n, k = map(int, input().split())
result = 0
while True:
    if n == 1:
        break
    if n % k == 0:
        n /= k
    else:
        n -= 1
    result += 1
print(result)

'''
'''
n, k = map(int, input().split())
result = 0

while n >= k:
    while n % k == 0:
        n -= 1
        result += 1
    n /= k
    result += 1

while n > 1:
    n -= 1
    result += 1
print(result)