class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
            
        def rob_linear(houses):
            prev2, prev1 = 0, 0
            for num in houses:
                current = max(prev1, prev2 + num)
                prev2 = prev1
                prev1 = current
            return prev1

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))