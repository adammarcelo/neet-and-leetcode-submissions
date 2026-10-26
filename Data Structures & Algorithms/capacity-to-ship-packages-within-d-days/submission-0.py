class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)

        while l < r:
            mid = (l + r) // 2 

            days_needed = 1
            current_weight = 0

            for weight in weights:
                if current_weight + weight > mid:
                    days_needed += 1
                    current_weight = weight
                else:
                    current_weight += weight
            
            if days_needed <= days:
                r = mid
            else:
                l = mid + 1
        
        return l