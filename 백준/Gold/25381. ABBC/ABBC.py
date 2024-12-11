from sys import stdin, stdout
from collections import deque


def solution(S):
    n = len(S)
    # 각 문자의 인덱스를 저장할 큐 생성
    a_queue = deque()
    b_queue = deque()
    c_queue = deque()

    # 각 문자의 인덱스를 해당하는 큐에 저장
    for i in range(n):
        if S[i] == "A":
            a_queue.append(i)
        elif S[i] == "B":
            b_queue.append(i)
        else:  # S[i] == 'C'
            c_queue.append(i)

    result = 0
    used = set()  # 사용된 인덱스를 저장할 집합

    # 각 B에 대해 처리
    while b_queue:
        b_idx = b_queue.popleft()
        if b_idx in used:
            continue

        # 현재 B보다 앞에 있는 사용 가능한 A 찾기
        a_idx = -1
        while a_queue and a_queue[0] < b_idx:
            if a_queue[0] not in used:
                a_idx = a_queue[0]
                break
            a_queue.popleft()

        # 현재 B보다 뒤에 있는 사용 가능한 C 찾기
        c_idx = -1
        while c_queue and c_queue[0] <= b_idx:
            c_queue.popleft()
        if c_queue and c_queue[0] not in used:
            c_idx = c_queue[0]

        # AB 쌍과 BC 쌍 중 선택
        if a_idx != -1 and c_idx != -1:
            # 다음 B의 위치를 고려하여 선택
            if len(b_queue) > 0 and b_queue[0] not in used:
                # BC 쌍 선택 (다음 B를 위해 A를 남김)
                used.add(b_idx)
                used.add(c_idx)
                c_queue.popleft()
            else:
                # AB 쌍 선택
                used.add(a_idx)
                used.add(b_idx)
                a_queue.popleft()
            result += 1
        elif a_idx != -1:
            # AB 쌍만 가능
            used.add(a_idx)
            used.add(b_idx)
            a_queue.popleft()
            result += 1
        elif c_idx != -1:
            # BC 쌍만 가능
            used.add(b_idx)
            used.add(c_idx)
            c_queue.popleft()
            result += 1

    return result


S = stdin.readline().strip()
stdout.write(str(solution(S)))
