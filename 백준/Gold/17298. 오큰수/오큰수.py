from sys import stdin, stdout

n = int(stdin.readline())
array = list(map(int, stdin.readline().split()))
st = []
ans = [-1] * n

for idx, num in enumerate(array):
    while st and st[-1][1] < num:
        i, _ = st.pop()
        ans[i] = num
    st.append((idx, num))

stdout.write(" ".join(map(str, ans)))