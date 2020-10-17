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
