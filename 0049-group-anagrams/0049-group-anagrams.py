class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams_map = {}
        
        for word in strs:
            sorted_word = "".join(sorted(word))
            
            if sorted_word not in anagrams_map:
                anagrams_map[sorted_word] = []
            
            anagrams_map[sorted_word].append(word)
            
        return list(anagrams_map.values())