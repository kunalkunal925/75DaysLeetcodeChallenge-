class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for n in nums:
            index = abs(n) - 1
            nums[index] = -abs(nums[index])
            
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        return res