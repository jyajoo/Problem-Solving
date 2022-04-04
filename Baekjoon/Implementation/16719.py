'''
< ZOAC >

- 보여주지 않은 문자 중, 추가했을 때의 문자열이 사전 순으로 가장 앞에 오도록 한다.
- AINK와 ALIK 중 AINK가 사전 순으로 더 앞이다.

- [출력 초과]
반례 : ACC(무한 반복)
중복되는 문자로 인해 .index() 사용시, 최초 인덱스를 출력하므로 실패.
- visit로 방문 표기하여 해결해보자.
- 오른쪽 부분 슬라이싱 후, 왼쪽 부분 풀스캔하며 사전 순으로 추가하는 방식
-> 왼쪽 부분에서도 다시 오른쪽 부분을 슬라이싱해나가야 하는 방식으로 바꾸기로 했다.

기준이 되는 start와 end를 설정하여 슬라이싱해준다.
start(기준점)를 덱에 보관해두며, 더이상 오른쪽 부분으로 이동할 수 없을 경우,
보관해둔 이전 start를 통해 왼쪽 부분을 슬라이싱할 수 있도록 한다.
'''
# from collections import deque

# def print_result():                # 방문한 문자만 출력
#     for i in range(len(n)):
#         if visit[i] == 1:
#             print(n[i], end='')
#     print()

# n = input()
# visit = [0] * len(n)     # 방문한 곳 확인
# prev = deque()           # 시작 지점인 start 인덱스값을 모아둔다.
# prev.append(0)
# start = 0
# end = len(n)

# while 0 in visit:              # 모든 문자가 방문될 때까지 반복, in 연산자의 시간복잡도는 O(N)
#     arr = n[start: end]
#     arr = sorted(arr)
#     if start == end:           # start와 end가 같다면, 리스트 슬라이싱으로 아무 값도 담을 수 없다.
#         end = prev.pop() - 1   # 이전 end에서 1을 빼주고, 이전 start값을 가져온다. (왼쪽 부분으로 이동)
#         start = prev.pop()
#         prev.append(start)
#     else:
#         for i in range(start, end):     # 정렬로 사전 순 가장 첫 문자와 동일하고, 방문한 적이 없는지 확인
#             if arr[0] == n[i] and visit[i] == 0:
#                 visit[i] = 1        # 방문 표시
#                 start = i + 1       # 시작 지점 업데이트 후 덱에 담기
#                 prev.append(start)
#                 break
#         print_result()

'''
- 좌우로 슬라이싱이 반복되니 재귀함수로 풀이할 수도 있다.
'''
n = input()
visit = [0] * len(n)

def zoac(start, end):
    if start == end:
        return
        
    idx = start
    arr = n[start: end]
    arr = sorted(arr)
    for i in range(start, end):
        if arr[0] == n[i] and visit[i] == 0:
            visit[i] = 1
            start = i + 1
            break
    for i in range(len(n)):
        if visit[i] == 1:
            print(n[i], end='')
    print()

    zoac(start, end)
    zoac(idx, start - 1)


zoac(0, len(n))
