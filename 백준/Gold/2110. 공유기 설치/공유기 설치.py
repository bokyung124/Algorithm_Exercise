n, c = map(int, input().split())
ls = [int(input()) for _ in range(n)]
ls.sort()

result = 0
start = 1
end = ls[-1] - ls[0]

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    current = ls[0]
    
    for i in range(1, len(ls)):
        if ls[i] >= current + mid:
            cnt += 1
            current = ls[i]
    
    if cnt >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)