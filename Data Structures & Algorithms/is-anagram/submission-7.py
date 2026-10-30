class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count, t_count = defaultdict(int), defaultdict(int)

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            s_count[s[i]] += 1
            t_count[t[i]] += 1
        
        return s_count == t_count