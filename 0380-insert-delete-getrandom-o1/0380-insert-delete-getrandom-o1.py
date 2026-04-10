import random

class RandomizedSet:

    def __init__(self):
        self.data_map = {}
        self.data_list = []

    def insert(self, val: int) -> bool:
        if val in self.data_map:
            return False
        self.data_map[val] = len(self.data_list)
        self.data_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data_map:
            return False
        
        # Swapping logic for O(1) removal
        last_element = self.data_list[-1]
        idx_to_remove = self.data_map[val]
        
        self.data_list[idx_to_remove] = last_element
        self.data_map[last_element] = idx_to_remove
        
        self.data_list.pop()
        del self.data_map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.data_list)