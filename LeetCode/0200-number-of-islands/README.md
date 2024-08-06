<h2><a href="https://leetcode.com/problems/number-of-islands/">200. Number of Islands</a></h2><h3>Medium</h3><hr><p>Given an <code>m x n</code> 2D binary grid <code>grid</code> which represents a map of <code>&#39;1&#39;</code>s (land) and <code>&#39;0&#39;</code>s (water), return <em>the number of islands</em>.</p>

<p>An <strong>island</strong> is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> grid = [
  [&quot;1&quot;,&quot;1&quot;,&quot;1&quot;,&quot;1&quot;,&quot;0&quot;],
  [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;1&quot;,&quot;0&quot;],
  [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;],
  [&quot;0&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;]
]
<strong>Output:</strong> 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> grid = [
  [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;],
  [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;],
  [&quot;0&quot;,&quot;0&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;],
  [&quot;0&quot;,&quot;0&quot;,&quot;0&quot;,&quot;1&quot;,&quot;1&quot;]
]
<strong>Output:</strong> 3
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 300</code></li>
	<li><code>grid[i][j]</code> is <code>&#39;0&#39;</code> or <code>&#39;1&#39;</code>.</li>
</ul>

### 풀이

```python
class Solution(object):

    def numIslands(self, grid):
        def dfs(i,j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return

            # 방문한 곳
            grid[i][j] =0

            # 연결된 1에 대해 dfs 수행
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        cnt = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i,j)
                    cnt +=1
        return cnt
```

- dfs 종료 조건: grid 경계를 벗어나거나, 1이 아닌 경우 (바다)

- grid의 왼쪽 상단에서부터 탐색하면서 값이 1인 경우 해당 셀에서 dfs 실행
  - 방문한 곳은 0으로 변경
  - 인접한 네 방향에 대해 dfs 수행
  - 연결된 모든 1을 찾아 0으로 변경
  - `dfs(i,j)` 을 수행하면 하나의 섬 전체를 탐색한 뒤 종료 -> cnt 1 증가

- **시간복잡도**: O(m * n)
  - grid 크기가 m x n일 때
  - 각 셀은 최대 한 번 방문할 수 있고, 모든 셀을 한 번씩 방문

- **공간복잡도**: O(m * n)
  - 한 섬을 탐색할 때 연속적으로 이어지는 1의 최대 길이와 연관
  - 최악의 경우 -> grid가 모두 1로 채워져있으면 재귀 깊이 O(m * n)
  - 평균적인 경우 -> 한 섬의 크기는 전체 grid보다 작을 수 있기 때문에 O(min(m, n))이 될 수 있음


#### 반복적 DFS

```python
class Solution(object):

    def numIslands(self, grid):
        if not grid:
            return 0

        cnt = 0
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    cnt += 1
                    self.dfs(grid, i, j)
        
        return cnt

    def dfs(self, grid, start_i, start_j):
        stack = [(start_i, start_j)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while stack:
            i, j = stack.pop()
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
                grid[i][j] = "0" 
                
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    stack.append((ni, nj))
```

- 이 문제에서는 재귀적 DFS가 더 빨랐지만, 두 가지 방법이 가능하다는 것!
  - 재귀 호출 대신 스택(stack)을 사용하여 방문할 셀 관리
  - `directions` 배열로 인접한 셀 탐색 방향 지정
  - 스택이 빌 때까지 dfs를 반복하며 값이 1일 경우에 0으로 변경 -> 인접한 셀을 스택에 추가하여 다음 반복에서 처리
