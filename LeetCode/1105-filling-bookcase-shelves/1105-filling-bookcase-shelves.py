class Solution:
    def minHeightShelves(self, books, shelfWidth):
        n = len(books)
        dp = [1000001] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            width = 0
            height = 0
            j = i - 1
            while j >= 0 and width + books[j][0] <= shelfWidth:
                width += books[j][0]
                height = max(height, books[j][1])
                dp[i] = min(dp[i], dp[j] + height)
                j -= 1

        return dp[n]
