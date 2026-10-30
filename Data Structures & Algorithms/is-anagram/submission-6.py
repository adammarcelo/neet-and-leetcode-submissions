class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count, t_count = defaultdict(int), defaultdict(int)

        for s_char in s:
            s_count[s_char] += 1

        for t_char in t:
            t_count[t_char] += 1
        
        return s_count == t_count