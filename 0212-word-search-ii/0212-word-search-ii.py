class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.word = None

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word
            
        rows, cols = len(board), len(board[0])
        result = []
        
        def dfs(r, c, parent_node):
            char = board[r][c]
            current_node = parent_node.children[char]
            
            if current_node.word:
                result.append(current_node.word)
                current_node.word = None
                
            board[r][c] = '#'
            
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in current_node.children:
                    dfs(nr, nc, current_node)
                    
            board[r][c] = char
            
            if not current_node.children:
                parent_node.children.pop(char)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root.children:
                    dfs(r, c, root)
                    
        return result