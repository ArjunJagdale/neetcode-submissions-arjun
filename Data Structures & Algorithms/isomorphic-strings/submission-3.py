class Solution:
    def helper(self, s: str, t: str) -> bool:
        hm = {}
        for i in range(len(s)):
            if (s[i] in hm) and (hm[s[i]] != t[i]):
                return False
            hm[s[i]] = t[i]
        
        return True

    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.helper(s, t) and self.helper(t, s)