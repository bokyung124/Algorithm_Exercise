n, m = map(int, input().split())
ls = list(map(int, input().split()))

# 구해야 할 것: 최소 M미터의 나무를 가져가기 위해 설정해야 할 높이의 최댓값
# M: 원소 값에서 절단기 높이를 뺀 값들의 합
# 주어진 배열을 탐색하는게 아니라 자연수 배열을 탐색해야 함
# mid: 절단기 높이

lo = 0
hi = max(ls)

answer = 0

while lo <= hi:
    mid = (lo + hi) // 2
    s = 0
    diff = 0
    
    for i in ls:   
        diff = i - mid
        if diff > 0:
            s += diff
    if s >= m:
        answer = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(answer)