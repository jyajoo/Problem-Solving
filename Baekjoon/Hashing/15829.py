'''
백준 - https://www.acmicpc.net/problem/15829

<Hashing>

'''
r = 31
m = 1234567891
n = int(input())
word = input()
sum = 0
for i in range(n):
    sum += (ord(word[i]) - 96) * (r ** i)

print(sum % m)
