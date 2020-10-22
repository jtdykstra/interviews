import heapq

# simple heap sort 
def minSort():
    h = []
    heapq.heappush(h, 7)
    heapq.heappush(h, 3)
    heapq.heappush(h, 2)
    heapq.heappush(h, -1)

    while(h):
        print(heapq.heappop(h))
print("heap sort")
minSort()

# demonstrate heapify, which turns a list into a heap
def heapifyFunc():
    h = [7, 3, 2, 1]
    heapq.heapify(h) # turn list into heap
    while(h):
        print(heapq.heappop(h))
print("heapify")
heapifyFunc()

# nsmallest (and equivalent n largest)
def smallestLargest():
    l = [7,1,9,10,11,24]
    print(heapq.nsmallest(3, l))
    print(heapq.nlargest(3, l))
print("smallest/largest")
smallestLargest()

import heapq

class Solution:
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            
        def __lt__(self, p):
            return ((abs(self.x)**2 + abs(self.y)**2) > (abs(p.x)**2 + abs(p.y)**2))
            
        def getArrayVer(self):
            return [self.x, self.y]
    
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        h = []
       
        for p in points:
            if (len(h) < K):
                heapq.heappush(h, self.Point(p[0], p[1]))
            else:
                heapq.heappushpop(h, self.Point(p[0], p[1]))
                
        return [p.getArrayVer() for p in h]
            
        
