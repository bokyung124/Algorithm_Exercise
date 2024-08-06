# [level 2] 타겟 넘버 - 43165 

[문제 링크](https://school.programmers.co.kr/learn/courses/30/lessons/43165) 

### 성능 요약

메모리: 9.94 MB, 시간: 388.51 ms

### 구분

코딩테스트 연습 > 깊이／너비 우선 탐색（DFS／BFS）

### 채점결과

정확성: 100.0<br/>합계: 100.0 / 100.0

### 제출 일자

2024년 08월 03일 18:22:53

### 문제 설명

<p>n개의 음이 아닌 정수들이 있습니다. 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.</p>
<div class="highlight"><pre class="codehilite"><code>-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
</code></pre></div>
<p>사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.</p>

<h5>제한사항</h5>

<ul>
<li>주어지는 숫자의 개수는 2개 이상 20개 이하입니다.</li>
<li>각 숫자는 1 이상 50 이하인 자연수입니다.</li>
<li>타겟 넘버는 1 이상 1000 이하인 자연수입니다.</li>
</ul>

<h5>입출력 예</h5>
<table class="table">
        <thead><tr>
<th>numbers</th>
<th>target</th>
<th>return</th>
</tr>
</thead>
        <tbody><tr>
<td>[1, 1, 1, 1, 1]</td>
<td>3</td>
<td>5</td>
</tr>
<tr>
<td>[4, 1, 2, 1]</td>
<td>4</td>
<td>2</td>
</tr>
</tbody>
      </table>
<h5>입출력 예 설명</h5>

<p><strong>입출력 예 #1</strong></p>

<p>문제 예시와 같습니다.</p>

<p><strong>입출력 예 #2</strong></p>
<div class="highlight"><pre class="codehilite"><code>+4+1-2+1 = 4
+4-1+2-1 = 4
</code></pre></div>
<ul>
<li>총 2가지 방법이 있으므로, 2를 return 합니다.</li>
</ul>


## 풀이

```python
cnt = 0
 
def dfs(numbers, target, current, idx):
    global cnt
    
    if idx == len(numbers):
        if current == target:
            cnt += 1
        return
    
    dfs(numbers, target, current + numbers[idx], idx + 1)
    dfs(numbers, target, current - numbers[idx], idx + 1)

def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return cnt
```

- dfs 종료 조건: 숫자 배열의 끝까지 탐색했을 때 (모든 숫자 처리)
    - 현재 계산 결과가 타겟 넘버와 같으면 cnt 증가

- 주어진 숫자 배열에서 idx를 1씩 증가시키면서 해당 숫자를 더하거나 빼는 경우에 대해 재귀적으로 dfs 수행
    - *모든 경우의 수*에 대해 계산하여 값과 비교할 수 있음

- **시간복잡도**: O(2^n)
    - 리스트의 길이가 n일 때 각 숫자에 대해 더하거나 빼는 두 가지 경우가 있기 때문

- **공간복잡도**: O(n)
    - 재귀 호출 -> 리스트의 길이만큼 반복
    - 두 번의 dfs 호출은 순차적으로 실행 -> 첫번째 dfs 호출이 완료되면 해당 스택 메모리 해제 -> 두번째 dfs가 해당 스택 공간 재사용 => O(n)
    - `콜 스택`: 프로그램이 함수를 호출할 때마다 호출 정보가 콜 스택에 쌓임 -> 재귀 함수를 호출할 때마다 새로운 스택 프레임이 콜 스택에 추가됨
        - `스택 프레임`: 함수의 매개변수, 지역 변수, 반환 주소 등의 정보가 포함됨