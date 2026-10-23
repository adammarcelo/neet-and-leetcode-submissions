from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.hash_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hash_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:        
        l, r = 0, len(self.hash_map[key]) - 1
        result = ""

        while l <= r:
            mid = (l + r) // 2

            if self.hash_map[key][mid][0] <= timestamp:
                result = self.hash_map[key][mid][1]
                l = mid + 1
            else:
                r = mid - 1
            
        return result