import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.data_list = []
        self.index_map = defaultdict(set)

    def insert(self, val: int) -> bool:
        res = val not in self.index_map or not self.index_map[val]
        self.index_map[val].add(len(self.data_list))
        self.data_list.append(val)
        return res

    def remove(self, val: int) -> bool:
        if not self.index_map[val]:
            return False
        
        # Element ka koi bhi ek index nikaalein
        remove_idx = self.index_map[val].pop()
        last_element = self.data_list[-1]
        
        # Agar last element hi remove hone waala element nahi hai, toh swap karein
        if remove_idx < len(self.data_list) - 1:
            self.data_list[remove_idx] = last_element
            # Last element ka index update karein
            self.index_map[last_element].remove(len(self.data_list) - 1)
            self.index_map[last_element].add(remove_idx)
            
        self.data_list.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.data_list)