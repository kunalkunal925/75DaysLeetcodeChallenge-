from bisect import bisect_left

class SummaryRanges:

    def __init__(self):
        self.nums = set()
        self.intervals = []

    def addNum(self, value: int) -> None:
        if value in self.nums:
            return
        
        self.nums.add(value)
        
        n = len(self.intervals)
        idx = bisect_left(self.intervals, [value, value])
        
        left_merge = (idx > 0 and self.intervals[idx-1][1] + 1 == value)
        right_merge = (idx < n and self.intervals[idx][0] - 1 == value)
        
        if left_merge and right_merge:
            self.intervals[idx-1][1] = self.intervals[idx][1]
            self.intervals.pop(idx)
        elif left_merge:
            self.intervals[idx-1][1] = value
        elif right_merge:
            self.intervals[idx][0] = value
        else:
            self.intervals.insert(idx, [value, value])

    def getIntervals(self) -> list[list[int]]:
        return self.intervals