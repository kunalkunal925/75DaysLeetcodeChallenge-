class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in num_map:
                return [num_map[complement], i]
            num_map[n] = i
        return []  