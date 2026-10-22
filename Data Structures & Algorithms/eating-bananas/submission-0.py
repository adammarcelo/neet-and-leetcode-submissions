import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_rate = max(piles)
        min_rate = 1

        while min_rate < max_rate:
            k = (max_rate + min_rate) // 2

            total_hours = 0

            for pile in piles:
                total_hours += math.ceil(pile/k)

            if total_hours <= h:
                max_rate = k
            else:
                min_rate = k + 1
        
        return min_rate