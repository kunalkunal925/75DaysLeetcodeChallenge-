import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        left = 1
        right = max(piles)
        
        while left < right:
            mid = left + (right - left) // 2
            total_hours = 0
            
            for pile in piles:
                total_hours += (pile + mid - 1) // mid
            
            if total_hours <= h:
                right = mid
            else:
                left = mid + 1
                
        return left