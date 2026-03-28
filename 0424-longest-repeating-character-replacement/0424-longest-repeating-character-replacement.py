class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        max_f = 0
        l = 0
        res = 0
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            max_f = max(max_f, count[s[r]])
            
            if (r - l + 1) - max_f > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            
        return res