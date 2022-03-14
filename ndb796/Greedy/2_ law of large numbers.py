'''
< 큰 수의 법칙 >

- 오름차순 정렬
- 가장 큰 값(리스트 맨 뒤 값)을 더해준다.
- 횟수가 k보다 커지게 되면, 두번째로 큰 값을 한 번 더해준다.
- 이를 총 횟수 m번 동안 반복

* 내장 함수 sort()의 시간복잡도는 O(NlogN)이다. +) for문은 O(N)
'''

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()  # 시간 복잡도 O(NlogN)
result = 0
i = 0

for _ in range(m):
    if(i == k):
        result += arr[n-2]
        i = 0
        continue
    result += arr[n-1]
    i += 1

print(result)

'''
M이 100억 이상일 경우, 시간 초과 발생

- {K만큼 반복한 가장 큰 수와 두 번째로 큰 수}가 반복된다. *반복되는 수열*의 길이는 K + 1 이 된다.
    - M // (K + 1)만큼 반복
- M이 K + 1로 나누어 떨어지지 않는 경우, M % (K + 1)를 더해준 값이 !가장 큰 수의 반복 횟수!

'''

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

# 가장 큰 수가 더해지는 횟수 계산
cnt = (m // (k+1)) * k  
cnt += m % (k+1)

print(cnt * arr[n-1] + (m - cnt) * arr[n-2]) 
