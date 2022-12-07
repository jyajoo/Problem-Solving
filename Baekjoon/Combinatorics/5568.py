'''
백준 - https://www.acmicpc.net/problem/5568

< 카드 놓기 >
'''

from sys import stdin
from itertools import permutations

card = []
answer = []
n = int(stdin.readline())
k = int(stdin.readline())
for _ in range(n):
    card.append(int(stdin.readline()))

card_list = list(permutations(card, k))
num_list = []
for i in card_list:
    num = ''
    for j in i:
        num += str(j)
    if num not in num_list:
        num_list.append(num)

print(len(num_list))
