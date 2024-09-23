class MedianFinder(object):
    import heapq

    def __init__(self):
        self.maxhp = []
        self.minhp = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        # 최대 힙에 숫자 추가
        heapq.heappush(self.maxhp, -num)
        
        # 최대 힙의 최대값이 최소 힙의 최소값보다 크면 교환
        if self.maxhp and self.minhp and (-self.maxhp[0] > self.minhp[0]):
            heapq.heappush(self.minhp, -heapq.heappop(self.maxhp))
        
        # 최대 힙의 크기가 최소 힙의 크기보다 크면 최소 힙으로 이동
        if len(self.maxhp) > len(self.minhp) + 1:
            heapq.heappush(self.minhp, -heapq.heappop(self.maxhp))
        
        # 최소 힙의 크기가 최대 힙의 크기보다 크면 최대 힙으로 이동
        if len(self.minhp) > len(self.maxhp):
            heapq.heappush(self.maxhp, -heapq.heappop(self.minhp))


    def findMedian(self):
        """
        :rtype: float
        """ 
        if len(self.maxhp) == len(self.minhp):
            return (-self.maxhp[0] + self.minhp[0]) / 2.0
        else:
            return -self.maxhp[0]
            

        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()