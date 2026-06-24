'''
백준 - https://www.acmicpc.net/problem/2607

< 비슷한 단어 >
'''
import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
target = input().strip()
words = [input().strip() for _ in range(n - 1)]

target_count = dict(Counter(target))
target_keys = target_count.keys()
answer = 0
for word in words:
    if abs(len(target) - len(word)) > 1:
        continue

    word_count = dict(Counter(word))
    word_keys = word_count.keys()
    keys = target_keys | word_keys
    count = 0
    for key in keys:
        t = target_count.get(key, 0)
        w = word_count.get(key, 0)
        if t != w:
            count += abs(t - w)
    if count <= 1:
        answer += 1
    elif abs(len(target) - len(word)) == 0 and count == 2:
        answer += 1

print(answer)

'''
'''
import sys
input = sys.stdin.readline

n = int(input())
target = input().strip()
words = [input().strip() for _ in range(n - 1)]

answer = 0
for word in words:
    if abs(len(target) - len(word)) > 1:
        continue
    
    keyword = list(target)
    word = list(word)
    count = 0
    for w in word:
        if w in keyword:
            keyword.remove(w)
        else:
            count += 1
    
    if len(keyword) <= 1 and count <= 1:
        answer += 1

print(answer)