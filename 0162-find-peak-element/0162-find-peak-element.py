class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] < nums[mid + 1]:
                # We are on an upward slope, peak must be on the right
                left = mid + 1
            else:
                # We are on a downward slope, peak is mid or to the left
                right = mid
                
        return left