from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_counts = Counter(tasks)
        frequencies = list(task_counts.values())
        
        max_freq = max(frequencies)
        max_freq_count = frequencies.count(max_freq)
        
        intervals_needed = (max_freq - 1) * (n + 1) + max_freq_count
        
        return max(len(tasks), intervals_needed)