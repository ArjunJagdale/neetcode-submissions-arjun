class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        h = {}

        for i in s:
            h[i] = h.get(i, 0) + 1
        
        for x in t:
            if x not in h or h[x] == 0:
                return False
            
            h[x] -= 1
        
        return True