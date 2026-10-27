from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        result, curr_sum = 0, 0

        if not nums:
            return 0
        
        for num in nums:
            curr_sum += num

            if curr_sum == k:
                result += 1
            
            if curr_sum - k in prefix:
                result += prefix[curr_sum - k]
            
            prefix[curr_sum] += 1
        
        return result