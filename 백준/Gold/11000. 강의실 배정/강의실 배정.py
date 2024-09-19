import sys
import heapq

n = int(sys.stdin.readline())
time = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
time.sort()

heap = []
for start, end in time:
    if heap and start >= heap[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, end)
    
sys.stdout.write(str(len(heap)))