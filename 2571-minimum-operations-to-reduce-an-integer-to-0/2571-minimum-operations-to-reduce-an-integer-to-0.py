class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n > 0:
            if (n & 3) == 3:
                n += (n & -n)
                res += 1
            else:
                res += (n & 1)
                n >>= 1
        return res