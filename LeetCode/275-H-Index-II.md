# [문제](https://leetcode.com/problems/h-index-ii/description/)

Given an array of integers `citations` where `citations[i]` is the number of citations a researcher received for their `ith` paper and `citations` is sorted in **ascending order**, return the *researcher's h-index*.

According to the [definition of h-index on Wikipedia](https://en.wikipedia.org/wiki/H-index): The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least `h` times.

You must write an algorithm that runs in logarithmic time.

<br>

**Example 1:**

> **Input:** citations = [0,1,3,5,6]
> **Output:** 3
> **Explanation:** [0,1,3,5,6] means the researcher has 5 papers in total and each of them had received 0, 1, 3, 5, 6 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

<br>

**Example 2:**

> **Input:** citations = [1,2,100]
> **Output:** 2

<br>

**Constraints:**

- `n == citations.length`
- `1 <= n <= 105`
- `0 <= citations[i] <= 1000`
- `citations` is sorted in **ascending order**.

# 풀이

- citations: 논문의 번호이자 논문이 인용된 수
- h-index: 해당 연구자가 적어도 h번 이상 인용된 적어도 h개의 논문을 출판했을 때의 h의 최대값

-> 정렬된 배열에서 최적의 h 값을 찾는 문제 + 문제에서 요구한 *로그 시간* 알고리즘 => **이진탐색**

<br>

```python
class Solution(object):
    def hIndex(self, citations):
        answer = 0
        n = len(citations)
        left = 0
        right = n-1

        while left <= right:
            mid = (left + right) // 2
            if citations[mid] >= n - mid:
                answer = n - mid
                right = mid - 1
            else:
                left = mid + 1
        return answer
```

- 리스트의 양 끝 인덱스를 각각 `left`, `right`으로 정의, 평균 인덱스 값을 `mid`로 정의
- mid 인덱스부터 리스트 끝까지의 길이 (`n-mid`)와 `citations[mid]` 값을 비교하여 `citations[mid]`의 인용된 횟수와 `citations[mid]`번 인용된 논문의 개수를 비교
- `mid` 이후의 모든 논문도 최소 `citations[mid]`번 이상 인용 되었을 것
- 따라서, 인용 수가 `citations[mid]` 이상인 논문의 개수: **n-mid**


# 시간 복잡도

O(log n)