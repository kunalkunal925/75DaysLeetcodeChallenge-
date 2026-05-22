import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = nums
        # Turn the list into a heap in-place: O(N)
        heapq.heapify(self.heap)
        
        # Keep only the k largest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        # Push new value into the heap: O(log K)
        heapq.heappush(self.heap, val)
        
        # If we have more than k elements, remove the smallest
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
            
        # The root is the kth largest: O(1)
        return self.heap[0]