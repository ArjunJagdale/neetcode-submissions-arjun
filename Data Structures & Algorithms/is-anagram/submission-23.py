class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Build dictionary for s string
        h1 = {}
        for i in s:
            h1[i] = h1.get(i, 0) + 1
        # r = 0 a = 0 c = 0 e = 0
        # loop over t
        for i in t:
            if i not in h1 or h1[i] == 0:
                return False
            h1[i] -= 1
        
        return True
