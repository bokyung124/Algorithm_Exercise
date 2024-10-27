from sys import stdin, stdout
from collections import Counter

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
count = Counter(arr)
st = []
ans = [-1] * n

for idx, num in enumerate(arr):
    while st and st[-1][1] < count[num]:
        i, _ = st.pop()
        ans[i] = num
    st.append((idx, count[num]))

stdout.write(" ".join(map(str, ans)))
