class StreamChecker:

    def __init__(self, words: list[str]):
        self.trie = {}
        self.stream = []
        for word in words:
            node = self.trie
            for char in reversed(word):
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['#'] = True

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        node = self.trie
        for i in range(len(self.stream) - 1, -1, -1):
            char = self.stream[i]
            if char in node:
                node = node[char]
                if '#' in node:
                    return True
            else:
                break
        return False