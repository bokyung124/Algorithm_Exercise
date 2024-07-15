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