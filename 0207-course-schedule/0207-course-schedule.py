class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)
            
        visit_set = set()
        
        def dfs(crs):
            if crs in visit_set:
                return False
            if pre_map[crs] == []:
                return True
                
            visit_set.add(crs)
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False
            visit_set.remove(crs)
            
            pre_map[crs] = []
            return True
            
        for crs in range(numCourses):
            if not dfs(crs):
                return False
                
        return True