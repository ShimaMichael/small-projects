import heapq

class MedianFinder:
    def __init__(self):
        self.min_heap = [] # 4
        self.max_heap = [] # -3,-2,-1

    def add(self, number: int):#1
        if len(self.min_heap) == 0 or number <= abs(self.max_heap[0]):
            heapq.heappush(self.max_heap, -number)
        else:
            heapq.heappush(self.min_heap, number)

        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, abs(heapq.heappop(self.max_heap)))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def get_median(self):
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2

heap = []
heap2 = []
heapq.heappush(heap, -7)
heapq.heappush(heap, -5)
heapq.heappush(heap, -9)

heapq.heappush(heap2, 2)
heapq.heappush(heap2, 4)
print(heap)
print(heap2)