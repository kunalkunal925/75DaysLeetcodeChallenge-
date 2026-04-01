class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nxt_greater_map = {}
        stack = []

        for num in nums2:
            while stack and num > stack[-1]:
                nxt_greater_map[stack.pop()] = num
            stack.append(num)

        return [nxt_greater_map.get(n, -1) for n in nums1]