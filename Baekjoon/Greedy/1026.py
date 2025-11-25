'''
백준 - https://www.acmicpc.net/problem/1026

< 보물 >
'''
import sys

input = sys.stdin.readline

'''
길이가 n인 정수 배열 a, b
s = a[0] x b[0] + ... + a[n-1] x b[n-1]
s의 값을 작게 만들기 위해 a를 재배열, b는 그대로
s의 최솟값 출력
'''

'''
n은 50보다 작거나 같은 수, 각 원소는 100보다 작거나 음이 아닌 정수
그리디 - 순간 가장 좋은 것을 선택하는 알고리즘
a를 정렬하여 최솟값이 구해지도록 하기

b 배열에 맞춰 b의 원소가 크면 작은 a의 원소를 배치하도록 정렬
-> a, b 반대로 정렬 후 s 구하기

시간 복잡도는 sort 함수의 O(NlogN)이 된다.
'''

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

s = 0
for i in range(n):
    s += a[i] * b[i]

print(s)