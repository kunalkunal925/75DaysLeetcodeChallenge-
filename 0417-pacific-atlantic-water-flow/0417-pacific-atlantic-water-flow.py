class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights or not heights[0]:
            return []
            
        rows, cols = len(heights), len(heights[0])
        pac_set = set()
        atl_set = set()
        
        def dfs(r, c, visit_set, prev_height):
            if (r, c) in visit_set or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prev_height:
                return
            
            visit_set.add((r, c))
            
            dfs(r + 1, c, visit_set, heights[r][c])
            dfs(r - 1, c, visit_set, heights[r][c])
            dfs(r, c + 1, visit_set, heights[r][c])
            dfs(r, c - 1, visit_set, heights[r][c])
            
        for c in range(cols):
            dfs(0, c, pac_set, heights[0][c])
            dfs(rows - 1, c, atl_set, heights[rows - 1][c])
            
        for r in range(rows):
            dfs(r, 0, pac_set, heights[r][0])
            dfs(r, cols - 1, atl_set, heights[r][cols - 1])
            
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac_set and (r, c) in atl_set:
                    result.append([r, c])
                    
        return result