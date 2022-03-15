'''
< 동전 0 >
동전은 오름차순으로 입력된다.

- 가장 단위가 큰 동전부터 거슬러준다.
'''

n, k = map(int, input().split())
coins = []
result = 0

for _ in range(n):
    coins.append(int(input()))

coins = coins[::-1]         # range(n-1, -1, -1)

for i in coins:
    if i <= k:   # 거스를 동전의 단위가, k보다 작은지 확인

        # 남은 돈(k % i) 가장 작은 단위의 동전보다는 커야 한다. or 나눠떨어지는 경우
        if k % i >= coins[n-1] or k % i == 0:
            result += k // i   
            k %= i
        

print(result)

'''
[DEL]
- 거스를 동전의 단위가 k보다 작은지 확인 
- 남은 돈이 가장 단위가 작은 동전보다 큰지 확인
- 남은 돈이 0일 경우, break
'''

n, k = map(int, input().split())
coins = []
result = 0

for _ in range(n):
    coins.append(int(input()))

coins = coins[::-1]        

for i in coins:
    result += k // i
    k %= i
    if k % i == 0: break

print(result)
