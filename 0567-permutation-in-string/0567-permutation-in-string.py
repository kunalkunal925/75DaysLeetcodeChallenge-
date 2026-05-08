class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
            
        s1_counts = [0] * 26
        s2_counts = [0] * 26
        
        for i in range(n1):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1
            
        if s1_counts == s2_counts:
            return True
            
        for i in range(n1, n2):
            s2_counts[ord(s2[i]) - ord('a')] += 1
            s2_counts[ord(s2[i - n1]) - ord('a')] -= 1
            if s1_counts == s2_counts:
                return True
                
        return False