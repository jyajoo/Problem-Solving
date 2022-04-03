'''
< ZOAC >

- 보여주지 않은 문자 중, 추가했을 때의 문자열이 사전 순으로 가장 앞에 오도록 한다.
- AINK와 ALIK 중 AINK가 사전 순으로 더 앞이다.

- [출력 초과]
반례 : ACC(무한 반복)
중복되는 문자로 인해 인덱스 사용시, 최초 인덱스를 출력하므로 실패.
- visit로 방문 표기하여 해결해보자.
- 오른쪽 부분 슬라이싱 후, 왼쪽 부분 풀스캔하며 사전 순으로 추가하는 방식
-> 왼쪽 부분에서도 다시 오른쪽 부분을 슬라이싱해나가야 하는 방식으로 바꾸기로 했다.

기준이 되는 start와 end를 설정하여 슬라이싱해준다.
start를 덱에 보관해두며, 더이상 오른쪽 부분으로 이동할 수 없을 경우,
보관해둔 이전 인덱스를 통해 왼쪽 부분을 슬라이싱할 수 있도록 한다.
'''
from collections import deque

def print_result():
    for i in range(len(n)):
        if visit[i] == 1:
            print(n[i], end='')
    print()

n = input()
visit = [0] * len(n)
prev = deque()
prev.append(0)
start = 0
end = len(n)

while 0 in visit:
    if start == end:
        end = prev.pop() - 1
        start = prev.pop()
        prev.append(start)
    arr = n[start: end]
    arr = sorted(arr)
    if start != end:
        for i in range(start, end):                  
            if arr[0] == n[i] and visit[i] == 0:
                visit[i] = 1
                start = i + 1
                prev.append(start)
                if start == end:
                    end = prev.pop() - 1
                    start = prev.pop() 
                    prev.append(start)
                break
        print_result()