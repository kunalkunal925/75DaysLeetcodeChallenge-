class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Adjacency list banayein
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        # visitSet current recursive path ke courses track karta hai
        visitSet = set()
        
        def dfs(crs):
            # Agar course visitSet mein hai, matlab cycle mil gayi
            if crs in visitSet:
                return False
            # Agar course ke koi prerequisites nahi hain, toh ye pass hai
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            
            # Backtracking: path se hata dein aur preMap clean karein efficiency ke liye
            visitSet.remove(crs)
            preMap[crs] = []
            return True
        
        # Har course ke liye DFS chalayein (kyunki graph disconnected ho sakta hai)
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True