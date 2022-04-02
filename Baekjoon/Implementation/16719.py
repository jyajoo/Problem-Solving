'''
< ZOAC >

- 보여주지 않은 문자 중, 추가했을 때의 문자열이 사전 순으로 가장 앞에 오도록
- AINK와 ALIK 중 AINK가 사전 순으로 더 앞이다.

- [출력 초과]
반례 : ACC(무한 반복)
중복되는 문자로 인해 인덱스 사용시, 최초 인덱스를 출력하므로 실패.
- check로 방문 표기하여 해결
'''

def print_result():
    for i in result:
        print(i, end="")
    print()

n = input()
idx = [0]     # 정렬 첫 문자로부터 오른쪽 부분을 슬라이싱하며, 첫 문자들의 인덱스 리스트.
x = -1        # 인덱스 초깃값
result = [''] * len(n)

while x + 1 < len(n):
    arr = n[x + 1:]                # 정렬된 첫 문자를 찾고, 그 문자의 오른쪽 부분 슬라이싱.
    s = sorted(arr)                # 사전 순 정렬
    x = n.index(s[0])
    idx.append(x + 1)              # 정렬 첫 문자의 인덱스 + 1 값을 보관한다.
    result[n.index(s[0])] = s[0]   # 기존 문자열에서 인덱스를 찾고, 해당 인덱스에 값 대입
    print_result()

idx.sort(reverse=True)

for i in range(len(idx) - 1):
    arr = n[idx[i + 1]: idx[i] - 1]   # 기존 문자열에서 result에 포함되지 않은 부분 슬라이싱
    arr_sort = sorted(arr)

    # 정렬된 순으로 arr + idx[i + 1] (기존 문자열에서의 인덱스)를 찾아 대입
    for j in arr_sort:
        result[arr.index(j) + idx[i + 1]] = j
        print_result()
