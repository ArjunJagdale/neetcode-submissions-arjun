class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(t) != len(s):
            return False
            
        h = {}

        for i in s:
            h[i] = h.get(i, 0) + 1
        
        for j in t:
            if j not in h or h[j] == 0:
                return False
            
            h[j] -= 1
        
        return True
        