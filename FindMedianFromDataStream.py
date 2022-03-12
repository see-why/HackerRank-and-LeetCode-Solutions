# https://leetcode.com/problems/find-median-from-data-stream/

class MedianFinder:

    def __init__(self):
        self.smallHeap = []        
        self.largeHeap = []

        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallHeap, -1 * num)
        
        if (self.smallHeap and self.largeHeap and (-1 * self.smallHeap[0]) > self.largeHeap[0]):
            val = -1 * heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, val)
        
        if len(self.smallHeap) > len(self.largeHeap) + 1:
            val = -1 * heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, val)
        
        
        if len(self.largeHeap) > len(self.smallHeap) + 1:
            val = heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, -1 * val)
        

    def findMedian(self) -> float:                        
        if len(self.smallHeap) > len(self.largeHeap):
            median =  -1 * self.smallHeap[0]
        elif len(self.largeHeap) > len(self.smallHeap):
            median =  self.largeHeap[0]
        else:
            median = ((-1 * self.smallHeap[0])+ self.largeHeap[0])/2.0
        return median
        
