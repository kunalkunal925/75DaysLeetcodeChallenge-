class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        total_sum = n * (n + 1) // 2
        x = int(total_sum**0.5)
        
        if x * x == total_sum:
            return x
        return -1