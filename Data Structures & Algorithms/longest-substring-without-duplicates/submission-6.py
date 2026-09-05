class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        res = 0
        Chatset = set()

        for r in range(len(s)):
            while s[r] in Chatset:
                Chatset.remove(s[l])
                l += 1
            Chatset.add(s[r])
            res = max(res, r-l+1)
        
        return res
